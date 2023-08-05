from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Transmitted: List[float]: No parameter help available
			- Ack: List[float]: No parameter help available
			- Nack: List[float]: No parameter help available
			- Dtx: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Transmitted', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ack', DataType.FloatList, None, False, True, 1),
			ArgStruct('Nack', DataType.FloatList, None, False, True, 1),
			ArgStruct('Dtx', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Transmitted: List[float] = None
			self.Ack: List[float] = None
			self.Nack: List[float] = None
			self.Dtx: List[float] = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HACK:TRANsmission:CARRier<carrier> \n
		Snippet: value: ResultData = driver.hack.transmission.carrier.fetch() \n
		Return all results of the 'Transmissions' table row by row, see 'Transmissions'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:HACK:TRANsmission:CARRier<Carrier>?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HACK:TRANsmission:CARRier<carrier> \n
		Snippet: value: ResultData = driver.hack.transmission.carrier.read() \n
		Return all results of the 'Transmissions' table row by row, see 'Transmissions'. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:HACK:TRANsmission:CARRier<Carrier>?', self.__class__.ResultData())
