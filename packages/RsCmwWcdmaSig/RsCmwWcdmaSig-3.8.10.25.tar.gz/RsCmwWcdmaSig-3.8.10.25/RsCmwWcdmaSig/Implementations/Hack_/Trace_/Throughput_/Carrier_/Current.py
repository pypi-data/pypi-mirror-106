from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:TRACe:THRoughput:CARRier<carrier>:CURRent \n
		Snippet: value: List[float] = driver.hack.trace.throughput.carrier.current.fetch() \n
		Returns the current throughput trace results per carrier. The number of results depends on the configured number of
		subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Hack.msFrames. For each 100 subframes,
		one result is returned. The results of the average and current traces can be retrieved. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: current: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:TRACe:THRoughput:CARRier<Carrier>:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:TRACe:THRoughput:CARRier<carrier>:CURRent \n
		Snippet: value: List[float] = driver.hack.trace.throughput.carrier.current.read() \n
		Returns the current throughput trace results per carrier. The number of results depends on the configured number of
		subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Hack.msFrames. For each 100 subframes,
		one result is returned. The results of the average and current traces can be retrieved. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: current: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:HACK:TRACe:THRoughput:CARRier<Carrier>:CURRent?', suppressed)
		return response
