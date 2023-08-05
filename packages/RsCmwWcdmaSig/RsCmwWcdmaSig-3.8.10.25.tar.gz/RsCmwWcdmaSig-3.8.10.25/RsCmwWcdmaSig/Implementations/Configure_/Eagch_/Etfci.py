from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etfci:
	"""Etfci commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etfci", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:ETFCi:MODE \n
		Snippet: value: enums.AutoManualMode = driver.configure.eagch.etfci.get_mode() \n
		Specifies the mode of expected E-TFCI selection. \n
			:return: mode: AUTO | MANual Automatic according to AG pattern or manual
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:ETFCi:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_mode(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:ETFCi:MODE \n
		Snippet: driver.configure.eagch.etfci.set_mode(mode = enums.AutoManualMode.AUTO) \n
		Specifies the mode of expected E-TFCI selection. \n
			:param mode: AUTO | MANual Automatic according to AG pattern or manual
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:ETFCi:MODE {param}')

	def get_manual(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:ETFCi:MANual \n
		Snippet: value: List[int] = driver.configure.eagch.etfci.get_manual() \n
		Specifies up to eight E-TFCI values used for E-AGCH measurement in manual mode. \n
			:return: etfci: Range: 0 to 127
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:ETFCi:MANual?')
		return response

	def set_manual(self, etfci: List[int]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:ETFCi:MANual \n
		Snippet: driver.configure.eagch.etfci.set_manual(etfci = [1, 2, 3]) \n
		Specifies up to eight E-TFCI values used for E-AGCH measurement in manual mode. \n
			:param etfci: Range: 0 to 127
		"""
		param = Conversions.list_to_csv_str(etfci)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:ETFCi:MANual {param}')

	def get_auto(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:ETFCi:AUTO \n
		Snippet: value: List[int] = driver.configure.eagch.etfci.get_auto() \n
		Queries the n E-TFCI values calculated according to the absolute grant (AG) configuration. The number of values n equals
		AG pattern length, see method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length \n
			:return: etfci: Range: 0 to 127
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:ETFCi:AUTO?')
		return response
