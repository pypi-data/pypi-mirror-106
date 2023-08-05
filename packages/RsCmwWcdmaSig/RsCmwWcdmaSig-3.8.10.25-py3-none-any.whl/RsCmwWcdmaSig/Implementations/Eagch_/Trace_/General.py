from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class General:
	"""General commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("general", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliablility: int: See 'Reliability Indicator'
			- Events: List[int]: Detections for all E-TFCI values 0 to 127 from first to last (most recent) measured subframe Range: 0 to 1E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliablility'),
			ArgStruct('Events', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliablility: int = None
			self.Events: List[int] = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:EAGCh:TRACe:GENeral \n
		Snippet: value: ResultData = driver.eagch.trace.general.read() \n
		Return the results of the detected E-TFCI values 0 to 127 for 'Measurement Type' = 'General Histogram'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:EAGCh:TRACe:GENeral?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:EAGCh:TRACe:GENeral \n
		Snippet: value: ResultData = driver.eagch.trace.general.fetch() \n
		Return the results of the detected E-TFCI values 0 to 127 for 'Measurement Type' = 'General Histogram'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:EAGCh:TRACe:GENeral?', self.__class__.ResultData())
