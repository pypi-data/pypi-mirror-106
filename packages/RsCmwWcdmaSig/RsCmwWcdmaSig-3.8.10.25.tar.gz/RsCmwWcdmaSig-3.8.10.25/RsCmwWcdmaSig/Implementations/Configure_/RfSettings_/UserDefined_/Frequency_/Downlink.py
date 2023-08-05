from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	def get_minimum(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:DL:MINimum \n
		Snippet: value: float = driver.configure.rfSettings.userDefined.frequency.downlink.get_minimum() \n
		Specifies the minimum value for downlink frequencies within a user-defined band. \n
			:return: frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:DL:MINimum?')
		return Conversions.str_to_float(response)

	def set_minimum(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:DL:MINimum \n
		Snippet: driver.configure.rfSettings.userDefined.frequency.downlink.set_minimum(frequency = 1.0) \n
		Specifies the minimum value for downlink frequencies within a user-defined band. \n
			:param frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:DL:MINimum {param}')

	def get_maximum(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:FREQuency:DL:MAXimum \n
		Snippet: value: float = driver.configure.rfSettings.userDefined.frequency.downlink.get_maximum() \n
		Specifies the maximum value for downlink frequencies within a user-defined band. \n
			:return: frequency: Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:FREQuency:DL:MAXimum?')
		return Conversions.str_to_float(response)
