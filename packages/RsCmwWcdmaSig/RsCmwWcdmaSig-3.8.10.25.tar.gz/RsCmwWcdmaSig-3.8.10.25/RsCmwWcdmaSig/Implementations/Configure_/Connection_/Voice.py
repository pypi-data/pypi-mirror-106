from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Voice:
	"""Voice commands group definition. 7 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("voice", core, parent)

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Voice_.Delay import Delay
			self._delay = Delay(self._core, self._base)
		return self._delay

	@property
	def amr(self):
		"""amr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_amr'):
			from .Voice_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	def get_dtx(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:DTX \n
		Snippet: value: bool = driver.configure.connection.voice.get_dtx() \n
		Enables/disables speech DTX indication in downlink. \n
			:return: speech_dtx_dl: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:DTX?')
		return Conversions.str_to_bool(response)

	def set_dtx(self, speech_dtx_dl: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:DTX \n
		Snippet: driver.configure.connection.voice.set_dtx(speech_dtx_dl = False) \n
		Enables/disables speech DTX indication in downlink. \n
			:param speech_dtx_dl: OFF | ON
		"""
		param = Conversions.bool_to_str(speech_dtx_dl)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:DTX {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.VoiceSource:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:SOURce \n
		Snippet: value: enums.VoiceSource = driver.configure.connection.voice.get_source() \n
		Selects the voice connection path. \n
			:return: source: LOOPback | SPEech LOOPback: voice stream looped back in the R&S CMW SPEech: connection to the speech codec board
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.VoiceSource)

	def set_source(self, source: enums.VoiceSource) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:SOURce \n
		Snippet: driver.configure.connection.voice.set_source(source = enums.VoiceSource.LOOPback) \n
		Selects the voice connection path. \n
			:param source: LOOPback | SPEech LOOPback: voice stream looped back in the R&S CMW SPEech: connection to the speech codec board
		"""
		param = Conversions.enum_scalar_to_str(source, enums.VoiceSource)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:SOURce {param}')

	# noinspection PyTypeChecker
	def get_codec(self) -> enums.VoiceCodec:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:CODec \n
		Snippet: value: enums.VoiceCodec = driver.configure.connection.voice.get_codec() \n
		Selects the AMR voice codec type to be used: narrowband or wideband. \n
			:return: codec: NB | WB NB: narrowband WB: wideband
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:CODec?')
		return Conversions.str_to_scalar_enum(response, enums.VoiceCodec)

	def set_codec(self, codec: enums.VoiceCodec) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:CODec \n
		Snippet: driver.configure.connection.voice.set_codec(codec = enums.VoiceCodec.NB) \n
		Selects the AMR voice codec type to be used: narrowband or wideband. \n
			:param codec: NB | WB NB: narrowband WB: wideband
		"""
		param = Conversions.enum_scalar_to_str(codec, enums.VoiceCodec)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:CODec {param}')

	def get_tfci(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:TFCI \n
		Snippet: value: bool = driver.configure.connection.voice.get_tfci() \n
		Enables/disables the downlink signaling of TFCI for voice connections. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:TFCI?')
		return Conversions.str_to_bool(response)

	def set_tfci(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VOICe:TFCI \n
		Snippet: driver.configure.connection.voice.set_tfci(enable = False) \n
		Enables/disables the downlink signaling of TFCI for voice connections. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VOICe:TFCI {param}')

	def clone(self) -> 'Voice':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Voice(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
