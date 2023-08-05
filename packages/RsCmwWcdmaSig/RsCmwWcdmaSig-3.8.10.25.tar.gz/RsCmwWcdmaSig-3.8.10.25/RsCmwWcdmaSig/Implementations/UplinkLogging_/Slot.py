from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slot:
	"""Slot commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("slot", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:SLOT \n
		Snippet: value: List[int] = driver.uplinkLogging.slot.fetch() \n
		Return results of the UL logging measurement on the E-DPCCH/DPCCH/HS-DPCCH. The results are returned per measured
		subframe: <Reliability>, <Slot>subframe1, <Slot>subframe2, ..., <Slot>subframe n The number of subframes n is configured
		via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: slot: First slot number of the received UL HS-DPCCH/E-DPCCH/DPCCH subframe; see 'UL Logging Measurement' Range: 0 | 3 | 6 | 9 | 12"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:SLOT?', suppressed)
		return response

	def read(self) -> List[int]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:SLOT \n
		Snippet: value: List[int] = driver.uplinkLogging.slot.read() \n
		Return results of the UL logging measurement on the E-DPCCH/DPCCH/HS-DPCCH. The results are returned per measured
		subframe: <Reliability>, <Slot>subframe1, <Slot>subframe2, ..., <Slot>subframe n The number of subframes n is configured
		via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: slot: First slot number of the received UL HS-DPCCH/E-DPCCH/DPCCH subframe; see 'UL Logging Measurement' Range: 0 | 3 | 6 | 9 | 12"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:SLOT?', suppressed)
		return response
