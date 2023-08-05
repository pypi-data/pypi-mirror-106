from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkLogging:
	"""UplinkLogging commands group definition. 27 total commands, 7 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplinkLogging", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .UplinkLogging_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def sfn(self):
		"""sfn commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sfn'):
			from .UplinkLogging_.Sfn import Sfn
			self._sfn = Sfn(self._core, self._base)
		return self._sfn

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_slot'):
			from .UplinkLogging_.Slot import Slot
			self._slot = Slot(self._core, self._base)
		return self._slot

	@property
	def carrier(self):
		"""carrier commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .UplinkLogging_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scell'):
			from .UplinkLogging_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcarrier'):
			from .UplinkLogging_.Dcarrier import Dcarrier
			self._dcarrier = Dcarrier(self._core, self._base)
		return self._dcarrier

	@property
	def dchspa(self):
		"""dchspa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dchspa'):
			from .UplinkLogging_.Dchspa import Dchspa
			self._dchspa = Dchspa(self._core, self._base)
		return self._dchspa

	def stop(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:WCDMa:SIGNaling<Instance>:ULLogging')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:WCDMa:SIGNaling<Instance>:ULLogging')

	def abort(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:WCDMa:SIGNaling<Instance>:ULLogging')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:WCDMa:SIGNaling<Instance>:ULLogging')

	def initiate(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:WCDMa:SIGNaling<Instance>:ULLogging')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:WCDMa:SIGNaling<instance>:ULLogging \n
		Snippet: driver.uplinkLogging.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:WCDMa:SIGNaling<Instance>:ULLogging')

	def clone(self) -> 'UplinkLogging':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkLogging(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
