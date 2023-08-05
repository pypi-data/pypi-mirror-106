from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfn:
	"""Sfn commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sfn", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:SFN \n
		Snippet: value: List[int] = driver.uplinkLogging.sfn.fetch() \n
		Return results of the UL logging measurement on the UL HS-DPCCH/E-DPCCH/DPCCH. The results are returned per measured
		subframe: <Reliability>, <SFN>subframe1, <SFN>subframe2, ..., <SFN>subframe n The number of subframes n is configured via
		method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: sfn: System frame number corresponds to the subframe number for which the UL logging information is displayed (set to modulo 4095) Range: 0 to 4095"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:SFN?', suppressed)
		return response

	def read(self) -> List[int]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:SFN \n
		Snippet: value: List[int] = driver.uplinkLogging.sfn.read() \n
		Return results of the UL logging measurement on the UL HS-DPCCH/E-DPCCH/DPCCH. The results are returned per measured
		subframe: <Reliability>, <SFN>subframe1, <SFN>subframe2, ..., <SFN>subframe n The number of subframes n is configured via
		method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: sfn: System frame number corresponds to the subframe number for which the UL logging information is displayed (set to modulo 4095) Range: 0 to 4095"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:SFN?', suppressed)
		return response
