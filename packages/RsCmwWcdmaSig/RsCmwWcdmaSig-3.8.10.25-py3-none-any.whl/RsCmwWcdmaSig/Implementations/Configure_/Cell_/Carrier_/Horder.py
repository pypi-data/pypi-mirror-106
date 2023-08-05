from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Horder:
	"""Horder commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("horder", core, parent)

	def get_downlink(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HORDer:DL \n
		Snippet: value: bool = driver.configure.cell.carrier.horder.get_downlink() \n
		Preconfigures the activation of an additional DL/UL carrier for the next HS-SCCH order type 1 in multi-carrier scenarios. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HORDer:DL?')
		return Conversions.str_to_bool(response)

	def set_downlink(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HORDer:DL \n
		Snippet: driver.configure.cell.carrier.horder.set_downlink(enable = False) \n
		Preconfigures the activation of an additional DL/UL carrier for the next HS-SCCH order type 1 in multi-carrier scenarios. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HORDer:DL {param}')

	def get_uplink(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HORDer:UL \n
		Snippet: value: bool = driver.configure.cell.carrier.horder.get_uplink() \n
		Preconfigures the activation of an additional DL/UL carrier for the next HS-SCCH order type 1 in multi-carrier scenarios. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HORDer:UL?')
		return Conversions.str_to_bool(response)

	def set_uplink(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HORDer:UL \n
		Snippet: driver.configure.cell.carrier.horder.set_uplink(enable = False) \n
		Preconfigures the activation of an additional DL/UL carrier for the next HS-SCCH order type 1 in multi-carrier scenarios. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HORDer:UL {param}')
