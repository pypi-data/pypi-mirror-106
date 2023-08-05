from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amr:
	"""Amr commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("amr", core, parent)

	# noinspection PyTypeChecker
	def get_narrow(self) -> enums.AmrCodecModeNarrow:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:AMR:NARRow \n
		Snippet: value: enums.AmrCodecModeNarrow = driver.configure.connection.voice.amr.get_narrow() \n
		Selects the mode of the NB AMR codec. The basic modes support one fixed bit-rate. Mode M supports several bit-rates. \n
			:return: rate: A | B | C | D | E | F | G | H | M A: 12.2 kbps B: 10.2 kbps C: 7.95 kbps D: 7.4 kbps E: 6.7 kbps F: 5.9 kbps G: 5.15 kbps H: 4.75 kbps M: A + C + F + H
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:AMR:NARRow?')
		return Conversions.str_to_scalar_enum(response, enums.AmrCodecModeNarrow)

	def set_narrow(self, rate: enums.AmrCodecModeNarrow) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:AMR:NARRow \n
		Snippet: driver.configure.connection.voice.amr.set_narrow(rate = enums.AmrCodecModeNarrow.A) \n
		Selects the mode of the NB AMR codec. The basic modes support one fixed bit-rate. Mode M supports several bit-rates. \n
			:param rate: A | B | C | D | E | F | G | H | M A: 12.2 kbps B: 10.2 kbps C: 7.95 kbps D: 7.4 kbps E: 6.7 kbps F: 5.9 kbps G: 5.15 kbps H: 4.75 kbps M: A + C + F + H
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.AmrCodecModeNarrow)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:AMR:NARRow {param}')

	# noinspection PyTypeChecker
	def get_wide(self) -> enums.AmrCodecModeWide:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:AMR:WIDE \n
		Snippet: value: enums.AmrCodecModeWide = driver.configure.connection.voice.amr.get_wide() \n
		Selects the mode of the WB AMR codec. The basic modes support one fixed bit-rate. Mode M supports several bit-rates. \n
			:return: rate: A | B | C | D | E | F | G | H | I | M | M1 | M2 A: 23.85 kbps B: 23.05 kbps C: 19.85 kbps D: 18.25 kbps E: 15.85 kbps F: 14.25 kbps G: 12.65 kbps H: 8.85 kbps I: 6.60 kbps M: G + H + I M1: E + G + H + I M2: A + G + H + I
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:AMR:WIDE?')
		return Conversions.str_to_scalar_enum(response, enums.AmrCodecModeWide)

	def set_wide(self, rate: enums.AmrCodecModeWide) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:AMR:WIDE \n
		Snippet: driver.configure.connection.voice.amr.set_wide(rate = enums.AmrCodecModeWide.A) \n
		Selects the mode of the WB AMR codec. The basic modes support one fixed bit-rate. Mode M supports several bit-rates. \n
			:param rate: A | B | C | D | E | F | G | H | I | M | M1 | M2 A: 23.85 kbps B: 23.05 kbps C: 19.85 kbps D: 18.25 kbps E: 15.85 kbps F: 14.25 kbps G: 12.65 kbps H: 8.85 kbps I: 6.60 kbps M: G + H + I M1: E + G + H + I M2: A + G + H + I
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.AmrCodecModeWide)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:AMR:WIDE {param}')
