from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqi:
	"""Cqi commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cqi", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.Cqi]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:CQI \n
		Snippet: value: List[enums.Cqi] = driver.uplinkLogging.carrier.cqi.fetch() \n
		Return results of the UL logging measurement on the HS-DPCCH. The results are returned per measured subframe:
		<Reliability>, <CQI>subframe1, <CQI>subframe2, ..., <CQI>subframe n The number of subframes n is configured via method
		RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: cqi: DTX | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 DTX: no answer received from the UE 0 to 30: reported channel quality indicator, 30 means the best quality"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:CQI?', suppressed)
		return Conversions.str_to_list_enum(response, enums.Cqi)

	# noinspection PyTypeChecker
	def read(self) -> List[enums.Cqi]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:CQI \n
		Snippet: value: List[enums.Cqi] = driver.uplinkLogging.carrier.cqi.read() \n
		Return results of the UL logging measurement on the HS-DPCCH. The results are returned per measured subframe:
		<Reliability>, <CQI>subframe1, <CQI>subframe2, ..., <CQI>subframe n The number of subframes n is configured via method
		RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: cqi: DTX | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 DTX: no answer received from the UE 0 to 30: reported channel quality indicator, 30 means the best quality"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:CQI?', suppressed)
		return Conversions.str_to_list_enum(response, enums.Cqi)
