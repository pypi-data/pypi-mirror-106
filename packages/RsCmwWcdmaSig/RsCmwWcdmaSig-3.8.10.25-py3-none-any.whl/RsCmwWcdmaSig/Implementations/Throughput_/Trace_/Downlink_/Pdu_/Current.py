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
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:THRoughput:TRACe:DL:PDU:CURRent \n
		Snippet: value: List[float] = driver.throughput.trace.downlink.pdu.current.fetch() \n
		Return the values of the downlink PDU and SDU throughput traces. The results of the current and average traces can be
		retrieved. The number of trace values N depends on the configured <update interval> and <window size>: N = integer
		(<window size> / <update interval>) \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: downlink_pdu: Comma-separated list of N throughput trace values Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:THRoughput:TRACe:DL:PDU:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:THRoughput:TRACe:DL:PDU:CURRent \n
		Snippet: value: List[float] = driver.throughput.trace.downlink.pdu.current.read() \n
		Return the values of the downlink PDU and SDU throughput traces. The results of the current and average traces can be
		retrieved. The number of trace values N depends on the configured <update interval> and <window size>: N = integer
		(<window size> / <update interval>) \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: downlink_pdu: Comma-separated list of N throughput trace values Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:THRoughput:TRACe:DL:PDU:CURRent?', suppressed)
		return response
