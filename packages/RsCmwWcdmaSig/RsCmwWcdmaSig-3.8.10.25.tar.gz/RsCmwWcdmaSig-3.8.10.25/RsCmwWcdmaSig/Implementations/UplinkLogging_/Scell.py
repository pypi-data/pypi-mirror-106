from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scell:
	"""Scell commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scell", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Sfn: List[int]: System frame number corresponds to the subframe number for which the UL HS-DPCCH/E-DPCCH/DPCCH information is displayed (set to modulo 4095) Range: 0 to 4095
			- Slot: List[int]: First slot number of the received UL HS-DPCCH/E-DPCCH/DPCCH subframe; see 'UL Logging Measurement' Range: 0 | 3 | 6 | 9 | 12
			- Etfci: List[enums.Etfci]: DTX | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 122 | 123 | 124 | 125 | 126 | 127 See also Table '2ms TTI E-DCH transport block size' DTX: no answer received from the UE 0 to 127: indicates the transport block size on the E-DPDCH
			- Rsn: List[enums.RetransmisionSeqNr]: No parameter help available
			- Happy_Bit: List[enums.HappyBit]: HAPPy | UNHappy | DTX HAPPy: UE is satisfied with the granted data rate UNHappy: UE is not transmitting at maximum power and cannot empty its transmit buffer with the current serving grant within a certain time period DTX: no answer received from the UE
			- Dpcch_1: List[bool]: No parameter help available
			- Dpcch_2: List[bool]: No parameter help available
			- Dpcch_3: List[bool]: No parameter help available
			- Ack_Nack: List[enums.AckNack]: No parameter help available
			- Cqi: List[enums.Cqi]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Sfn', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Etfci', DataType.EnumList, enums.Etfci, False, True, 1),
			ArgStruct('Rsn', DataType.EnumList, enums.RetransmisionSeqNr, False, True, 1),
			ArgStruct('Happy_Bit', DataType.EnumList, enums.HappyBit, False, True, 1),
			ArgStruct('Dpcch_1', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Dpcch_2', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Dpcch_3', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Ack_Nack', DataType.EnumList, enums.AckNack, False, True, 1),
			ArgStruct('Cqi', DataType.EnumList, enums.Cqi, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sfn: List[int] = None
			self.Slot: List[int] = None
			self.Etfci: List[enums.Etfci] = None
			self.Rsn: List[enums.RetransmisionSeqNr] = None
			self.Happy_Bit: List[enums.HappyBit] = None
			self.Dpcch_1: List[bool] = None
			self.Dpcch_2: List[bool] = None
			self.Dpcch_3: List[bool] = None
			self.Ack_Nack: List[enums.AckNack] = None
			self.Cqi: List[enums.Cqi] = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ULLogging[:SCELl] \n
		Snippet: value: ResultData = driver.uplinkLogging.scell.fetch() \n
		Return all results of the UL logging measurement on the E-DPCCH/DPCCH/HS-DPCCH. The results are returned as groups per
		measured subframe: <Reliability>, {<SFN>, <Slot>, <ETFCI>, <RSN>, <HappyBit>, <DPCCH1>, <DPCCH2>, <DPCCH3>, <ACKNACK>,
		<CQI>}subframe 1, {...}subframe 2, ..., {...}subframe n The number of subframes n is configured via method RsCmwWcdmaSig.
		Configure.UplinkLogging.msFrames. The number to the left of each result parameter is provided for easy identification of
		the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:ULLogging:SCELl?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ULLogging[:SCELl] \n
		Snippet: value: ResultData = driver.uplinkLogging.scell.read() \n
		Return all results of the UL logging measurement on the E-DPCCH/DPCCH/HS-DPCCH. The results are returned as groups per
		measured subframe: <Reliability>, {<SFN>, <Slot>, <ETFCI>, <RSN>, <HappyBit>, <DPCCH1>, <DPCCH2>, <DPCCH3>, <ACKNACK>,
		<CQI>}subframe 1, {...}subframe 2, ..., {...}subframe n The number of subframes n is configured via method RsCmwWcdmaSig.
		Configure.UplinkLogging.msFrames. The number to the left of each result parameter is provided for easy identification of
		the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:ULLogging:SCELl?', self.__class__.ResultData())
