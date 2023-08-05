from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HCQI:TRACe:CARRier<carrier> \n
		Snippet: value: List[float] = driver.hcqi.trace.carrier.fetch() \n
		Returns the CQI distribution results in percentage per carrier. For each CQI value one result is returned: <Reliability>,
		<HistCQI>0, ..., <HistCQI>31 \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: hist_cqi: Histogram CQI: percentage of the reported CQI value 0 to 30 per measurement cycle The position 31 indicates the percentage of DTX subframes. Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:HCQI:TRACe:CARRier<Carrier>?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HCQI:TRACe:CARRier<carrier> \n
		Snippet: value: List[float] = driver.hcqi.trace.carrier.read() \n
		Returns the CQI distribution results in percentage per carrier. For each CQI value one result is returned: <Reliability>,
		<HistCQI>0, ..., <HistCQI>31 \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: hist_cqi: Histogram CQI: percentage of the reported CQI value 0 to 30 per measurement cycle The position 31 indicates the percentage of DTX subframes. Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:WCDMa:SIGNaling<Instance>:HCQI:TRACe:CARRier<Carrier>?', suppressed)
		return response
