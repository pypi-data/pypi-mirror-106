from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcontrol:
	"""Pcontrol commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcontrol", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PowerControlMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:MODE \n
		Snippet: value: enums.PowerControlMode = driver.configure.downlink.pcontrol.get_mode() \n
		Selects the frequency of power adjustment in downlink. \n
			:return: mode: M0 | M1 | ON | OFF Mode 0, mode 1, additional ON / OFF enables or disables power control in downlink.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PowerControlMode)

	def set_mode(self, mode: enums.PowerControlMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:MODE \n
		Snippet: driver.configure.downlink.pcontrol.set_mode(mode = enums.PowerControlMode.M0) \n
		Selects the frequency of power adjustment in downlink. \n
			:param mode: M0 | M1 | ON | OFF Mode 0, mode 1, additional ON / OFF enables or disables power control in downlink.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PowerControlMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:MODE {param}')

	def get_step(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:STEP \n
		Snippet: value: float = driver.configure.downlink.pcontrol.get_step() \n
		Specifies the step size of downlink power control. \n
			:return: stepsize: Range: 0.5 dB to 2 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:STEP?')
		return Conversions.str_to_float(response)

	def set_step(self, stepsize: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:STEP \n
		Snippet: driver.configure.downlink.pcontrol.set_step(stepsize = 1.0) \n
		Specifies the step size of downlink power control. \n
			:param stepsize: Range: 0.5 dB to 2 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:STEP {param}')

	def get_dt_quality(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:DTQuality \n
		Snippet: value: float = driver.configure.downlink.pcontrol.get_dt_quality() \n
		Specifies a signaled target BLER value. \n
			:return: error_rate: Range: 0.01 % to 20 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:DTQuality?')
		return Conversions.str_to_float(response)

	def set_dt_quality(self, error_rate: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:DTQuality \n
		Snippet: driver.configure.downlink.pcontrol.set_dt_quality(error_rate = 1.0) \n
		Specifies a signaled target BLER value. \n
			:param error_rate: Range: 0.01 % to 20 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(error_rate)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:DTQuality {param}')

	def get_fterate(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:FTERate \n
		Snippet: value: float = driver.configure.downlink.pcontrol.get_fterate() \n
		Specifies a signaled target TPC error rate value for tests using the F-DPCH. \n
			:return: error_rate: Range: 1 % to 10 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:FTERate?')
		return Conversions.str_to_float(response)

	def set_fterate(self, error_rate: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:PCONtrol:FTERate \n
		Snippet: driver.configure.downlink.pcontrol.set_fterate(error_rate = 1.0) \n
		Specifies a signaled target TPC error rate value for tests using the F-DPCH. \n
			:param error_rate: Range: 1 % to 10 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(error_rate)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:PCONtrol:FTERate {param}')
