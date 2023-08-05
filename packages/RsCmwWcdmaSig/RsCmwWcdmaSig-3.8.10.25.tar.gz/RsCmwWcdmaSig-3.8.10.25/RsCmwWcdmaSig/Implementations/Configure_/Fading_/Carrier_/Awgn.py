from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("awgn", core, parent)

	def get_noise(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:AWGN:NOISe \n
		Snippet: value: float = driver.configure.fading.carrier.awgn.get_noise() \n
		Sets the total AWGN level within the channel bandwidth, applicable to AWGN inserted via the internal fading module. For
		multi-carrier scenarios, the same settings are applied to all carriers. Thus it is sufficient to configure one carrier. \n
			:return: noise: Range: depends on connector, external attenuation, base level and insertion loss , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:AWGN:NOISe?')
		return Conversions.str_to_float(response)

	def set_noise(self, noise: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:AWGN:NOISe \n
		Snippet: driver.configure.fading.carrier.awgn.set_noise(noise = 1.0) \n
		Sets the total AWGN level within the channel bandwidth, applicable to AWGN inserted via the internal fading module. For
		multi-carrier scenarios, the same settings are applied to all carriers. Thus it is sufficient to configure one carrier. \n
			:param noise: Range: depends on connector, external attenuation, base level and insertion loss , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(noise)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:AWGN:NOISe {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:AWGN:ENABle \n
		Snippet: value: bool = driver.configure.fading.carrier.awgn.get_enable() \n
		Enables or disables AWGN insertion via the fading module. For multi-carrier scenarios, the same settings are applied to
		all carriers. Thus it is sufficient to configure one carrier. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:AWGN:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:AWGN:ENABle \n
		Snippet: driver.configure.fading.carrier.awgn.set_enable(enable = False) \n
		Enables or disables AWGN insertion via the fading module. For multi-carrier scenarios, the same settings are applied to
		all carriers. Thus it is sufficient to configure one carrier. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:AWGN:ENABle {param}')

	def get_sn_ratio(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.fading.carrier.awgn.get_sn_ratio() \n
		Queries the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:return: ratio: Range: -50 dB to 40 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:AWGN:SNRatio?')
		return Conversions.str_to_float(response)
