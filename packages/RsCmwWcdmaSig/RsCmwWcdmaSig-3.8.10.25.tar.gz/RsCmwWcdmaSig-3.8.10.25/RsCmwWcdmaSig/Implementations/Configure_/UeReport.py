from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReport:
	"""UeReport commands group definition. 7 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueReport", core, parent)

	@property
	def ccell(self):
		"""ccell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccell'):
			from .UeReport_.Ccell import Ccell
			self._ccell = Ccell(self._core, self._base)
		return self._ccell

	@property
	def ncell(self):
		"""ncell commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncell'):
			from .UeReport_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:ENABle \n
		Snippet: value: bool = driver.configure.ueReport.get_enable() \n
		Enables or disables the UE measurement report completely. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:ENABle \n
		Snippet: driver.configure.ueReport.set_enable(enable = False) \n
		Enables or disables the UE measurement report completely. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UEReport:ENABle {param}')

	def get_rinterval(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:RINTerval \n
		Snippet: value: float = driver.configure.ueReport.get_rinterval() \n
		Sets the interval between two consecutive measurement report messages. \n
			:return: interval: Range: 0.25 s to 64 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:RINTerval?')
		return Conversions.str_to_float(response)

	def set_rinterval(self, interval: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:RINTerval \n
		Snippet: driver.configure.ueReport.set_rinterval(interval = 1.0) \n
		Sets the interval between two consecutive measurement report messages. \n
			:param interval: Range: 0.25 s to 64 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UEReport:RINTerval {param}')

	def clone(self) -> 'UeReport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
