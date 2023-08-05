from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etws:
	"""Etws commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etws", core, parent)

	def get_alert(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ETWS:ALERt \n
		Snippet: value: bool = driver.configure.cbs.message.etws.get_alert() \n
		Deactivates / activates earthquake and tsunami warning system alerting. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ETWS:ALERt?')
		return Conversions.str_to_bool(response)

	def set_alert(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ETWS:ALERt \n
		Snippet: driver.configure.cbs.message.etws.set_alert(enable = False) \n
		Deactivates / activates earthquake and tsunami warning system alerting. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ETWS:ALERt {param}')

	def get_popup(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ETWS:POPup \n
		Snippet: value: bool = driver.configure.cbs.message.etws.get_popup() \n
		Deactivates / activates earthquake and tsunami warning popup on display. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ETWS:POPup?')
		return Conversions.str_to_bool(response)

	def set_popup(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ETWS:POPup \n
		Snippet: driver.configure.cbs.message.etws.set_popup(enable = False) \n
		Deactivates / activates earthquake and tsunami warning popup on display. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ETWS:POPup {param}')
