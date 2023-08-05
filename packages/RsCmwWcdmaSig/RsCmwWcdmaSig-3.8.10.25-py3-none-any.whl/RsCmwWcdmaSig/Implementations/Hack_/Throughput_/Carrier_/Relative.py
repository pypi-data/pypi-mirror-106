from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("relative", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Rel_Current: float: Range: 0 % to 100 %, Unit: %
			- Rel_Maximum: float: Range: 0 % to 100 %, Unit: %
			- Rel_Minimum: float: Range: 0 % to 100 %, Unit: %
			- Rel_Scheduled: float: Range: 0 % to 100 %, Unit: %
			- Rel_Average: float: Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Rel_Current'),
			ArgStruct.scalar_float('Rel_Maximum'),
			ArgStruct.scalar_float('Rel_Minimum'),
			ArgStruct.scalar_float('Rel_Scheduled'),
			ArgStruct.scalar_float('Rel_Average')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rel_Current: float = None
			self.Rel_Maximum: float = None
			self.Rel_Minimum: float = None
			self.Rel_Scheduled: float = None
			self.Rel_Average: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:THRoughput:CARRier<carrier>:RELative \n
		Snippet: value: ResultData = driver.hack.throughput.carrier.relative.fetch() \n
		Return the throughput results as percentage of the 'Max. possible Throughput'. The current, maximum, minimum, scheduled
		and average values are returned, see 'Throughput'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:THRoughput:CARRier<Carrier>:RELative?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:THRoughput:CARRier<carrier>:RELative \n
		Snippet: value: ResultData = driver.hack.throughput.carrier.relative.read() \n
		Return the throughput results as percentage of the 'Max. possible Throughput'. The current, maximum, minimum, scheduled
		and average values are returned, see 'Throughput'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:HACK:THRoughput:CARRier<Carrier>:RELative?', self.__class__.ResultData())
