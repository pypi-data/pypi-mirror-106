from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("preamble", core, parent)

	def get_aich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:AICH \n
		Snippet: value: int = driver.configure.uplink.prach.preamble.get_aich() \n
		Specifies the number of preambles to be received before the instrument transmits the AICH. \n
			:return: preambles: Range: 1 to 12
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:AICH?')
		return Conversions.str_to_int(response)

	def set_aich(self, preambles: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:AICH \n
		Snippet: driver.configure.uplink.prach.preamble.set_aich(preambles = 1) \n
		Specifies the number of preambles to be received before the instrument transmits the AICH. \n
			:param preambles: Range: 1 to 12
		"""
		param = Conversions.decimal_value_to_str(preambles)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:AICH {param}')

	def get_ssize(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SSIZe \n
		Snippet: value: int = driver.configure.uplink.prach.preamble.get_ssize() \n
		Specifies the transmit power difference between two consecutive preambles. \n
			:return: stepsize: Range: 1 dB to 8 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SSIZe?')
		return Conversions.str_to_int(response)

	def set_ssize(self, stepsize: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SSIZe \n
		Snippet: driver.configure.uplink.prach.preamble.set_ssize(stepsize = 1) \n
		Specifies the transmit power difference between two consecutive preambles. \n
			:param stepsize: Range: 1 dB to 8 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SSIZe {param}')

	def get_sub_channels(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SUBChannels \n
		Snippet: value: float = driver.configure.uplink.prach.preamble.get_sub_channels() \n
		Specifies which of the 12 PRACH subchannels are available. The information is coded in a 12-bit number where the bits
		from left to right indicate the availability of subchannel 11 to subchannel 0 (0=not available, 1=available) .
		The default format is decimal, but you can also enter binary numbers (#B000000000000 to #B111111111111) . \n
			:return: sub_channels: Range: #B000000000000 to #B111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SUBChannels?')
		return Conversions.str_to_float(response)

	def set_sub_channels(self, sub_channels: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SUBChannels \n
		Snippet: driver.configure.uplink.prach.preamble.set_sub_channels(sub_channels = 1.0) \n
		Specifies which of the 12 PRACH subchannels are available. The information is coded in a 12-bit number where the bits
		from left to right indicate the availability of subchannel 11 to subchannel 0 (0=not available, 1=available) .
		The default format is decimal, but you can also enter binary numbers (#B000000000000 to #B111111111111) . \n
			:param sub_channels: Range: #B000000000000 to #B111111111111
		"""
		param = Conversions.decimal_value_to_str(sub_channels)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SUBChannels {param}')

	def get_mcycles(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:MCYCles \n
		Snippet: value: int = driver.configure.uplink.prach.preamble.get_mcycles() \n
		Specifies the maximum number of times the preamble cycle is repeated. \n
			:return: max_cycles: Range: 1 to 32
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:MCYCles?')
		return Conversions.str_to_int(response)

	def set_mcycles(self, max_cycles: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:MCYCles \n
		Snippet: driver.configure.uplink.prach.preamble.set_mcycles(max_cycles = 1) \n
		Specifies the maximum number of times the preamble cycle is repeated. \n
			:param max_cycles: Range: 1 to 32
		"""
		param = Conversions.decimal_value_to_str(max_cycles)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:MCYCles {param}')

	def get_mretrans(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:MRETrans \n
		Snippet: value: int = driver.configure.uplink.prach.preamble.get_mretrans() \n
		Sets the maximum number of preambles to be transmitted before a single preamble cycle is terminated. \n
			:return: retransmission: Range: 1 to 64
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:MRETrans?')
		return Conversions.str_to_int(response)

	def set_mretrans(self, retransmission: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:MRETrans \n
		Snippet: driver.configure.uplink.prach.preamble.set_mretrans(retransmission = 1) \n
		Sets the maximum number of preambles to be transmitted before a single preamble cycle is terminated. \n
			:param retransmission: Range: 1 to 64
		"""
		param = Conversions.decimal_value_to_str(retransmission)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:MRETrans {param}')

	def get_signature(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SIGNature \n
		Snippet: value: float = driver.configure.uplink.prach.preamble.get_signature() \n
		Specifies which of the 16 signatures defined by 3GPP TS 25.213 are available and associated with the PRACH.
		The information is coded in a 16-bit number. The bits from left to right indicate the availability of signature 15 to
		signature 0 (0=not available, 1=available) . \n
			:return: signature: Range: #B0000000000000000 to #B1111111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SIGNature?')
		return Conversions.str_to_float(response)

	def set_signature(self, signature: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:PREamble:SIGNature \n
		Snippet: driver.configure.uplink.prach.preamble.set_signature(signature = 1.0) \n
		Specifies which of the 16 signatures defined by 3GPP TS 25.213 are available and associated with the PRACH.
		The information is coded in a 16-bit number. The bits from left to right indicate the availability of signature 15 to
		signature 0 (0=not available, 1=available) . \n
			:param signature: Range: #B0000000000000000 to #B1111111111111111
		"""
		param = Conversions.decimal_value_to_str(signature)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:PREamble:SIGNature {param}')
