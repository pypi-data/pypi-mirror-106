from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Total:
	"""Total commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("total", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Current: float: N throughput values, from first to last (most recent) measured subframe
			- Average: float: Average of all 'Current' values referenced to the last statistics cycle"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Current'),
			ArgStruct.scalar_float('Average')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Current: float = None
			self.Average: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:EHICh:THRoughput:TOTal \n
		Snippet: value: ResultData = driver.ehich.throughput.total.read() \n
		Return the results of the E-HICH traces over all carriers. The number of results N depends on the configured number of
		subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Ehich.mframes. One measurement result
		is returned per 100 subframes for 2 ms TTI and per 20 frames for 10 ms TTI. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:EHICh:THRoughput:TOTal?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:EHICh:THRoughput:TOTal \n
		Snippet: value: ResultData = driver.ehich.throughput.total.fetch() \n
		Return the results of the E-HICH traces over all carriers. The number of results N depends on the configured number of
		subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Ehich.mframes. One measurement result
		is returned per 100 subframes for 2 ms TTI and per 20 frames for 10 ms TTI. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:EHICh:THRoughput:TOTal?', self.__class__.ResultData())
