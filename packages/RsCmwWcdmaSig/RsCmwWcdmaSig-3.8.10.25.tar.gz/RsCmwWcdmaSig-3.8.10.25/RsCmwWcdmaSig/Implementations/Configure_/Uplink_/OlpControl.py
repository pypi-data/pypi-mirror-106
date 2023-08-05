from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControl:
	"""OlpControl commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("olpControl", core, parent)

	def get_interference(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:OLPControl:INTerference \n
		Snippet: value: float = driver.configure.uplink.olpControl.get_interference() \n
		Estimated UL interference contained in system information block type 7. \n
			:return: interference: Range: -110 dBm to -70 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:OLPControl:INTerference?')
		return Conversions.str_to_float(response)

	def set_interference(self, interference: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:OLPControl:INTerference \n
		Snippet: driver.configure.uplink.olpControl.set_interference(interference = 1.0) \n
		Estimated UL interference contained in system information block type 7. \n
			:param interference: Range: -110 dBm to -70 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(interference)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:OLPControl:INTerference {param}')

	def get_cvalue(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:OLPControl:CVALue \n
		Snippet: value: float = driver.configure.uplink.olpControl.get_cvalue() \n
		Sets the constant offset value for the initial preamble power. \n
			:return: con_offset_value: Range: -35 dB to -10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:OLPControl:CVALue?')
		return Conversions.str_to_float(response)

	def set_cvalue(self, con_offset_value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:OLPControl:CVALue \n
		Snippet: driver.configure.uplink.olpControl.set_cvalue(con_offset_value = 1.0) \n
		Sets the constant offset value for the initial preamble power. \n
			:param con_offset_value: Range: -35 dB to -10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(con_offset_value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:OLPControl:CVALue {param}')
