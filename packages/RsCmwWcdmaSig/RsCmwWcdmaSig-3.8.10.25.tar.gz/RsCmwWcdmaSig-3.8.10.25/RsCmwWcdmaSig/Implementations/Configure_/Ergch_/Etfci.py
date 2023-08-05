from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etfci:
	"""Etfci commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etfci", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:MODE \n
		Snippet: value: enums.AutoManualMode = driver.configure.ergch.etfci.get_mode() \n
		Specifies the mode of expected E-TFCI selection. \n
			:return: mode: AUTO | MANual Automatic according to AG pattern or manual
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_mode(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:MODE \n
		Snippet: driver.configure.ergch.etfci.set_mode(mode = enums.AutoManualMode.AUTO) \n
		Specifies the mode of expected E-TFCI selection. \n
			:param mode: AUTO | MANual Automatic according to AG pattern or manual
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:MODE {param}')

	def get_expected(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:EXPected \n
		Snippet: value: int = driver.configure.ergch.etfci.get_expected() \n
		Specifies the number of valid E-TFCI values in the expected E-TFCI table, see also method RsCmwWcdmaSig.Configure.Ergch.
		Etfci.manual method RsCmwWcdmaSig.Configure.Ergch.Etfci.auto \n
			:return: no_expected: Range: 3 to 11
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:EXPected?')
		return Conversions.str_to_int(response)

	def set_expected(self, no_expected: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:EXPected \n
		Snippet: driver.configure.ergch.etfci.set_expected(no_expected = 1) \n
		Specifies the number of valid E-TFCI values in the expected E-TFCI table, see also method RsCmwWcdmaSig.Configure.Ergch.
		Etfci.manual method RsCmwWcdmaSig.Configure.Ergch.Etfci.auto \n
			:param no_expected: Range: 3 to 11
		"""
		param = Conversions.decimal_value_to_str(no_expected)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:EXPected {param}')

	def get_initial(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:INITial \n
		Snippet: value: int = driver.configure.ergch.etfci.get_initial() \n
		Position of the initial operating point in the expected E-TFCI table. If the operating point of the UE is shifted outside
		the E-TFCI range, the initial operating point is readjusted. See also: method RsCmwWcdmaSig.Configure.Ergch.Etfci.manual
		and method RsCmwWcdmaSig.Configure.Ergch.Etfci.auto \n
			:return: index: Range: 2 to (No. of expected ETFCI) - 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:INITial?')
		return Conversions.str_to_int(response)

	def set_initial(self, index: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:INITial \n
		Snippet: driver.configure.ergch.etfci.set_initial(index = 1) \n
		Position of the initial operating point in the expected E-TFCI table. If the operating point of the UE is shifted outside
		the E-TFCI range, the initial operating point is readjusted. See also: method RsCmwWcdmaSig.Configure.Ergch.Etfci.manual
		and method RsCmwWcdmaSig.Configure.Ergch.Etfci.auto \n
			:param index: Range: 2 to (No. of expected ETFCI) - 1
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:INITial {param}')

	def get_manual(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:MANual \n
		Snippet: value: List[int] = driver.configure.ergch.etfci.get_manual() \n
		Specifies the n E-TFCI values set manually. Number of values n is set by method RsCmwWcdmaSig.Configure.Ergch.Etfci.
		expected \n
			:return: etfci: Range: 0 to 127
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:MANual?')
		return response

	def set_manual(self, etfci: List[int]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:MANual \n
		Snippet: driver.configure.ergch.etfci.set_manual(etfci = [1, 2, 3]) \n
		Specifies the n E-TFCI values set manually. Number of values n is set by method RsCmwWcdmaSig.Configure.Ergch.Etfci.
		expected \n
			:param etfci: Range: 0 to 127
		"""
		param = Conversions.list_to_csv_str(etfci)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:MANual {param}')

	def get_auto(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:ETFCi:AUTO \n
		Snippet: value: List[int] = driver.configure.ergch.etfci.get_auto() \n
		Queries the n calculated E-TFCI values according to the AG configuration. Number of values n is set by method
		RsCmwWcdmaSig.Configure.Ergch.Etfci.expected \n
			:return: etfci: Range: 0 to 127
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:ETFCi:AUTO?')
		return response
