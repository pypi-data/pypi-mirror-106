from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fixed:
	"""Fixed commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fixed", core, parent)

	# noinspection PyTypeChecker
	def get_hset(self) -> enums.HsetFixed:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:FIXed:HSET \n
		Snippet: value: enums.HsetFixed = driver.configure.cell.hsdpa.fixed.get_hset() \n
		Selects an H-Set for the fixed reference channel. \n
			:return: hset: H1M1 | H1M2 | H2M1 | H2M2 | H3M1 | H3M2 | H4M1 | H5M1 | H6M1 | H6M2 | H8M3 | H8MT | H1MI | H8MI | H3A1 | H3A2 | H8A3 | H8AI | HAM1 | HAM2 | HAA1 | HAA2 | HCM1 | HCMT | H6A1 | H6A2 | H1AI | H1BI | H3B1 | H3B2 | H6B1 | H6B2 | H8B3 | H8BI | HAB1 | HAB2 Single carrier H-Sets: H1M1 to H6M1, HAM1: H-Set 1 to 6, 10 (QPSK) H1M2 to H3M2, H6M2, HAM2: H-Set 1 to 3, 6, 10 (16-QAM) H8M3: H-Set 8 (64-QAM) H1MI, H8MI: H-Set 1, 8 (maximum input) H8MT: H-Set 8 (maximum throughput) Dual carrier H-Sets: H1AI: H-Set 1A (maximum input) H3A1, H6A1, HAA1, HCM1: H-Set 3A, 6A, 10A, 12 (QPSK) H3A2, H6A2, HAA2: H-Set 3A, 6A, 10A (16-QAM) H8A3: H-Set 8A (64-QAM) H8AI: H-Set 8A (maximum input) HCMT: H-Set 12 (maximum throughput) 3C-HSDPA H-Sets: H1BI: H-Set 1B (maximum input) H3B1, H6B1, HAB1: H-Set 3B, 6B, 10B (QPSK) H3B2, H6B2, HAB2: H-Set 3B, 6B, 10B (16-QAM) H8B3: H-Set 8B (64-QAM) H8BI: H-Set 8B (maximum input)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:FIXed:HSET?')
		return Conversions.str_to_scalar_enum(response, enums.HsetFixed)

	def set_hset(self, hset: enums.HsetFixed) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:FIXed:HSET \n
		Snippet: driver.configure.cell.hsdpa.fixed.set_hset(hset = enums.HsetFixed.H1AI) \n
		Selects an H-Set for the fixed reference channel. \n
			:param hset: H1M1 | H1M2 | H2M1 | H2M2 | H3M1 | H3M2 | H4M1 | H5M1 | H6M1 | H6M2 | H8M3 | H8MT | H1MI | H8MI | H3A1 | H3A2 | H8A3 | H8AI | HAM1 | HAM2 | HAA1 | HAA2 | HCM1 | HCMT | H6A1 | H6A2 | H1AI | H1BI | H3B1 | H3B2 | H6B1 | H6B2 | H8B3 | H8BI | HAB1 | HAB2 Single carrier H-Sets: H1M1 to H6M1, HAM1: H-Set 1 to 6, 10 (QPSK) H1M2 to H3M2, H6M2, HAM2: H-Set 1 to 3, 6, 10 (16-QAM) H8M3: H-Set 8 (64-QAM) H1MI, H8MI: H-Set 1, 8 (maximum input) H8MT: H-Set 8 (maximum throughput) Dual carrier H-Sets: H1AI: H-Set 1A (maximum input) H3A1, H6A1, HAA1, HCM1: H-Set 3A, 6A, 10A, 12 (QPSK) H3A2, H6A2, HAA2: H-Set 3A, 6A, 10A (16-QAM) H8A3: H-Set 8A (64-QAM) H8AI: H-Set 8A (maximum input) HCMT: H-Set 12 (maximum throughput) 3C-HSDPA H-Sets: H1BI: H-Set 1B (maximum input) H3B1, H6B1, HAB1: H-Set 3B, 6B, 10B (QPSK) H3B2, H6B2, HAB2: H-Set 3B, 6B, 10B (16-QAM) H8B3: H-Set 8B (64-QAM) H8BI: H-Set 8B (maximum input)
		"""
		param = Conversions.enum_scalar_to_str(hset, enums.HsetFixed)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:FIXed:HSET {param}')
