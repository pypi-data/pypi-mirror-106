from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hbit:
	"""Hbit commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hbit", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.HappyBit]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:HBIT \n
		Snippet: value: List[enums.HappyBit] = driver.uplinkLogging.carrier.hbit.fetch() \n
		Return results of the UL logging measurement on the E-DPCCH. The results are returned per measured subframe:
		<Reliability>, <HappyBit>subframe1, <HappyBit>subframe2, ..., <HappyBit>subframe n The number of subframes n is
		configured via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: happy_bit: HAPPy | UNHappy | DTX HAPPy: UE is satisfied with the granted data rate UNHappy: UE is not transmitting at maximum power and cannot empty its transmit buffer with the current serving grant within a certain time period DTX: no answer received from the UE"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:HBIT?', suppressed)
		return Conversions.str_to_list_enum(response, enums.HappyBit)

	# noinspection PyTypeChecker
	def read(self) -> List[enums.HappyBit]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:HBIT \n
		Snippet: value: List[enums.HappyBit] = driver.uplinkLogging.carrier.hbit.read() \n
		Return results of the UL logging measurement on the E-DPCCH. The results are returned per measured subframe:
		<Reliability>, <HappyBit>subframe1, <HappyBit>subframe2, ..., <HappyBit>subframe n The number of subframes n is
		configured via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: happy_bit: HAPPy | UNHappy | DTX HAPPy: UE is satisfied with the granted data rate UNHappy: UE is not transmitting at maximum power and cannot empty its transmit buffer with the current serving grant within a certain time period DTX: no answer received from the UE"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:HBIT?', suppressed)
		return Conversions.str_to_list_enum(response, enums.HappyBit)
