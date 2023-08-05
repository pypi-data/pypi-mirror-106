from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hcqi:
	"""Hcqi commands group definition. 9 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hcqi", core, parent)

	@property
	def cqi(self):
		"""cqi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cqi'):
			from .Hcqi_.Cqi import Cqi
			self._cqi = Cqi(self._core, self._base)
		return self._cqi

	@property
	def bler(self):
		"""bler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bler'):
			from .Hcqi_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def limit(self):
		"""limit commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Hcqi_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:TOUT \n
		Snippet: value: float = driver.configure.hcqi.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:TOUT \n
		Snippet: driver.configure.hcqi.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HCQI:TOUT {param}')

	# noinspection PyTypeChecker
	def get_tcase(self) -> enums.TestCase:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:TCASe \n
		Snippet: value: enums.TestCase = driver.configure.hcqi.get_tcase() \n
		Selects either AWGN or fading test case. \n
			:return: test_case: AWGN | FADing
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:TCASe?')
		return Conversions.str_to_scalar_enum(response, enums.TestCase)

	def set_tcase(self, test_case: enums.TestCase) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:TCASe \n
		Snippet: driver.configure.hcqi.set_tcase(test_case = enums.TestCase.AWGN) \n
		Selects either AWGN or fading test case. \n
			:param test_case: AWGN | FADing
		"""
		param = Conversions.enum_scalar_to_str(test_case, enums.TestCase)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HCQI:TCASe {param}')

	def clone(self) -> 'Hcqi':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hcqi(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
