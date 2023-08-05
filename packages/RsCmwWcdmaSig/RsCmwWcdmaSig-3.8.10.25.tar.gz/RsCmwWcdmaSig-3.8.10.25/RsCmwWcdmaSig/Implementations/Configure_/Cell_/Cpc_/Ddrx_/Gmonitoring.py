from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gmonitoring:
	"""Gmonitoring commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gmonitoring", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:GMONitoring:ENABle \n
		Snippet: value: bool = driver.configure.cell.cpc.ddrx.gmonitoring.get_enable() \n
		Defines the settings for the discontinuous reception in the downlink, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: enable: OFF | ON enables/disables UE monitoring of E-AGCH/E-RGCH when they overlap with the start of a UE DRX HS-SCCH reception
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:GMONitoring:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:GMONitoring:ENABle \n
		Snippet: driver.configure.cell.cpc.ddrx.gmonitoring.set_enable(enable = False) \n
		Defines the settings for the discontinuous reception in the downlink, see 'Continuous Packet Connectivity (CPC) '. \n
			:param enable: OFF | ON enables/disables UE monitoring of E-AGCH/E-RGCH when they overlap with the start of a UE DRX HS-SCCH reception
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:GMONitoring:ENABle {param}')

	def get_ithreshold(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:GMONitoring:ITHReshold \n
		Snippet: value: int = driver.configure.cell.cpc.ddrx.gmonitoring.get_ithreshold() \n
		Number of subframes after uplink activity when UE has to monitor E-AGCH/E-RGCH, see 'Continuous Packet Connectivity (CPC)
		'. \n
			:return: threshold: Only the following values are allowed (in E-DCH TTIs) : 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 256 E-DCH TTI
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:GMONitoring:ITHReshold?')
		return Conversions.str_to_int(response)

	def set_ithreshold(self, threshold: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:GMONitoring:ITHReshold \n
		Snippet: driver.configure.cell.cpc.ddrx.gmonitoring.set_ithreshold(threshold = 1) \n
		Number of subframes after uplink activity when UE has to monitor E-AGCH/E-RGCH, see 'Continuous Packet Connectivity (CPC)
		'. \n
			:param threshold: Only the following values are allowed (in E-DCH TTIs) : 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 256 E-DCH TTI
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:GMONitoring:ITHReshold {param}')
