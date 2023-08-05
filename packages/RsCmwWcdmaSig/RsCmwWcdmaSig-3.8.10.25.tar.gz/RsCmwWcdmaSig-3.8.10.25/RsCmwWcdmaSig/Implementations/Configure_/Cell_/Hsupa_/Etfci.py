from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etfci:
	"""Etfci commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etfci", core, parent)

	def get_tindex(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:ETFCi:TINDex \n
		Snippet: value: int = driver.configure.cell.hsupa.etfci.get_tindex() \n
		Specifies the E-TFCI table index signaled to the UE (use table 0 or table 1 defined in annex B of 3GPP TS 25.321) . \n
			:return: index: 0 | 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:ETFCi:TINDex?')
		return Conversions.str_to_int(response)

	def set_tindex(self, index: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:ETFCi:TINDex \n
		Snippet: driver.configure.cell.hsupa.etfci.set_tindex(index = 1) \n
		Specifies the E-TFCI table index signaled to the UE (use table 0 or table 1 defined in annex B of 3GPP TS 25.321) . \n
			:param index: 0 | 1
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:ETFCi:TINDex {param}')
