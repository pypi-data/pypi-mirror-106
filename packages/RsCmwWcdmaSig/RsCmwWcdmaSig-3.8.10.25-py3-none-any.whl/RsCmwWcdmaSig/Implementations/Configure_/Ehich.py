from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ehich:
	"""Ehich commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ehich", core, parent)

	@property
	def smode(self):
		"""smode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smode'):
			from .Ehich_.Smode import Smode
			self._smode = Smode(self._core, self._base)
		return self._smode

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:TOUT \n
		Snippet: value: float = driver.configure.ehich.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EHICh:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:TOUT \n
		Snippet: driver.configure.ehich.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EHICh:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.ehich.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ehich.mframes to define the number of
		subframes to be measured per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EHICh:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:REPetition \n
		Snippet: driver.configure.ehich.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ehich.mframes to define the number of
		subframes to be measured per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EHICh:REPetition {param}')

	def get_mframes(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:MFRames \n
		Snippet: value: int = driver.configure.ehich.get_mframes() \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . \n
			:return: meas_frames: Range: 100 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EHICh:MFRames?')
		return Conversions.str_to_int(response)

	def set_mframes(self, meas_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:MFRames \n
		Snippet: driver.configure.ehich.set_mframes(meas_frames = 1) \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . \n
			:param meas_frames: Range: 100 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(meas_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EHICh:MFRames {param}')

	def get_limit(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:LIMit \n
		Snippet: value: float = driver.configure.ehich.get_limit() \n
		Specifies limits for the results of the E-HICH measurement. \n
			:return: false_ratio: Upper limit for E-HICH reception 'False Ratio' result Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EHICh:LIMit?')
		return Conversions.str_to_float(response)

	def set_limit(self, false_ratio: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:LIMit \n
		Snippet: driver.configure.ehich.set_limit(false_ratio = 1.0) \n
		Specifies limits for the results of the E-HICH measurement. \n
			:param false_ratio: Upper limit for E-HICH reception 'False Ratio' result Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(false_ratio)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EHICh:LIMit {param}')

	def clone(self) -> 'Ehich':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ehich(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
