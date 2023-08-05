from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:TOUT \n
		Snippet: value: float = driver.configure.throughput.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:TOUT \n
		Snippet: driver.configure.throughput.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:TOUT {param}')

	def get_update(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:UPDate \n
		Snippet: value: float = driver.configure.throughput.get_update() \n
		Configures the time interval used to derive a single throughput result. \n
			:return: interval: Range: 0.24 s / 120 subframes to 2.4 s / 1200 subframes, Unit: subframe
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:UPDate?')
		return Conversions.str_to_float(response)

	def set_update(self, interval: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:UPDate \n
		Snippet: driver.configure.throughput.set_update(interval = 1.0) \n
		Configures the time interval used to derive a single throughput result. \n
			:param interval: Range: 0.24 s / 120 subframes to 2.4 s / 1200 subframes, Unit: subframe
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:UPDate {param}')

	def get_window(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:WINDow \n
		Snippet: value: float = driver.configure.throughput.get_window() \n
		Specifies the duration of a single-shot measurement, i.e. the time interval covered by a throughput result trace.
		The value is internally rounded up to the next integer multiple of the time interval used to calculate a single result
		(see method RsCmwWcdmaSig.Configure.Throughput.update) . \n
			:return: size: Range: 9.6 s / 48000 subframes to 240 s / 120000 subframes, Unit: subframe
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:WINDow?')
		return Conversions.str_to_float(response)

	def set_window(self, size: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:WINDow \n
		Snippet: driver.configure.throughput.set_window(size = 1.0) \n
		Specifies the duration of a single-shot measurement, i.e. the time interval covered by a throughput result trace.
		The value is internally rounded up to the next integer multiple of the time interval used to calculate a single result
		(see method RsCmwWcdmaSig.Configure.Throughput.update) . \n
			:param size: Range: 9.6 s / 48000 subframes to 240 s / 120000 subframes, Unit: subframe
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:WINDow {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.throughput.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Throughput.window to configure the duration of
		a single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:THRoughput:REPetition \n
		Snippet: driver.configure.throughput.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwWcdmaSig.Configure.Throughput.window to configure the duration of
		a single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:THRoughput:REPetition {param}')
