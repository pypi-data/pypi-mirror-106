from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Request:
	"""Request commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("request", core, parent)

	def get_imei(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:IMEI \n
		Snippet: value: bool = driver.configure.cell.request.get_imei() \n
		Enables or disables the request of the IMEI from the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:IMEI?')
		return Conversions.str_to_bool(response)

	def set_imei(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:IMEI \n
		Snippet: driver.configure.cell.request.set_imei(enable = False) \n
		Enables or disables the request of the IMEI from the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:IMEI {param}')

	def get_adetach(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:ADETach \n
		Snippet: value: bool = driver.configure.cell.request.get_adetach() \n
		Enables or disables the CS registration and PS attach procedure. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:ADETach?')
		return Conversions.str_to_bool(response)

	def set_adetach(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:ADETach \n
		Snippet: driver.configure.cell.request.set_adetach(enable = False) \n
		Enables or disables the CS registration and PS attach procedure. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:ADETach {param}')

	def get_rcur(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:RCUR \n
		Snippet: value: bool = driver.configure.cell.request.get_rcur() \n
		Enables or disables the request of the radio capability update from the UE. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:RCUR?')
		return Conversions.str_to_bool(response)

	def set_rcur(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:REQuest:RCUR \n
		Snippet: driver.configure.cell.request.set_rcur(enable = False) \n
		Enables or disables the request of the radio capability update from the UE. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:REQuest:RCUR {param}')
