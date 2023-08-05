from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harq:
	"""Harq commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("harq", core, parent)

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HARQ:POFFset \n
		Snippet: value: float = driver.configure.cell.hsupa.harq.get_poffset() \n
		Specifies the HARQ profile parameter 'E-DCH MAC-d flow power offset' signaled to the UE. \n
			:return: power_offset: Range: 0 dB to 6 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HARQ:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, power_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HARQ:POFFset \n
		Snippet: driver.configure.cell.hsupa.harq.set_poffset(power_offset = 1.0) \n
		Specifies the HARQ profile parameter 'E-DCH MAC-d flow power offset' signaled to the UE. \n
			:param power_offset: Range: 0 dB to 6 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(power_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HARQ:POFFset {param}')

	def get_re_tx(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HARQ:RETX \n
		Snippet: value: int = driver.configure.cell.hsupa.harq.get_re_tx() \n
		Specifies the HARQ profile parameter 'E-DCH MAC-d flow maximum number of retransmissions' signaled to the UE. \n
			:return: number: Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HARQ:RETX?')
		return Conversions.str_to_int(response)

	def set_re_tx(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HARQ:RETX \n
		Snippet: driver.configure.cell.hsupa.harq.set_re_tx(number = 1) \n
		Specifies the HARQ profile parameter 'E-DCH MAC-d flow maximum number of retransmissions' signaled to the UE. \n
			:param number: Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HARQ:RETX {param}')
