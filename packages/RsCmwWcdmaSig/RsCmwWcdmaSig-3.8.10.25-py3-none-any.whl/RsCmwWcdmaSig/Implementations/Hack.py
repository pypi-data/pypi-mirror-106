from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hack:
	"""Hack commands group definition. 39 total commands, 7 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hack", core, parent)

	@property
	def trace(self):
		"""trace commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Hack_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def mcqi(self):
		"""mcqi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcqi'):
			from .Hack_.Mcqi import Mcqi
			self._mcqi = Mcqi(self._core, self._base)
		return self._mcqi

	@property
	def msFrames(self):
		"""msFrames commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_msFrames'):
			from .Hack_.MsFrames import MsFrames
			self._msFrames = MsFrames(self._core, self._base)
		return self._msFrames

	@property
	def bler(self):
		"""bler commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bler'):
			from .Hack_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def throughput(self):
		"""throughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_throughput'):
			from .Hack_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def transmission(self):
		"""transmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_transmission'):
			from .Hack_.Transmission import Transmission
			self._transmission = Transmission(self._core, self._base)
		return self._transmission

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Hack_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:HACK')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:HACK')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:HACK')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:HACK')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:HACK')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:HACK \n
		Snippet: driver.hack.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:HACK')

	def clone(self) -> 'Hack':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hack(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
