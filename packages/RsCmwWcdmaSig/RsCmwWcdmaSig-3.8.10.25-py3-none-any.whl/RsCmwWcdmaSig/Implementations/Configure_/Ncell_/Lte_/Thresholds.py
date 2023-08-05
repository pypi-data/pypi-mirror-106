from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	def get_high(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:LTE:THResholds:HIGH \n
		Snippet: value: int = driver.configure.ncell.lte.thresholds.get_high() \n
		Configures the reselection threshold value 'threshXhigh' for LTE neighbor cells. \n
			:return: high: Range: 0 to 31
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:NCELl:LTE:THResholds:HIGH?')
		return Conversions.str_to_int(response)

	def set_high(self, high: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:LTE:THResholds:HIGH \n
		Snippet: driver.configure.ncell.lte.thresholds.set_high(high = 1) \n
		Configures the reselection threshold value 'threshXhigh' for LTE neighbor cells. \n
			:param high: Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(high)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:LTE:THResholds:HIGH {param}')
