from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:MCQI:CARRier<carrier> \n
		Snippet: value: int = driver.hack.mcqi.carrier.fetch() \n
		Return the median CQI result per carrier, see 'Median CQI'. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: median_cqi: Range: 0 to 31"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:MCQI:CARRier<Carrier>?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:MCQI:CARRier<carrier> \n
		Snippet: value: int = driver.hack.mcqi.carrier.read() \n
		Return the median CQI result per carrier, see 'Median CQI'. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: median_cqi: Range: 0 to 31"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:HACK:MCQI:CARRier<Carrier>?', suppressed)
		return Conversions.str_to_int(response)
