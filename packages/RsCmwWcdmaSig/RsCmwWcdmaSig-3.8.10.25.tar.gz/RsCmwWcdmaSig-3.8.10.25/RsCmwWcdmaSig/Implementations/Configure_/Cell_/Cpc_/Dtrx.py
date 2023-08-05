from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtrx:
	"""Dtrx commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dtrx", core, parent)

	def get_delay(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DTRX:DELay \n
		Snippet: value: int = driver.configure.cell.cpc.dtrx.get_delay() \n
		Frame delay the UE waits until enabling a new timing pattern for DRX/DTX operation, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:return: enable_delay: Only the following values are allowed (in frames) : 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 If you enter another value, the nearest allowed value is set instead. Range: 0 frames to 128 frames
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DTRX:DELay?')
		return Conversions.str_to_int(response)

	def set_delay(self, enable_delay: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DTRX:DELay \n
		Snippet: driver.configure.cell.cpc.dtrx.set_delay(enable_delay = 1) \n
		Frame delay the UE waits until enabling a new timing pattern for DRX/DTX operation, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:param enable_delay: Only the following values are allowed (in frames) : 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 If you enter another value, the nearest allowed value is set instead. Range: 0 frames to 128 frames
		"""
		param = Conversions.decimal_value_to_str(enable_delay)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DTRX:DELay {param}')

	def get_offset(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DTRX:OFFSet \n
		Snippet: value: int = driver.configure.cell.cpc.dtrx.get_offset() \n
		Defines the settings for the discontinuous transmission and reception, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: offset: Subframe offset to spread the DPCCH transmissions from different UEs Range: 0 Subframe to 159 Subframe
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DTRX:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, offset: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:DTRX:OFFSet \n
		Snippet: driver.configure.cell.cpc.dtrx.set_offset(offset = 1) \n
		Defines the settings for the discontinuous transmission and reception, see 'Continuous Packet Connectivity (CPC) '. \n
			:param offset: Subframe offset to spread the DPCCH transmissions from different UEs Range: 0 Subframe to 159 Subframe
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:DTRX:OFFSet {param}')
