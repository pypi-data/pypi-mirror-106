from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


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
			- Meas_Frames: int: Number of already measured HSUPA subframes Range: 0 to 1E+6
			- False_Rx: int: Number of transmissions that the UE received incorrectly Range: 0 to 1E+6
			- Correct_Rx: int: Number of transmissions that the UE received correctly Range: 0 to 1E+6
			- All_Valid_Rx: int: Number of transmissions that the UE received correctly or incorrectly For all three 'RX' results, the first new data block after a complete retransmission cycle is not counted as a test sample. Range: 0 to 1E+6
			- False_Ratio: float: Ratio of 3_FalseRX to 5_AllValidRX Range: 0 % to 100 %, Unit: %
			- Correct_Crc: int: Number of transmissions with correct CRC Range: 0 to 1E+6
			- Error_Crc: int: Number of transmissions with incorrect CRC Range: 0 to 1E+6
			- Bler: float: Block error rate resulting from CRC results Range: 0 % to 100 %, Unit: %
			- Thrpt_Current: float: Current throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Thrpt_Max_Pos: float: Current throughput if there would be no CRC errors Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Thrpt_Max_Exp: float: Expected maximum reachable throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Thrpt_Average: float: Average throughput Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Thrpt_Maximum: float: Maximum throughput since the start of the measurement Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s
			- Thrpt_Minimum: float: Minimum throughput since the start of the measurement Range: 0 bit/s to 100E+6 bit/s, Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Meas_Frames'),
			ArgStruct.scalar_int('False_Rx'),
			ArgStruct.scalar_int('Correct_Rx'),
			ArgStruct.scalar_int('All_Valid_Rx'),
			ArgStruct.scalar_float('False_Ratio'),
			ArgStruct.scalar_int('Correct_Crc'),
			ArgStruct.scalar_int('Error_Crc'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Thrpt_Current'),
			ArgStruct.scalar_float('Thrpt_Max_Pos'),
			ArgStruct.scalar_float('Thrpt_Max_Exp'),
			ArgStruct.scalar_float('Thrpt_Average'),
			ArgStruct.scalar_float('Thrpt_Maximum'),
			ArgStruct.scalar_float('Thrpt_Minimum')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Meas_Frames: int = None
			self.False_Rx: int = None
			self.Correct_Rx: int = None
			self.All_Valid_Rx: int = None
			self.False_Ratio: float = None
			self.Correct_Crc: int = None
			self.Error_Crc: int = None
			self.Bler: float = None
			self.Thrpt_Current: float = None
			self.Thrpt_Max_Pos: float = None
			self.Thrpt_Max_Exp: float = None
			self.Thrpt_Average: float = None
			self.Thrpt_Maximum: float = None
			self.Thrpt_Minimum: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:EHICh:CARRier<carrier> \n
		Snippet: value: ResultData = driver.ehich.carrier.read() \n
		Return all single value results of the E-HICH measurement per carrier. The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:EHICh:CARRier<Carrier>?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:EHICh:CARRier<carrier> \n
		Snippet: value: ResultData = driver.ehich.carrier.fetch() \n
		Return all single value results of the E-HICH measurement per carrier. The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:EHICh:CARRier<Carrier>?', self.__class__.ResultData())
