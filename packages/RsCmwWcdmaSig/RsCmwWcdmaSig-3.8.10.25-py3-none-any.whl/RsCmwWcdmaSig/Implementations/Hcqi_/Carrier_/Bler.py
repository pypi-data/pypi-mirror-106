from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Median_Cqim_1: float: Block error rate measured at median CQI - 1 in the third stage of measurement (AWGN test case only) Range: 0 % to 100 %, Unit: %
			- Median_Cqi: float: Block error rate measured at median CQI in the second stage of measurement (AWGN and fading test cases) Range: 0 % to 100 %, Unit: %
			- Median_Cqip_2: float: Block error rate measured at median CQI + 2 in the third stage of measurement (AWGN test case only) Range: 0 % to 100 %, Unit: %
			- Median_Cqip_3: float: Block error rate measured at median CQI + 3 in the second stage of measurement (Fading test case only) Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Median_Cqim_1'),
			ArgStruct.scalar_float('Median_Cqi'),
			ArgStruct.scalar_float('Median_Cqip_2'),
			ArgStruct.scalar_float('Median_Cqip_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Median_Cqim_1: float = None
			self.Median_Cqi: float = None
			self.Median_Cqip_2: float = None
			self.Median_Cqip_3: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HCQI:CARRier<carrier>:BLER \n
		Snippet: value: ResultData = driver.hcqi.carrier.bler.fetch() \n
		Returns the BLER results of the second and third stage of HSDPA CQI measurement. As indicated in the parameter
		descriptions below, each test case provides valid results for a subset of the parameters only. For the other parameters
		NCAP is returned. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:HCQI:CARRier<Carrier>:BLER?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HCQI:CARRier<carrier>:BLER \n
		Snippet: value: ResultData = driver.hcqi.carrier.bler.read() \n
		Returns the BLER results of the second and third stage of HSDPA CQI measurement. As indicated in the parameter
		descriptions below, each test case provides valid results for a subset of the parameters only. For the other parameters
		NCAP is returned. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:HCQI:CARRier<Carrier>:BLER?', self.__class__.ResultData())
