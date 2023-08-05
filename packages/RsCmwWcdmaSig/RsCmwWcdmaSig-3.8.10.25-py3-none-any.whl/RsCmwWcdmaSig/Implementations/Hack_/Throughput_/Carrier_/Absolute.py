from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Abs_Current: float: Current throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Maximum: float: Maximum throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Minimum: float: Minimum throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Scheduled: float: Scheduled throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Max_Possible: float: Maximum possible throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Total_Current: float: Current throughput - sum of all carriers Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Total_Max_Pos: float: Maximum possible throughput - sum of all carriers Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Total_Average: float: Average throughput calculated from a sum of all carriers Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Abs_Average: float: Average throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Abs_Current'),
			ArgStruct.scalar_float('Abs_Maximum'),
			ArgStruct.scalar_float('Abs_Minimum'),
			ArgStruct.scalar_float('Abs_Scheduled'),
			ArgStruct.scalar_float('Max_Possible'),
			ArgStruct.scalar_float('Abs_Total_Current'),
			ArgStruct.scalar_float('Total_Max_Pos'),
			ArgStruct.scalar_float('Abs_Total_Average'),
			ArgStruct.scalar_float('Abs_Average')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Abs_Current: float = None
			self.Abs_Maximum: float = None
			self.Abs_Minimum: float = None
			self.Abs_Scheduled: float = None
			self.Max_Possible: float = None
			self.Abs_Total_Current: float = None
			self.Total_Max_Pos: float = None
			self.Abs_Total_Average: float = None
			self.Abs_Average: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:THRoughput:CARRier<carrier>:ABSolute \n
		Snippet: value: ResultData = driver.hack.throughput.carrier.absolute.fetch() \n
		Return the throughput results as absolute values. The current, maximum, minimum, scheduled and average values are
		returned, see 'Throughput'. In addition to the measured values, the theoretical maximum possible throughput is returned,
		see 'Max. possible Throughput'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:THRoughput:CARRier<Carrier>:ABSolute?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:THRoughput:CARRier<carrier>:ABSolute \n
		Snippet: value: ResultData = driver.hack.throughput.carrier.absolute.read() \n
		Return the throughput results as absolute values. The current, maximum, minimum, scheduled and average values are
		returned, see 'Throughput'. In addition to the measured values, the theoretical maximum possible throughput is returned,
		see 'Max. possible Throughput'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:HACK:THRoughput:CARRier<Carrier>:ABSolute?', self.__class__.ResultData())
