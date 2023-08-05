from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 20 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	@property
	def outgoing(self):
		"""outgoing commands group. 2 Sub-classes, 12 commands."""
		if not hasattr(self, '_outgoing'):
			from .Sms_.Outgoing import Outgoing
			self._outgoing = Outgoing(self._core, self._base)
		return self._outgoing

	@property
	def incoming(self):
		"""incoming commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_incoming'):
			from .Sms_.Incoming import Incoming
			self._incoming = Incoming(self._core, self._base)
		return self._incoming

	def get_kt_loop(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:SMS:KTLoop \n
		Snippet: value: bool = driver.configure.sms.get_kt_loop() \n
		Specifies whether the test loop is kept closed for an established RMC connection with test loop, when an SMS message is
		sent to the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:SMS:KTLoop?')
		return Conversions.str_to_bool(response)

	def set_kt_loop(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:SMS:KTLoop \n
		Snippet: driver.configure.sms.set_kt_loop(enable = False) \n
		Specifies whether the test loop is kept closed for an established RMC connection with test loop, when an SMS message is
		sent to the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:SMS:KTLoop {param}')

	def clone(self) -> 'Sms':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sms(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
