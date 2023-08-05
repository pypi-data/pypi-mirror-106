from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("awgn", core, parent)

	# noinspection PyTypeChecker
	class BlerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Median_M_1: float: Upper limit for the values acquired at median CQI - 1. This limit applies if BLER at median CQI is above the limit Median0. Range: 0 % to 100 %, Unit: %
			- Median_0: float: Limit for the values acquired at median CQI Range: 0 % to 100 %, Unit: %
			- Median_P_2: float: Lower limit for the values acquired at median CQI + 2. This limit applies if BLER at median CQI is below the limit Median0. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_float('Median_M_1'),
			ArgStruct.scalar_float('Median_0'),
			ArgStruct.scalar_float('Median_P_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Median_M_1: float = None
			self.Median_0: float = None
			self.Median_P_2: float = None

	def get_bler(self) -> BlerStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN:BLER \n
		Snippet: value: BlerStruct = driver.configure.hcqi.limit.awgn.get_bler() \n
		Defines BLER limit for AWGN test case. \n
			:return: structure: for return value, see the help for BlerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN:BLER?', self.__class__.BlerStruct())

	def set_bler(self, value: BlerStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN:BLER \n
		Snippet: driver.configure.hcqi.limit.awgn.set_bler(value = BlerStruct()) \n
		Defines BLER limit for AWGN test case. \n
			:param value: see the help for BlerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN:BLER', value)

	# noinspection PyTypeChecker
	class DtxStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Median_M_1: float or bool: Limit for the values acquired at median CQI - 1 Range: 0 % to 100 % Additional OFF | ON disables | enables the limit check
			- Median_0: float or bool: Limit for the values acquired at median CQI Range: 0 % to 100 % Additional OFF | ON disables | enables the limit check
			- Median_P_2: float or bool: Limit for the values acquired at median CQI + 2 Range: 0 % to 100 % Additional OFF | ON disables | enables the limit check"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Median_M_1'),
			ArgStruct.scalar_float_ext('Median_0'),
			ArgStruct.scalar_float_ext('Median_P_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Median_M_1: float or bool = None
			self.Median_0: float or bool = None
			self.Median_P_2: float or bool = None

	def get_dtx(self) -> DtxStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN:DTX \n
		Snippet: value: DtxStruct = driver.configure.hcqi.limit.awgn.get_dtx() \n
		Defines the maximum percentage of HSDPA subframes that the UE answers with DTX during AWGN test case. \n
			:return: structure: for return value, see the help for DtxStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN:DTX?', self.__class__.DtxStruct())

	def set_dtx(self, value: DtxStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN:DTX \n
		Snippet: driver.configure.hcqi.limit.awgn.set_dtx(value = DtxStruct()) \n
		Defines the maximum percentage of HSDPA subframes that the UE answers with DTX during AWGN test case. \n
			:param value: see the help for DtxStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN:DTX', value)

	def get_value(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN \n
		Snippet: value: float = driver.configure.hcqi.limit.awgn.get_value() \n
		Specifies the minimum percentage of measured CQI values, that fall in the range (median CQI – 2) ≦ median CQI ≦ (median
		CQI + 2) . \n
			:return: cqiin_range: Lower limit for the first stage of AWGN test case Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN?')
		return Conversions.str_to_float(response)

	def set_value(self, cqiin_range: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:LIMit:AWGN \n
		Snippet: driver.configure.hcqi.limit.awgn.set_value(cqiin_range = 1.0) \n
		Specifies the minimum percentage of measured CQI values, that fall in the range (median CQI – 2) ≦ median CQI ≦ (median
		CQI + 2) . \n
			:param cqiin_range: Lower limit for the first stage of AWGN test case Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(cqiin_range)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HCQI:LIMit:AWGN {param}')
