from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 9 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handover", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Handover_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_external'):
			from .Handover_.External import External
			self._external = External(self._core, self._base)
		return self._external

	def get_destination(self) -> str:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: value: str = driver.prepare.handover.get_destination() \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwWcdmaSig.
		Prepare.Handover.Catalog.destination. \n
			:return: destination: Destination as string
		"""
		response = self._core.io.query_str('PREPare:WCDMa:SIGNaling<Instance>:HANDover:DESTination?')
		return trim_str_response(response)

	def set_destination(self, destination: str) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:DESTination \n
		Snippet: driver.prepare.handover.set_destination(destination = '1') \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwWcdmaSig.
		Prepare.Handover.Catalog.destination. \n
			:param destination: Destination as string
		"""
		param = Conversions.value_to_quoted_str(destination)
		self._core.io.write(f'PREPare:WCDMa:SIGNaling<Instance>:HANDover:DESTination {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.MobilityMode:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: value: enums.MobilityMode = driver.prepare.handover.get_mmode() \n
		Selects the mechanism to be used for mobility management. \n
			:return: mobility_mode: HANDover | REDirection | CCORder Handover, redirection, or cell change order
		"""
		response = self._core.io.query_str('PREPare:WCDMa:SIGNaling<Instance>:HANDover:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.MobilityMode)

	def set_mmode(self, mobility_mode: enums.MobilityMode) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: driver.prepare.handover.set_mmode(mobility_mode = enums.MobilityMode.CCORder) \n
		Selects the mechanism to be used for mobility management. \n
			:param mobility_mode: HANDover | REDirection | CCORder Handover, redirection, or cell change order
		"""
		param = Conversions.enum_scalar_to_str(mobility_mode, enums.MobilityMode)
		self._core.io.write(f'PREPare:WCDMa:SIGNaling<Instance>:HANDover:MMODe {param}')

	def clone(self) -> 'Handover':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Handover(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
