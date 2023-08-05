from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hack:
	"""Hack commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hack", core, parent)

	@property
	def smode(self):
		"""smode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smode'):
			from .Hack_.Smode import Smode
			self._smode = Smode(self._core, self._base)
		return self._smode

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:TOUT \n
		Snippet: value: float = driver.configure.hack.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HACK:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:TOUT \n
		Snippet: driver.configure.hack.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HACK:TOUT {param}')

	# noinspection PyTypeChecker
	def get_harq(self) -> enums.MonitoredHarq:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:HARQ \n
		Snippet: value: enums.MonitoredHarq = driver.configure.hack.get_harq() \n
		Selects either a single H-ARQ process (numbered 0 to 7) to be monitored or specifies that all processes are to be
		monitored. \n
			:return: monitored_harq: ALL | H0 | H1 | H2 | H3 | H4 | H5 | H6 | H7
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HACK:HARQ?')
		return Conversions.str_to_scalar_enum(response, enums.MonitoredHarq)

	def set_harq(self, monitored_harq: enums.MonitoredHarq) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:HARQ \n
		Snippet: driver.configure.hack.set_harq(monitored_harq = enums.MonitoredHarq.ALL) \n
		Selects either a single H-ARQ process (numbered 0 to 7) to be monitored or specifies that all processes are to be
		monitored. \n
			:param monitored_harq: ALL | H0 | H1 | H2 | H3 | H4 | H5 | H6 | H7
		"""
		param = Conversions.enum_scalar_to_str(monitored_harq, enums.MonitoredHarq)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HACK:HARQ {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.hack.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Hack.msFrames to determine the number of HSDPA
		subframes to be measured per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HACK:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:REPetition \n
		Snippet: driver.configure.hack.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Hack.msFrames to determine the number of HSDPA
		subframes to be measured per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HACK:REPetition {param}')

	def get_ms_frames(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:MSFRames \n
		Snippet: value: int = driver.configure.hack.get_ms_frames() \n
		Defines the number of HSDPA subframes to be measured per measurement cycle (statistics cycle) . \n
			:return: meas_sub_frames: Range: 100 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HACK:MSFRames?')
		return Conversions.str_to_int(response)

	def set_ms_frames(self, meas_sub_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HACK:MSFRames \n
		Snippet: driver.configure.hack.set_ms_frames(meas_sub_frames = 1) \n
		Defines the number of HSDPA subframes to be measured per measurement cycle (statistics cycle) . \n
			:param meas_sub_frames: Range: 100 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(meas_sub_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HACK:MSFRames {param}')

	def clone(self) -> 'Hack':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hack(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
