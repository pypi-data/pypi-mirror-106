from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cswitched'):
			from .Connection_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	# noinspection PyTypeChecker
	def get_current(self) -> enums.CurrentConnectionType:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:CONNection:CURRent \n
		Snippet: value: enums.CurrentConnectionType = driver.sense.connection.get_current() \n
		Queries the type of the current connection. \n
			:return: type_py: NONE | VOICe | VIDeo | SRB | TEST | PACKet NONE: none active connection VOICe: voice connection VIDeo: video connection SRB: signaling radio bearer only TEST: test mode PACKet: packet data connection using DAU
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:CONNection:CURRent?')
		return Conversions.str_to_scalar_enum(response, enums.CurrentConnectionType)

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
