from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cycle:
	"""Cycle commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cycle", core, parent)

	@property
	def tti(self):
		"""tti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tti'):
			from .Cycle_.Tti import Tti
			self._tti = Tti(self._core, self._base)
		return self._tti

	def get_ithreshold(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:MAC:CYCLe:ITHReshold \n
		Snippet: value: int or bool = driver.configure.cell.cpc.mac.cycle.get_ithreshold() \n
		Restricts the starting points of the uplink transmission on E-DCH for a particular UE. E-DCH inactivity time after which
		the UE can start E-DCH transmission only at given times, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: threshold: 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | ON | OFF Values in E-DCH TTIs, additional OFF | ON disables | enables the threshold If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 512 E-DCH TTI, Unit: E-DCH TTI
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:MAC:CYCLe:ITHReshold?')
		return Conversions.str_to_int_or_bool(response)

	def set_ithreshold(self, threshold: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:MAC:CYCLe:ITHReshold \n
		Snippet: driver.configure.cell.cpc.mac.cycle.set_ithreshold(threshold = 1) \n
		Restricts the starting points of the uplink transmission on E-DCH for a particular UE. E-DCH inactivity time after which
		the UE can start E-DCH transmission only at given times, see 'Continuous Packet Connectivity (CPC) '. \n
			:param threshold: 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | ON | OFF Values in E-DCH TTIs, additional OFF | ON disables | enables the threshold If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 512 E-DCH TTI, Unit: E-DCH TTI
		"""
		param = Conversions.decimal_or_bool_value_to_str(threshold)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:MAC:CYCLe:ITHReshold {param}')

	def clone(self) -> 'Cycle':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cycle(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
