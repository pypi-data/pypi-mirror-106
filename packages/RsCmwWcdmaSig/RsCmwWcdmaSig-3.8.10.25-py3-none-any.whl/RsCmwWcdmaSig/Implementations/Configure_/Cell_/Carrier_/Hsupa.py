from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsupa:
	"""Hsupa commands group definition. 17 total commands, 5 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsupa", core, parent)

	@property
	def ehrch(self):
		"""ehrch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ehrch'):
			from .Hsupa_.Ehrch import Ehrch
			self._ehrch = Ehrch(self._core, self._base)
		return self._ehrch

	@property
	def eagch(self):
		"""eagch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eagch'):
			from .Hsupa_.Eagch import Eagch
			self._eagch = Eagch(self._core, self._base)
		return self._eagch

	@property
	def ehich(self):
		"""ehich commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ehich'):
			from .Hsupa_.Ehich import Ehich
			self._ehich = Ehich(self._core, self._base)
		return self._ehich

	@property
	def ergch(self):
		"""ergch commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ergch'):
			from .Hsupa_.Ergch import Ergch
			self._ergch = Ergch(self._core, self._base)
		return self._ergch

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_etfci'):
			from .Hsupa_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ENABle \n
		Snippet: value: bool = driver.configure.cell.carrier.hsupa.get_enable() \n
		Enables/disables additional uplink carrier in scenarios with multiple uplink carriers. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ENABle \n
		Snippet: driver.configure.cell.carrier.hsupa.set_enable(enable = False) \n
		Enables/disables additional uplink carrier in scenarios with multiple uplink carriers. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ENABle {param}')

	def clone(self) -> 'Hsupa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsupa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
