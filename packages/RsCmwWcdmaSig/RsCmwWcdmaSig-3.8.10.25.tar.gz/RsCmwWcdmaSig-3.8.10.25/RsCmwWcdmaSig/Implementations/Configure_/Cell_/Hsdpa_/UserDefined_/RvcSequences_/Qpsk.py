from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qpsk:
	"""Qpsk commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qpsk", core, parent)

	# noinspection PyTypeChecker
	class UserDefinedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Length: int: The first Length entries of the user defined coding sequence are used. Range: 1 to 8
			- Sequence: List[int]: Up to 8 values separated by commas. If you specify n values, they overwrite the first n entries of the user-defined sequence. Range: 0 to 7"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct('Sequence', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Sequence: List[int] = None

	def get_user_defined(self) -> UserDefinedStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK:UDEFined \n
		Snippet: value: UserDefinedStruct = driver.configure.cell.hsdpa.userDefined.rvcSequences.qpsk.get_user_defined() \n
		Specifies an RV coding sequence to be used for signals with QPSK modulation if UDEFined is set via method RsCmwWcdmaSig.
		Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qpsk.value. \n
			:return: structure: for return value, see the help for UserDefinedStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK:UDEFined?', self.__class__.UserDefinedStruct())

	def set_user_defined(self, value: UserDefinedStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK:UDEFined \n
		Snippet: driver.configure.cell.hsdpa.userDefined.rvcSequences.qpsk.set_user_defined(value = UserDefinedStruct()) \n
		Specifies an RV coding sequence to be used for signals with QPSK modulation if UDEFined is set via method RsCmwWcdmaSig.
		Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qpsk.value. \n
			:param value: see the help for UserDefinedStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK:UDEFined', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.RvcSequence:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK \n
		Snippet: value: enums.RvcSequence = driver.configure.cell.hsdpa.userDefined.rvcSequences.qpsk.get_value() \n
		Specifies an RV coding sequence to be used for signals with QPSK modulation. If UDEFined is selected, the sequence is
		defined via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qpsk.userDefined. \n
			:return: sequence: S1 | S2 | S3 | S4 | S5 | S6 | S7 | UDEFined S1: {0} S2: {6} S3: {0, 2, 5, 6} S4: {6, 2, 1, 5} S5: {0, 0, 0, 0} S6: {6, 6, 6, 6} S7: {6, 0, 4, 5} UDEFined: user-defined sequence
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK?')
		return Conversions.str_to_scalar_enum(response, enums.RvcSequence)

	def set_value(self, sequence: enums.RvcSequence) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK \n
		Snippet: driver.configure.cell.hsdpa.userDefined.rvcSequences.qpsk.set_value(sequence = enums.RvcSequence.S1) \n
		Specifies an RV coding sequence to be used for signals with QPSK modulation. If UDEFined is selected, the sequence is
		defined via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qpsk.userDefined. \n
			:param sequence: S1 | S2 | S3 | S4 | S5 | S6 | S7 | UDEFined S1: {0} S2: {6} S3: {0, 2, 5, 6} S4: {6, 2, 1, 5} S5: {0, 0, 0, 0} S6: {6, 6, 6, 6} S7: {6, 0, 4, 5} UDEFined: user-defined sequence
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.RvcSequence)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QPSK {param}')
