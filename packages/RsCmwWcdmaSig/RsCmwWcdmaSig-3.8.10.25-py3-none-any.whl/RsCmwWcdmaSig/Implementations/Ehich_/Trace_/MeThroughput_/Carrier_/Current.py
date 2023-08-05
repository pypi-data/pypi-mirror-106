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

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:EHICh:TRACe:METHroughput:CARRier<carrier>:CURRent \n
		Snippet: value: List[float] = driver.ehich.trace.meThroughput.carrier.current.read() \n
		Return the results of the E-HICH traces per carrier. Maximum expected throughput reachable if the UE sends at the maximum
		data rate (depends on the current settings) and no CRC errors occur. The number of results depends on the configured
		number of subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Ehich.mframes.
		One measurement result is returned per 100 subframes for 2 ms TTI and per 20 frames for 10 ms TTI. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: current: N throughput values, from first to last (most recent) measured subframe Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:EHICh:TRACe:METHroughput:CARRier<Carrier>:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:EHICh:TRACe:METHroughput:CARRier<carrier>:CURRent \n
		Snippet: value: List[float] = driver.ehich.trace.meThroughput.carrier.current.fetch() \n
		Return the results of the E-HICH traces per carrier. Maximum expected throughput reachable if the UE sends at the maximum
		data rate (depends on the current settings) and no CRC errors occur. The number of results depends on the configured
		number of subframes to be measured per measurement cycle, see method RsCmwWcdmaSig.Configure.Ehich.mframes.
		One measurement result is returned per 100 subframes for 2 ms TTI and per 20 frames for 10 ms TTI. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: current: N throughput values, from first to last (most recent) measured subframe Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:EHICh:TRACe:METHroughput:CARRier<Carrier>:CURRent?', suppressed)
		return response
