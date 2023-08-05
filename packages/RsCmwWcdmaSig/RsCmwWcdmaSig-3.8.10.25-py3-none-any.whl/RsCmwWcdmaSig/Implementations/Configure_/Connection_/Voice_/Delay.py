from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("delay", core, parent)

	def get_loopback(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:DELay:LOOPback \n
		Snippet: value: float = driver.configure.connection.voice.delay.get_loopback() \n
		Defines the time that the R&S CMW waits before it loops back the received data in the loopback voice connection. \n
			:return: delay: Range: 0 s to 10 s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:DELay:LOOPback?')
		return Conversions.str_to_float(response)

	def set_loopback(self, delay: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:DELay:LOOPback \n
		Snippet: driver.configure.connection.voice.delay.set_loopback(delay = 1.0) \n
		Defines the time that the R&S CMW waits before it loops back the received data in the loopback voice connection. \n
			:param delay: Range: 0 s to 10 s
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:DELay:LOOPback {param}')
