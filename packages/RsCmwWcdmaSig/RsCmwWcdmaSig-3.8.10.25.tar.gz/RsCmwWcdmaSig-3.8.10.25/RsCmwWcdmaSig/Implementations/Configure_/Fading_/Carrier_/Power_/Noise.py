from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("noise", core, parent)

	def get_total(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:POWer:NOISe:TOTal \n
		Snippet: value: float = driver.configure.fading.carrier.power.noise.get_total() \n
		Queries the total noise power. \n
			:return: noise_power: Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:POWer:NOISe:TOTal?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:POWer:NOISe \n
		Snippet: value: float = driver.configure.fading.carrier.power.noise.get_value() \n
		Queries the calculated noise power on the downlink carrier. \n
			:return: noise_power: Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:POWer:NOISe?')
		return Conversions.str_to_float(response)
