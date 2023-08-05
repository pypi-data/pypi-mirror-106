from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcch:
	"""Dpcch commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpcch", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Dpcch_1: List[bool]: OFF | ON Queries the status of DPCCH read out from the first slot
			- Dpcch_2: List[bool]: OFF | ON Queries the status of DPCCH read out from the second slot
			- Dpcch_3: List[bool]: OFF | ON Queries the status of DPCCH read out from the third slot"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Dpcch_1', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Dpcch_2', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Dpcch_3', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Dpcch_1: List[bool] = None
			self.Dpcch_2: List[bool] = None
			self.Dpcch_3: List[bool] = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:DPCCh \n
		Snippet: value: ResultData = driver.uplinkLogging.carrier.dpcch.fetch() \n
		Return results of the UL logging measurement on the DPCCH. The results are returned as groups per measured subframe:
		<Reliability>, {<DPCCH1>, <DPCCH2>, <DPCCH3>}subframe1, {...}subframe 2, ..., {...}subframe n The number of subframes n
		is configured via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:DPCCh?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging:CARRier<carrier>:DPCCh \n
		Snippet: value: ResultData = driver.uplinkLogging.carrier.dpcch.read() \n
		Return results of the UL logging measurement on the DPCCH. The results are returned as groups per measured subframe:
		<Reliability>, {<DPCCH1>, <DPCCH2>, <DPCCH3>}subframe1, {...}subframe 2, ..., {...}subframe n The number of subframes n
		is configured via method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:CARRier<Carrier>:DPCCh?', self.__class__.ResultData())
