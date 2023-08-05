from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cycle:
	"""Cycle commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cycle", core, parent)

	def get_apattern(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:CYCLe:APATtern \n
		Snippet: value: int = driver.configure.cell.cpc.ddrx.cycle.get_apattern() \n
		Reception pattern, to inform UE how often to monitor HS-SCCH, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: pattern: Only the following values are allowed (in subframes) : 4 | 5 | 8 | 10 | 16 | 20 If you enter another value, the nearest allowed value is set instead. Range: 4 Subframe to 20 Subframe
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:CYCLe:APATtern?')
		return Conversions.str_to_int(response)

	def set_apattern(self, pattern: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:CYCLe:APATtern \n
		Snippet: driver.configure.cell.cpc.ddrx.cycle.set_apattern(pattern = 1) \n
		Reception pattern, to inform UE how often to monitor HS-SCCH, see 'Continuous Packet Connectivity (CPC) '. \n
			:param pattern: Only the following values are allowed (in subframes) : 4 | 5 | 8 | 10 | 16 | 20 If you enter another value, the nearest allowed value is set instead. Range: 4 Subframe to 20 Subframe
		"""
		param = Conversions.decimal_value_to_str(pattern)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:CYCLe:APATtern {param}')

	def get_ithreshold(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:CYCLe:ITHReshold \n
		Snippet: value: int = driver.configure.cell.cpc.ddrx.cycle.get_ithreshold() \n
		Number of subframes after downlink activity where UE has to continuously monitor HS-SCCH, see 'Continuous Packet
		Connectivity (CPC) '. \n
			:return: threshold: Only the following values are allowed (in subframes) : 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 If you enter another value, the nearest allowed value is set instead. Range: 0 Subframe to 512 Subframe
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:CYCLe:ITHReshold?')
		return Conversions.str_to_int(response)

	def set_ithreshold(self, threshold: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DDRX:CYCLe:ITHReshold \n
		Snippet: driver.configure.cell.cpc.ddrx.cycle.set_ithreshold(threshold = 1) \n
		Number of subframes after downlink activity where UE has to continuously monitor HS-SCCH, see 'Continuous Packet
		Connectivity (CPC) '. \n
			:param threshold: Only the following values are allowed (in subframes) : 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 If you enter another value, the nearest allowed value is set instead. Range: 0 Subframe to 512 Subframe
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DDRX:CYCLe:ITHReshold {param}')
