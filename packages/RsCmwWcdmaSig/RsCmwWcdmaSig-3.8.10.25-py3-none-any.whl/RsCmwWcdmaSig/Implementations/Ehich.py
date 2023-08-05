from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ehich:
	"""Ehich commands group definition. 17 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ehich", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Ehich_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Ehich_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_carrier'):
			from .Ehich_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def throughput(self):
		"""throughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_throughput'):
			from .Ehich_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:EHICh')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:EHICh')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:EHICh')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:EHICh')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:EHICh')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:EHICh \n
		Snippet: driver.ehich.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:EHICh')

	def clone(self) -> 'Ehich':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ehich(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
