from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Ber_.State import State
			self._state = State(self._core, self._base)
		return self._state

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ber: enums.ResultStatus2: Bit error rate Range: 0 % to 100 %, Unit: %
			- Bler: enums.ResultStatus2: Block error ratio Range: 0 % to 100 %, Unit: %
			- Dbler: enums.ResultStatus2: Data block error rate Range: 0 % to 100 %, Unit: %
			- Lost_Trans_Blocks: enums.ResultStatus2: Difference between the number of blocks sent and the number of blocks received Range: 0 to total number of blocks sent
			- Ult_Fci_Faults: enums.ResultStatus2: Percentage of transport blocks which the UE receiver detected with a wrong transport format, irrespective of the result of the CRC checks Range: 0 % to 100 %, Unit: %
			- Fdr: enums.ResultStatus2: False transport format detection ratio; the percentage of transport blocks which passed the UE receiver’s CRC check but were detected with a wrong transport format Range: 0 % to 100 %, Unit: %
			- Pn_Discontinuity: enums.ResultStatus2: Number of transport blocks that the R&S CMW corrected (i.e. reordered) in the PN resync procedure Range: 0 to total number of blocks sent"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Ber', enums.ResultStatus2),
			ArgStruct.scalar_enum('Bler', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dbler', enums.ResultStatus2),
			ArgStruct.scalar_enum('Lost_Trans_Blocks', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ult_Fci_Faults', enums.ResultStatus2),
			ArgStruct.scalar_enum('Fdr', enums.ResultStatus2),
			ArgStruct.scalar_enum('Pn_Discontinuity', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ber: enums.ResultStatus2 = None
			self.Bler: enums.ResultStatus2 = None
			self.Dbler: enums.ResultStatus2 = None
			self.Lost_Trans_Blocks: enums.ResultStatus2 = None
			self.Ult_Fci_Faults: enums.ResultStatus2 = None
			self.Fdr: enums.ResultStatus2 = None
			self.Pn_Discontinuity: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:WCDMa:SIGNaling<instance>:BER \n
		Snippet: value: CalculateStruct = driver.ber.calculate() \n
		Returns all results of the signaling BER measurement. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. The number to the left of
		each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:WCDMa:SIGNaling<Instance>:BER?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ber: float: Bit error rate Range: 0 % to 100 %, Unit: %
			- Bler: float: Block error ratio Range: 0 % to 100 %, Unit: %
			- Dbler: float: Data block error rate Range: 0 % to 100 %, Unit: %
			- Lost_Trans_Blocks: int: Difference between the number of blocks sent and the number of blocks received Range: 0 to total number of blocks sent
			- Ult_Fci_Faults: float: Percentage of transport blocks which the UE receiver detected with a wrong transport format, irrespective of the result of the CRC checks Range: 0 % to 100 %, Unit: %
			- Fdr: float: False transport format detection ratio; the percentage of transport blocks which passed the UE receiver’s CRC check but were detected with a wrong transport format Range: 0 % to 100 %, Unit: %
			- Pn_Discontinuity: int: Number of transport blocks that the R&S CMW corrected (i.e. reordered) in the PN resync procedure Range: 0 to total number of blocks sent"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ber'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Dbler'),
			ArgStruct.scalar_int('Lost_Trans_Blocks'),
			ArgStruct.scalar_float('Ult_Fci_Faults'),
			ArgStruct.scalar_float('Fdr'),
			ArgStruct.scalar_int('Pn_Discontinuity')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ber: float = None
			self.Bler: float = None
			self.Dbler: float = None
			self.Lost_Trans_Blocks: int = None
			self.Ult_Fci_Faults: float = None
			self.Fdr: float = None
			self.Pn_Discontinuity: int = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:BER \n
		Snippet: value: ResultData = driver.ber.fetch() \n
		Returns all results of the signaling BER measurement. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. The number to the left of
		each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:BER?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:BER \n
		Snippet: value: ResultData = driver.ber.read() \n
		Returns all results of the signaling BER measurement. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. The number to the left of
		each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:BER?', self.__class__.ResultData())

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:BER')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:BER')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:BER')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:BER')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:BER')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:BER \n
		Snippet: driver.ber.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:BER')

	def clone(self) -> 'Ber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
