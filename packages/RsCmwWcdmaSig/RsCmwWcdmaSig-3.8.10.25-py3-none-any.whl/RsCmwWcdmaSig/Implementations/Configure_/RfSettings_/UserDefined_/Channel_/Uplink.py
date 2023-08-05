from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	def get_minimum(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:CHANnel:UL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.userDefined.channel.uplink.get_minimum() \n
		Specifies the minimum value for uplink channel number within a user-defined band. \n
			:return: channel: Range: 0 Ch to 16.383E+3 Ch
		"""
		response = self._core.io.query_str_with_opc('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:CHANnel:UL:MINimum?')
		return Conversions.str_to_int(response)

	def set_minimum(self, channel: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:CHANnel:UL:MINimum \n
		Snippet: driver.configure.rfSettings.userDefined.channel.uplink.set_minimum(channel = 1) \n
		Specifies the minimum value for uplink channel number within a user-defined band. \n
			:param channel: Range: 0 Ch to 16.383E+3 Ch
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:CHANnel:UL:MINimum {param}')

	def get_maximum(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:CHANnel:UL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.userDefined.channel.uplink.get_maximum() \n
		Specifies the maximum value for uplink channel number within a user-defined band. \n
			:return: channel: Range: 0 Ch to 16.383E+3 Ch
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:CHANnel:UL:MAXimum?')
		return Conversions.str_to_int(response)
