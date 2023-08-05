from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoPower:
	"""CoPower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("coPower", core, parent)

	def get_total(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:COPower:TOTal \n
		Snippet: value: float = driver.configure.rfSettings.coPower.get_total() \n
		Sets the total base level of the generator. For multi-carrier operation, this value is the sum of all carrier powers. If
		you modify the total power level, all carrier powers are increased/decreased by the same amount so that the new total
		power level is reached. The allowed value range per carrier can be calculated as follows: Range (Base Level) = Range
		(Output Power) - External Attenuation - Insertion Loss + Baseband Level Range (Output Power) = -130 dBm to -5 dBm (RFx
		COM) or -120 dBm to 3 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. Insertion loss is only
		relevant for internal fading. Baseband level only relevant for external fading. \n
			:return: total_out_ch_pwr: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:COPower:TOTal?')
		return Conversions.str_to_float(response)

	def set_total(self, total_out_ch_pwr: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:COPower:TOTal \n
		Snippet: driver.configure.rfSettings.coPower.set_total(total_out_ch_pwr = 1.0) \n
		Sets the total base level of the generator. For multi-carrier operation, this value is the sum of all carrier powers. If
		you modify the total power level, all carrier powers are increased/decreased by the same amount so that the new total
		power level is reached. The allowed value range per carrier can be calculated as follows: Range (Base Level) = Range
		(Output Power) - External Attenuation - Insertion Loss + Baseband Level Range (Output Power) = -130 dBm to -5 dBm (RFx
		COM) or -120 dBm to 3 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. Insertion loss is only
		relevant for internal fading. Baseband level only relevant for external fading. \n
			:param total_out_ch_pwr: Range: see above , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(total_out_ch_pwr)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:COPower:TOTal {param}')
