from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eagch:
	"""Eagch commands group definition. 8 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eagch", core, parent)

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_etfci'):
			from .Eagch_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:TOUT \n
		Snippet: value: float = driver.configure.eagch.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:TOUT \n
		Snippet: driver.configure.eagch.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.eagch.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Eagch.mframes to define the number of
		subframes to be measured per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:REPetition \n
		Snippet: driver.configure.eagch.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Eagch.mframes to define the number of
		subframes to be measured per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:REPetition {param}')

	def get_mframes(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:MFRames \n
		Snippet: value: int = driver.configure.eagch.get_mframes() \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . Ideally, one E-TFCI value is
		detected per TTI. \n
			:return: meas_frames: Range: 1 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:MFRames?')
		return Conversions.str_to_int(response)

	def set_mframes(self, meas_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:MFRames \n
		Snippet: driver.configure.eagch.set_mframes(meas_frames = 1) \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . Ideally, one E-TFCI value is
		detected per TTI. \n
			:param meas_frames: Range: 1 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(meas_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:MFRames {param}')

	# noinspection PyTypeChecker
	def get_mtype(self) -> enums.MeasType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:MTYPe \n
		Snippet: value: enums.MeasType = driver.configure.eagch.get_mtype() \n
		Specifies the type of measurement. \n
			:return: meas_type: GENeral | MISSed General histogram or missed detection
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:MTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasType)

	def set_mtype(self, meas_type: enums.MeasType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:MTYPe \n
		Snippet: driver.configure.eagch.set_mtype(meas_type = enums.MeasType.GENeral) \n
		Specifies the type of measurement. \n
			:param meas_type: GENeral | MISSed General histogram or missed detection
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.MeasType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:MTYPe {param}')

	def get_limit(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:LIMit \n
		Snippet: value: float = driver.configure.eagch.get_limit() \n
		Upper limit for the ratio of missed detections to the detected E-TFCI events. \n
			:return: probability: Range: 0 % to 100 %
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:LIMit?')
		return Conversions.str_to_float(response)

	def set_limit(self, probability: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EAGCh:LIMit \n
		Snippet: driver.configure.eagch.set_limit(probability = 1.0) \n
		Upper limit for the ratio of missed detections to the detected E-TFCI events. \n
			:param probability: Range: 0 % to 100 %
		"""
		param = Conversions.decimal_value_to_str(probability)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EAGCh:LIMit {param}')

	def clone(self) -> 'Eagch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eagch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
