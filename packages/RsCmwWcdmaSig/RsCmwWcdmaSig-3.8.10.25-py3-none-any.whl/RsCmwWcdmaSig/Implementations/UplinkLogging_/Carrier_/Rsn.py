from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsn:
	"""Rsn commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rsn", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.RetransmisionSeqNr]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:RSN \n
		Snippet: value: List[enums.RetransmisionSeqNr] = driver.uplinkLogging.carrier.rsn.fetch() \n
		Return results of the UL logging measurement on the E-DPCCH. The results are returned per measured subframe:
		<Reliability>, <RSN>subframe1, <RSN>subframe2, ..., <RSN>subframe n The number of subframes n is configured via method
		RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: rsn: DTX | 0 | 1 | 2 | 3 Retransmission sequence number: DTX: no answer received from the UE 0: new transmission 1: first retransmission 2: second retransmission 3: higher than second retransmission"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:RSN?', suppressed)
		return Conversions.str_to_list_enum(response, enums.RetransmisionSeqNr)

	# noinspection PyTypeChecker
	def read(self) -> List[enums.RetransmisionSeqNr]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:RSN \n
		Snippet: value: List[enums.RetransmisionSeqNr] = driver.uplinkLogging.carrier.rsn.read() \n
		Return results of the UL logging measurement on the E-DPCCH. The results are returned per measured subframe:
		<Reliability>, <RSN>subframe1, <RSN>subframe2, ..., <RSN>subframe n The number of subframes n is configured via method
		RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: rsn: DTX | 0 | 1 | 2 | 3 Retransmission sequence number: DTX: no answer received from the UE 0: new transmission 1: first retransmission 2: second retransmission 3: higher than second retransmission"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:RSN?', suppressed)
		return Conversions.str_to_list_enum(response, enums.RetransmisionSeqNr)
