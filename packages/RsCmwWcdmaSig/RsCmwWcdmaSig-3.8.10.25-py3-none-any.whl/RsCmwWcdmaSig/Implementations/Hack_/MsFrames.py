from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsFrames:
	"""MsFrames commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msFrames", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:MSFRames \n
		Snippet: value: int = driver.hack.msFrames.fetch() \n
		Return the total number of already measured HSDPA subframes. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: meas_sub_frames: Range: 0 to 2E+9"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:MSFRames?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:MSFRames \n
		Snippet: value: int = driver.hack.msFrames.read() \n
		Return the total number of already measured HSDPA subframes. \n
		Use RsCmwWcdmaSig.reliability.last_value to read the updated reliability indicator. \n
			:return: meas_sub_frames: Range: 0 to 2E+9"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:WCDMa:SIGNaling<Instance>:HACK:MSFRames?', suppressed)
		return Conversions.str_to_int(response)
