from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fading:
	"""Fading commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fading", core, parent)

	# noinspection PyTypeChecker
	class BlerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Median_0: float: Limit for the values acquired at median CQI Range: 0 % to 100 %, Unit: %
			- Median_P_3: float: Limit for the values acquired at median CQI + 3 Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_float('Median_0'),
			ArgStruct.scalar_float('Median_P_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Median_0: float = None
			self.Median_P_3: float = None

	def get_bler(self) -> BlerStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:FADing:BLER \n
		Snippet: value: BlerStruct = driver.configure.hcqi.limit.fading.get_bler() \n
		Defines upper BLER limit for fading test case. \n
			:return: structure: for return value, see the help for BlerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:FADing:BLER?', self.__class__.BlerStruct())

	def set_bler(self, value: BlerStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:FADing:BLER \n
		Snippet: driver.configure.hcqi.limit.fading.set_bler(value = BlerStruct()) \n
		Defines upper BLER limit for fading test case. \n
			:param value: see the help for BlerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:FADing:BLER', value)

	# noinspection PyTypeChecker
	class DtxStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Median_0: float or bool: Limit for the values acquired at median CQI Range: 0 % to 100 % Additional parameters: OFF | ON (disables | enables the limit check)
			- Median_P_3: float or bool: Limit for the values acquired at median CQI + 3 Range: 0 % to 100 % Additional parameters: OFF | ON (disables | enables the limit check)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Median_0'),
			ArgStruct.scalar_float_ext('Median_P_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Median_0: float or bool = None
			self.Median_P_3: float or bool = None

	def get_dtx(self) -> DtxStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:FADing:DTX \n
		Snippet: value: DtxStruct = driver.configure.hcqi.limit.fading.get_dtx() \n
		Defines the maximum percentage of HSDPA subframes that the UE answers with DTX during fading test case. \n
			:return: structure: for return value, see the help for DtxStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:FADing:DTX?', self.__class__.DtxStruct())

	def set_dtx(self, value: DtxStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:FADing:DTX \n
		Snippet: driver.configure.hcqi.limit.fading.set_dtx(value = DtxStruct()) \n
		Defines the maximum percentage of HSDPA subframes that the UE answers with DTX during fading test case. \n
			:param value: see the help for DtxStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:FADing:DTX', value)
