from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ergch:
	"""Ergch commands group definition. 9 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ergch", core, parent)

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_etfci'):
			from .Ergch_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:TOUT \n
		Snippet: value: float = driver.configure.ergch.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:TOUT \n
		Snippet: driver.configure.ergch.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.ergch.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ergch.mframes to define the number of
		subframes to be measured per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:REPetition \n
		Snippet: driver.configure.ergch.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ergch.mframes to define the number of
		subframes to be measured per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:REPetition {param}')

	def get_mframes(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:MFRames \n
		Snippet: value: int = driver.configure.ergch.get_mframes() \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . Ideally, one relative grant
		value is detected per TTI. \n
			:return: meas_frames: Range: 1 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:MFRames?')
		return Conversions.str_to_int(response)

	def set_mframes(self, meas_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:MFRames \n
		Snippet: driver.configure.ergch.set_mframes(meas_frames = 1) \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . Ideally, one relative grant
		value is detected per TTI. \n
			:param meas_frames: Range: 1 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(meas_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:MFRames {param}')

	# noinspection PyTypeChecker
	class LimitStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Missed_Down_Ratio: float: Range: 0 % to 100 %
			- Missed_Up_Ratio: float: Range: 0 % to 100 %
			- Missed_Hold_Ratio: float: Range: 0 % to 100 %"""
		__meta_args_list = [
			ArgStruct.scalar_float('Missed_Down_Ratio'),
			ArgStruct.scalar_float('Missed_Up_Ratio'),
			ArgStruct.scalar_float('Missed_Hold_Ratio')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Missed_Down_Ratio: float = None
			self.Missed_Up_Ratio: float = None
			self.Missed_Hold_Ratio: float = None

	def get_limit(self) -> LimitStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:LIMit \n
		Snippet: value: LimitStruct = driver.configure.ergch.get_limit() \n
		Specifies the upper limit for the missed DOWN / UP / HOLD ratios. \n
			:return: structure: for return value, see the help for LimitStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:LIMit?', self.__class__.LimitStruct())

	def set_limit(self, value: LimitStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ERGCh:LIMit \n
		Snippet: driver.configure.ergch.set_limit(value = LimitStruct()) \n
		Specifies the upper limit for the missed DOWN / UP / HOLD ratios. \n
			:param value: see the help for LimitStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:ERGCh:LIMit', value)

	def clone(self) -> 'Ergch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ergch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
