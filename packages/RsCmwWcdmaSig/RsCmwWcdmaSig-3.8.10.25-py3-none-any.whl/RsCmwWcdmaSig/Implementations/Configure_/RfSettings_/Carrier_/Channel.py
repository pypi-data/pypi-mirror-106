from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channel", core, parent)

	def get_uplink(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:CHANnel:UL \n
		Snippet: value: int = driver.configure.rfSettings.carrier.channel.get_uplink() \n
		Selects the UL channel number. The channel number must be valid for the current operating band. For dependencies, see
		'Operating Bands'. The related DL channel number is calculated and set automatically. \n
			:return: channel_number: Range: depends on operating band
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:CHANnel:UL?')
		return Conversions.str_to_int(response)

	def set_uplink(self, channel_number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:CHANnel:UL \n
		Snippet: driver.configure.rfSettings.carrier.channel.set_uplink(channel_number = 1) \n
		Selects the UL channel number. The channel number must be valid for the current operating band. For dependencies, see
		'Operating Bands'. The related DL channel number is calculated and set automatically. \n
			:param channel_number: Range: depends on operating band
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:CHANnel:UL {param}')

	def get_downlink(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:CHANnel:DL \n
		Snippet: value: int = driver.configure.rfSettings.carrier.channel.get_downlink() \n
		Selects the DL channel number. The channel number must be valid for the current operating band, for dependencies see
		'Operating Bands'. The related UL channel number is calculated and set automatically. For multi-carrier scenarios, the
		channel numbers of the other carriers are calculated and set as well. \n
			:return: channel_number: Range: depends on operating band
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:CHANnel:DL?')
		return Conversions.str_to_int(response)

	def set_downlink(self, channel_number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:CHANnel:DL \n
		Snippet: driver.configure.rfSettings.carrier.channel.set_downlink(channel_number = 1) \n
		Selects the DL channel number. The channel number must be valid for the current operating band, for dependencies see
		'Operating Bands'. The related UL channel number is calculated and set automatically. For multi-carrier scenarios, the
		channel numbers of the other carriers are calculated and set as well. \n
			:param channel_number: Range: depends on operating band
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:CHANnel:DL {param}')
