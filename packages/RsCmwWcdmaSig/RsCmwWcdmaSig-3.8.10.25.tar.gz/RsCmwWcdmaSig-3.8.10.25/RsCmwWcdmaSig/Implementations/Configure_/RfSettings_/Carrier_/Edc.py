from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edc:
	"""Edc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("edc", core, parent)

	def get_input_py(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EDC:INPut \n
		Snippet: value: float = driver.configure.rfSettings.carrier.edc.get_input_py() \n
		No command help available \n
			:return: ext_delay: Range: 0 s to 20E-6 s
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EDC:INPut?')
		return Conversions.str_to_float(response)

	def set_input_py(self, ext_delay: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EDC:INPut \n
		Snippet: driver.configure.rfSettings.carrier.edc.set_input_py(ext_delay = 1.0) \n
		No command help available \n
			:param ext_delay: Range: 0 s to 20E-6 s
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(ext_delay)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EDC:INPut {param}')

	def get_output(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EDC:OUTPut \n
		Snippet: value: float = driver.configure.rfSettings.carrier.edc.get_output() \n
		No command help available \n
			:return: ext_delay: Range: 0 s to 20E-6 s
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EDC:OUTPut?')
		return Conversions.str_to_float(response)

	def set_output(self, ext_delay: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:EDC:OUTPut \n
		Snippet: driver.configure.rfSettings.carrier.edc.set_output(ext_delay = 1.0) \n
		No command help available \n
			:param ext_delay: Range: 0 s to 20E-6 s
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(ext_delay)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:EDC:OUTPut {param}')
