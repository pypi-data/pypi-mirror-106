from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eattenuation:
	"""Eattenuation commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eattenuation", core, parent)

	def get_input_py(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EATTenuation:INPut \n
		Snippet: value: float = driver.configure.rfSettings.carrier.eattenuation.get_input_py() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF input connector. \n
			:return: ext_attenuation: Range: -50 dB to 90 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EATTenuation:INPut?')
		return Conversions.str_to_float(response)

	def set_input_py(self, ext_attenuation: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EATTenuation:INPut \n
		Snippet: driver.configure.rfSettings.carrier.eattenuation.set_input_py(ext_attenuation = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF input connector. \n
			:param ext_attenuation: Range: -50 dB to 90 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EATTenuation:INPut {param}')

	def get_output(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EATTenuation:OUTPut \n
		Snippet: value: float = driver.configure.rfSettings.carrier.eattenuation.get_output() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector. \n
			:return: ext_attenuation: Range: -50 dB to 90 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EATTenuation:OUTPut?')
		return Conversions.str_to_float(response)

	def set_output(self, ext_attenuation: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EATTenuation:OUTPut \n
		Snippet: driver.configure.rfSettings.carrier.eattenuation.set_output(ext_attenuation = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output connector. \n
			:param ext_attenuation: Range: -50 dB to 90 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(ext_attenuation)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EATTenuation:OUTPut {param}')
