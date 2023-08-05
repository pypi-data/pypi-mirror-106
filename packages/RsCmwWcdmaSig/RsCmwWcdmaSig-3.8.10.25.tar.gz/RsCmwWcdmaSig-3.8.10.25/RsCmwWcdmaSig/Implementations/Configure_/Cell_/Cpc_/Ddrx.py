from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddrx:
	"""Ddrx commands group definition. 5 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ddrx", core, parent)

	@property
	def cycle(self):
		"""cycle commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cycle'):
			from .Ddrx_.Cycle import Cycle
			self._cycle = Cycle(self._core, self._base)
		return self._cycle

	@property
	def gmonitoring(self):
		"""gmonitoring commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gmonitoring'):
			from .Ddrx_.Gmonitoring import Gmonitoring
			self._gmonitoring = Gmonitoring(self._core, self._base)
		return self._gmonitoring

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:ENABle \n
		Snippet: value: bool = driver.configure.cell.cpc.ddrx.get_enable() \n
		Defines the settings for the discontinuous reception in the downlink, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: enable: OFF | ON enables/disables UE DRX
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:ENABle \n
		Snippet: driver.configure.cell.cpc.ddrx.set_enable(enable = False) \n
		Defines the settings for the discontinuous reception in the downlink, see 'Continuous Packet Connectivity (CPC) '. \n
			:param enable: OFF | ON enables/disables UE DRX
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:ENABle {param}')

	def clone(self) -> 'Ddrx':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ddrx(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
