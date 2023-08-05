from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eagch:
	"""Eagch commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eagch", core, parent)

	def get_tindex(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:EAGCh:TINDex \n
		Snippet: value: int = driver.configure.cell.hsupa.eagch.get_tindex() \n
		Specifies the mapping of the absolute grant value according to 3GPP TS 25.212. \n
			:return: index: 0: according to table 16B 1: according to table 16B.1, alternative mapping Range: 0 to 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:EAGCh:TINDex?')
		return Conversions.str_to_int(response)

	def set_tindex(self, index: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:EAGCh:TINDex \n
		Snippet: driver.configure.cell.hsupa.eagch.set_tindex(index = 1) \n
		Specifies the mapping of the absolute grant value according to 3GPP TS 25.212. \n
			:param index: 0: according to table 16B 1: according to table 16B.1, alternative mapping Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:EAGCh:TINDex {param}')

	# noinspection PyTypeChecker
	def get_utti(self) -> enums.UnscheduledTransType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:EAGCh:UTTI \n
		Snippet: value: enums.UnscheduledTransType = driver.configure.cell.hsupa.eagch.get_utti() \n
		Defines the transmission in unscheduled TTIs. \n
			:return: unscheduled_tti: DUMMy | DTX DUMMy: send absolute grants to dummy UE-IDs DTX: switch E-AGCH off
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:EAGCh:UTTI?')
		return Conversions.str_to_scalar_enum(response, enums.UnscheduledTransType)

	def set_utti(self, unscheduled_tti: enums.UnscheduledTransType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:EAGCh:UTTI \n
		Snippet: driver.configure.cell.hsupa.eagch.set_utti(unscheduled_tti = enums.UnscheduledTransType.DTX) \n
		Defines the transmission in unscheduled TTIs. \n
			:param unscheduled_tti: DUMMy | DTX DUMMy: send absolute grants to dummy UE-IDs DTX: switch E-AGCH off
		"""
		param = Conversions.enum_scalar_to_str(unscheduled_tti, enums.UnscheduledTransType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:EAGCh:UTTI {param}')
