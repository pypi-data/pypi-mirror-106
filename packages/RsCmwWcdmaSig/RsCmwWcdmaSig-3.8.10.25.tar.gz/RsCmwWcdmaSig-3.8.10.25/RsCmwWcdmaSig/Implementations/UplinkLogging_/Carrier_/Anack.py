from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Anack:
	"""Anack commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("anack", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.AckNack]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:ANACk \n
		Snippet: value: List[enums.AckNack] = driver.uplinkLogging.carrier.anack.fetch() \n
		Return results of the UL logging measurement on the UL HS-DPCCH. The results are returned per measured subframe:
		<Reliability>, <ACKNACK>subframe1, <ACKNACK>subframe2, ..., <ACKNACK>subframe n The number of subframes n is configured
		via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: ack_nack: DTX | ACK | NACK HARQ-ACK: DTX: no answer received from the UE ACK: successful CRC check of a received transmission packet NACK: failed CRC check of a received transmission packet"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:ANACk?', suppressed)
		return Conversions.str_to_list_enum(response, enums.AckNack)

	# noinspection PyTypeChecker
	def read(self) -> List[enums.AckNack]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:ANACk \n
		Snippet: value: List[enums.AckNack] = driver.uplinkLogging.carrier.anack.read() \n
		Return results of the UL logging measurement on the UL HS-DPCCH. The results are returned per measured subframe:
		<Reliability>, <ACKNACK>subframe1, <ACKNACK>subframe2, ..., <ACKNACK>subframe n The number of subframes n is configured
		via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: ack_nack: DTX | ACK | NACK HARQ-ACK: DTX: no answer received from the UE ACK: successful CRC check of a received transmission packet NACK: failed CRC check of a received transmission packet"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:ANACk?', suppressed)
		return Conversions.str_to_list_enum(response, enums.AckNack)
