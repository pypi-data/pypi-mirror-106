from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def get_uplink(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FREQuency:UL \n
		Snippet: value: float = driver.configure.rfSettings.carrier.frequency.get_uplink() \n
		Selects the UL carrier center frequency. The frequency must correspond to a channel valid for the current operating band.
		For dependencies, see 'Operating Bands'. The related DL frequency is calculated and set automatically. \n
			:return: frequency: Range: depends on operating band , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FREQuency:UL?')
		return Conversions.str_to_float(response)

	def set_uplink(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FREQuency:UL \n
		Snippet: driver.configure.rfSettings.carrier.frequency.set_uplink(frequency = 1.0) \n
		Selects the UL carrier center frequency. The frequency must correspond to a channel valid for the current operating band.
		For dependencies, see 'Operating Bands'. The related DL frequency is calculated and set automatically. \n
			:param frequency: Range: depends on operating band , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FREQuency:UL {param}')

	def get_downlink(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FREQuency:DL \n
		Snippet: value: float = driver.configure.rfSettings.carrier.frequency.get_downlink() \n
		Selects the DL carrier center frequency. The frequency must correspond to a channel valid for the current operating band,
		for dependencies see 'Operating Bands'. The related UL frequency is calculated and set automatically. For dual carrier,
		the frequency of the other carrier is calculated and set as well. \n
			:return: frequency: Range: depends on operating band , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FREQuency:DL?')
		return Conversions.str_to_float(response)

	def set_downlink(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FREQuency:DL \n
		Snippet: driver.configure.rfSettings.carrier.frequency.set_downlink(frequency = 1.0) \n
		Selects the DL carrier center frequency. The frequency must correspond to a channel valid for the current operating band,
		for dependencies see 'Operating Bands'. The related UL frequency is calculated and set automatically. For dual carrier,
		the frequency of the other carrier is calculated and set as well. \n
			:param frequency: Range: depends on operating band , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FREQuency:DL {param}')
