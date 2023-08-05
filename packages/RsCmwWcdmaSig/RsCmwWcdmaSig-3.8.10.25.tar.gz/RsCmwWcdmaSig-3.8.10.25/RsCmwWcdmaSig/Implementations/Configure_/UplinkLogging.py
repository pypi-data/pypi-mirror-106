from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkLogging:
	"""UplinkLogging commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplinkLogging", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:TOUT \n
		Snippet: value: float = driver.configure.uplinkLogging.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:TOUT \n
		Snippet: driver.configure.uplinkLogging.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:TOUT {param}')

	def get_sccycle(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:SCCYcle \n
		Snippet: value: bool = driver.configure.uplinkLogging.get_sccycle() \n
		Enables in the UL logging RX measurement to be started two subframes before a CPC cycle one. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:SCCYcle?')
		return Conversions.str_to_bool(response)

	def set_sccycle(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:SCCYcle \n
		Snippet: driver.configure.uplinkLogging.set_sccycle(enable = False) \n
		Enables in the UL logging RX measurement to be started two subframes before a CPC cycle one. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:SCCYcle {param}')

	def get_ssfn(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:SSFN \n
		Snippet: value: int or bool = driver.configure.uplinkLogging.get_ssfn() \n
		Specifies the first system frame number for which the UL HS-DPCCH/E-DPCCH/DPCCH information is displayed. System frame
		number corresponds to the subframe number of the UL HS-DPCCH/E-DPCCH/DPCCH. \n
			:return: sfn: First system frame number set to modulo 4095 Range: 0 to 4095 Additional ON / OFF enables or disables the use of SFN.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:SSFN?')
		return Conversions.str_to_int_or_bool(response)

	def set_ssfn(self, sfn: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:SSFN \n
		Snippet: driver.configure.uplinkLogging.set_ssfn(sfn = 1) \n
		Specifies the first system frame number for which the UL HS-DPCCH/E-DPCCH/DPCCH information is displayed. System frame
		number corresponds to the subframe number of the UL HS-DPCCH/E-DPCCH/DPCCH. \n
			:param sfn: First system frame number set to modulo 4095 Range: 0 to 4095 Additional ON / OFF enables or disables the use of SFN.
		"""
		param = Conversions.decimal_or_bool_value_to_str(sfn)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:SSFN {param}')

	def get_ms_frames(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:MSFRames \n
		Snippet: value: int = driver.configure.uplinkLogging.get_ms_frames() \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . \n
			:return: meas_sub_frames: Volume of measured consecutive UL HS-DPCCH/E-DPCCH/DPCCH subframes Range: 15 to 10E+3
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:MSFRames?')
		return Conversions.str_to_int(response)

	def set_ms_frames(self, meas_sub_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:MSFRames \n
		Snippet: driver.configure.uplinkLogging.set_ms_frames(meas_sub_frames = 1) \n
		Defines the number of subframes to be measured per measurement cycle (statistics cycle) . \n
			:param meas_sub_frames: Volume of measured consecutive UL HS-DPCCH/E-DPCCH/DPCCH subframes Range: 15 to 10E+3
		"""
		param = Conversions.decimal_value_to_str(meas_sub_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:MSFRames {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.uplinkLogging.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames to define the number of
		subframes to be measured per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ULLogging:REPetition \n
		Snippet: driver.configure.uplinkLogging.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.UplinkLogging.msFrames to define the number of
		subframes to be measured per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ULLogging:REPetition {param}')
