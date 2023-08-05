from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mnc:
	"""Mnc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mnc", core, parent)

	# noinspection PyTypeChecker
	def get_digits(self) -> enums.NrOfDigits:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MNC:DIGits \n
		Snippet: value: enums.NrOfDigits = driver.configure.cell.mnc.get_digits() \n
		Specifies the size of mobile network code (MNC) . A two or three-digit MNC can be selected. \n
			:return: no_digits: D2 | D3 D2: two-digit MNC D3: three-digit MNC
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:MNC:DIGits?')
		return Conversions.str_to_scalar_enum(response, enums.NrOfDigits)

	def set_digits(self, no_digits: enums.NrOfDigits) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MNC:DIGits \n
		Snippet: driver.configure.cell.mnc.set_digits(no_digits = enums.NrOfDigits.D2) \n
		Specifies the size of mobile network code (MNC) . A two or three-digit MNC can be selected. \n
			:param no_digits: D2 | D3 D2: two-digit MNC D3: three-digit MNC
		"""
		param = Conversions.enum_scalar_to_str(no_digits, enums.NrOfDigits)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:MNC:DIGits {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value: int: Range: 0 to 99 or 999 depending on NrOfDigits
			- Nr_Of_Digits: enums.NrOfDigits: D2 | D3 D2: two-digit MNC D3: three-digit MNC"""
		__meta_args_list = [
			ArgStruct.scalar_int('Value'),
			ArgStruct.scalar_enum('Nr_Of_Digits', enums.NrOfDigits)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: int = None
			self.Nr_Of_Digits: enums.NrOfDigits = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MNC \n
		Snippet: value: ValueStruct = driver.configure.cell.mnc.get_value() \n
		Specifies the mobile network code (MNC) . A two or three-digit MNC can be set. Leading zeros can be omitted. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:MNC?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MNC \n
		Snippet: driver.configure.cell.mnc.set_value(value = ValueStruct()) \n
		Specifies the mobile network code (MNC) . A two or three-digit MNC can be set. Leading zeros can be omitted. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:MNC', value)
