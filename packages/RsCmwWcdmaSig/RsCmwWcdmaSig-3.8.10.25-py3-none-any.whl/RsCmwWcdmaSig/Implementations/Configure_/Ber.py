from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	def get_pn_resync(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:PNResync \n
		Snippet: value: bool = driver.configure.ber.get_pn_resync() \n
		Activates or deactivates a correction (reordering) mechanism for transports blocks looped back in wrong order. \n
			:return: enable: OFF | ON ON: correction mechanism active, BER measurement result based on corrected block sequence, number of corrected blocks available as result PN discontinuity OFF: correction mechanism inactive, no PN discontinuity result
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:BER:PNResync?')
		return Conversions.str_to_bool(response)

	def set_pn_resync(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:PNResync \n
		Snippet: driver.configure.ber.set_pn_resync(enable = False) \n
		Activates or deactivates a correction (reordering) mechanism for transports blocks looped back in wrong order. \n
			:param enable: OFF | ON ON: correction mechanism active, BER measurement result based on corrected block sequence, number of corrected blocks available as result PN discontinuity OFF: correction mechanism inactive, no PN discontinuity result
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:BER:PNResync {param}')

	# noinspection PyTypeChecker
	class LimitStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Ber: float or bool: Range: 0 % to 100 %, Unit: % Additional OFF | ON disables | enables the limit using the previous/default level
			- Bler: float or bool: Range: 0 % to 100 %, Unit: % Additional OFF | ON disables | enables the limit using the previous/default level
			- Dbler: float or bool: Range: 0 % to 100 %, Unit: % Additional OFF | ON disables | enables the limit using the previous/default level
			- Lost_Trans_Blocks: int or bool: Range: 1 to 50000 Additional OFF | ON disables | enables the limit using the previous/default level
			- Ult_Fci_Faults: float or bool: Range: 0 % to 100 %, Unit: % Additional OFF | ON disables | enables the limit using the previous/default level
			- Fdr: float or bool: Range: 0 % to 100 %, Unit: % Additional OFF | ON disables | enables the limit using the previous/default level
			- Pn_Discontinuity: int or bool: Range: 1 to 50000 Additional OFF | ON disables | enables the limit using the previous/default level"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Ber'),
			ArgStruct.scalar_float_ext('Bler'),
			ArgStruct.scalar_float_ext('Dbler'),
			ArgStruct.scalar_int_ext('Lost_Trans_Blocks'),
			ArgStruct.scalar_float_ext('Ult_Fci_Faults'),
			ArgStruct.scalar_float_ext('Fdr'),
			ArgStruct.scalar_int_ext('Pn_Discontinuity')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ber: float or bool = None
			self.Bler: float or bool = None
			self.Dbler: float or bool = None
			self.Lost_Trans_Blocks: int or bool = None
			self.Ult_Fci_Faults: float or bool = None
			self.Fdr: float or bool = None
			self.Pn_Discontinuity: int or bool = None

	def get_limit(self) -> LimitStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:LIMit \n
		Snippet: value: LimitStruct = driver.configure.ber.get_limit() \n
		Specifies upper limits for the results of the 'BER' measurement. \n
			:return: structure: for return value, see the help for LimitStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:BER:LIMit?', self.__class__.LimitStruct())

	def set_limit(self, value: LimitStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:LIMit \n
		Snippet: driver.configure.ber.set_limit(value = LimitStruct()) \n
		Specifies upper limits for the results of the 'BER' measurement. \n
			:param value: see the help for LimitStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:BER:LIMit', value)

	def get_tblocks(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:TBLocks \n
		Snippet: value: int = driver.configure.ber.get_tblocks() \n
		Defines the number of transport blocks to be measured per measurement cycle (statistics cycle) . \n
			:return: transport_blocks: Range: 1 to 50E+3
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:BER:TBLocks?')
		return Conversions.str_to_int(response)

	def set_tblocks(self, transport_blocks: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:TBLocks \n
		Snippet: driver.configure.ber.set_tblocks(transport_blocks = 1) \n
		Defines the number of transport blocks to be measured per measurement cycle (statistics cycle) . \n
			:param transport_blocks: Range: 1 to 50E+3
		"""
		param = Conversions.decimal_value_to_str(transport_blocks)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:BER:TBLocks {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.ber.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:BER:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:SCONdition \n
		Snippet: driver.configure.ber.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:BER:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.ber.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ber.tblocks to determine the number of
		transport blocks per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:BER:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:REPetition \n
		Snippet: driver.configure.ber.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Ber.tblocks to determine the number of
		transport blocks per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:BER:REPetition {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:TOUT \n
		Snippet: value: float = driver.configure.ber.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:BER:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:BER:TOUT \n
		Snippet: driver.configure.ber.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:BER:TOUT {param}')
