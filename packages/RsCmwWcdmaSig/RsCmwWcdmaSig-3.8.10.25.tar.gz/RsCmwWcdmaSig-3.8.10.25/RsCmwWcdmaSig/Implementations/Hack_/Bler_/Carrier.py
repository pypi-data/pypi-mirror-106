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

	def fetch(self) -> float:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:BLER:CARRier<carrier> \n
		Snippet: value: float = driver.hack.bler.carrier.fetch() \n
		Return the BLER result per carrier, see 'DL BLER'. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: bler: Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:BLER:CARRier<Carrier>?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:BLER:CARRier<carrier> \n
		Snippet: value: float = driver.hack.bler.carrier.read() \n
		Return the BLER result per carrier, see 'DL BLER'. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: bler: Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:HACK:BLER:CARRier<Carrier>?', suppressed)
		return Conversions.str_to_float(response)
