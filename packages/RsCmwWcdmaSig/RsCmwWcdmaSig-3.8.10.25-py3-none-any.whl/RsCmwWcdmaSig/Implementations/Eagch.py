from typing import List

from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.Types import DataType
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eagch:
	"""Eagch commands group definition. 9 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eagch", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Eagch_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Eagch_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:EAGCh')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:EAGCh')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:EAGCh')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:EAGCh')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:EAGCh')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: driver.eagch.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:EAGCh')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Measured_Frames: int: Number of already measured HSUPA subframes Range: 1 to 1E+6
			- Tot_Etfci_Events: int: Sum of all detected E-TFCI events Range: 1 to 1E+6
			- Missed_Det: float: Number of missed expected E-TFCI detections Range: 1 to 1E+6
			- Missed_Det_Prop: float: Missed detection probability (4_MissedDet / 3_TotETFCIEvents) Range: 0 % to 100 %
			- Happy_Bits: int: Number of happy happy bits Range: 1 to 1E+6
			- Etfci_Nr: List[int]: Expected E-TFCI value Range: 0 to 127
			- Etfci_Events: List[int]: Number of detections Range: 0 to 1E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Measured_Frames'),
			ArgStruct.scalar_int('Tot_Etfci_Events'),
			ArgStruct.scalar_float('Missed_Det'),
			ArgStruct.scalar_float('Missed_Det_Prop'),
			ArgStruct.scalar_int('Happy_Bits'),
			ArgStruct('Etfci_Nr', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Etfci_Events', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Measured_Frames: int = None
			self.Tot_Etfci_Events: int = None
			self.Missed_Det: float = None
			self.Missed_Det_Prop: float = None
			self.Happy_Bits: int = None
			self.Etfci_Nr: List[int] = None
			self.Etfci_Events: List[int] = None

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: value: ResultData = driver.eagch.read() \n
		Return all single value results of the E-AGCH measurement. The results are returned as groups per most frequently
		detected E-TFCI values: <1_Reliability>, <2_MeasedFrames>, <3_TotETFCIEvents>, <4_MissedDet>, <5_MissedDetProb>,
		<6_HappyBits>, {<7_ETFCINr>, <8_ETFCIEvents>}1, {...}2, ..., {...}8 The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:EAGCh?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:EAGCh \n
		Snippet: value: ResultData = driver.eagch.fetch() \n
		Return all single value results of the E-AGCH measurement. The results are returned as groups per most frequently
		detected E-TFCI values: <1_Reliability>, <2_MeasedFrames>, <3_TotETFCIEvents>, <4_MissedDet>, <5_MissedDetProb>,
		<6_HappyBits>, {<7_ETFCINr>, <8_ETFCIEvents>}1, {...}2, ..., {...}8 The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:EAGCh?', self.__class__.ResultData())

	def clone(self) -> 'Eagch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eagch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
