from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ergch:
	"""Ergch commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ergch", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Ergch_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:ERGCh')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:ERGCh')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:ERGCh')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:ERGCh')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:ERGCh')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: driver.ergch.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:ERGCh')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Meas_Frames: int: Number of already measured HSUPA subframes
			- Happy_Happy_Bits: int: Number of detected happy happy bits
			- Missed_Up: int: Number of relative grant values that the UE received in error during 'Missed Up' test
			- Missed_Down: int: Number of relative grant values that the UE received in error during 'Missed Down' test
			- Correct_Up: int: Number of relative grant values that the UE received correctly during 'Missed Up' test
			- Correct_Down: int: Number of relative grant values that the UE received correctly during 'Missed Down' test
			- All_Valid_Up: int: Sum of the missed and the correct events during 'Missed Up' test
			- All_Valid_Down: int: Sum of the missed and the correct events during 'Missed Down' test
			- Missed_Up_Ratio: float: 4_MissedUp events / 8_AllValidUp events
			- Missed_Down_Ratio: float: 5_MissedDown events / 9_AllValidDown events
			- Missed_Hold: int: Number of relative grant values that the UE received in error during 'Missed Hold' test
			- Correct_Hold: int: Number of relative grant values that the UE received correctly during 'Missed Hold' test
			- All_Valid_Hold: int: Sum of the missed and the correct events during 'Missed Hold' test
			- Missed_Hold_Ratio: float: 12_MissedHold events / 14_AllValidHold events"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Meas_Frames'),
			ArgStruct.scalar_int('Happy_Happy_Bits'),
			ArgStruct.scalar_int('Missed_Up'),
			ArgStruct.scalar_int('Missed_Down'),
			ArgStruct.scalar_int('Correct_Up'),
			ArgStruct.scalar_int('Correct_Down'),
			ArgStruct.scalar_int('All_Valid_Up'),
			ArgStruct.scalar_int('All_Valid_Down'),
			ArgStruct.scalar_float('Missed_Up_Ratio'),
			ArgStruct.scalar_float('Missed_Down_Ratio'),
			ArgStruct.scalar_int('Missed_Hold'),
			ArgStruct.scalar_int('Correct_Hold'),
			ArgStruct.scalar_int('All_Valid_Hold'),
			ArgStruct.scalar_float('Missed_Hold_Ratio')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Meas_Frames: int = None
			self.Happy_Happy_Bits: int = None
			self.Missed_Up: int = None
			self.Missed_Down: int = None
			self.Correct_Up: int = None
			self.Correct_Down: int = None
			self.All_Valid_Up: int = None
			self.All_Valid_Down: int = None
			self.Missed_Up_Ratio: float = None
			self.Missed_Down_Ratio: float = None
			self.Missed_Hold: int = None
			self.Correct_Hold: int = None
			self.All_Valid_Hold: int = None
			self.Missed_Hold_Ratio: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: value: ResultData = driver.ergch.fetch() \n
		Return all single value results of the E-RGCH measurement. 'Missed Up', 'Missed Down' and 'Missed Hold' test refers to
		wizard settings, see 'Using the WCDMA Wizards'. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:ERGCh?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:ERGCh \n
		Snippet: value: ResultData = driver.ergch.read() \n
		Return all single value results of the E-RGCH measurement. 'Missed Up', 'Missed Down' and 'Missed Hold' test refers to
		wizard settings, see 'Using the WCDMA Wizards'. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:ERGCh?', self.__class__.ResultData())

	def clone(self) -> 'Ergch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ergch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
