from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	def get_minimum(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:UL:MINimum \n
		Snippet: value: float = driver.configure.rfSettings.userDefined.frequency.uplink.get_minimum() \n
		Specifies the minimum value for uplink frequencies within a user-defined band. \n
			:return: frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:UL:MINimum?')
		return Conversions.str_to_float(response)

	def set_minimum(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:UL:MINimum \n
		Snippet: driver.configure.rfSettings.userDefined.frequency.uplink.set_minimum(frequency = 1.0) \n
		Specifies the minimum value for uplink frequencies within a user-defined band. \n
			:param frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:UL:MINimum {param}')

	def get_maximum(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:UL:MAXimum \n
		Snippet: value: float = driver.configure.rfSettings.userDefined.frequency.uplink.get_maximum() \n
		Specifies the maximum value for uplink frequencies within a user-defined band. \n
			:return: frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:UL:MAXimum?')
		return Conversions.str_to_float(response)
