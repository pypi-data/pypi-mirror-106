from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Message:
	"""Message commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("message", core, parent)

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:MESSage:POFFset \n
		Snippet: value: float = driver.configure.uplink.prach.message.get_poffset() \n
		Specifies the power difference between the last preamble transmitted and the RACH message part. \n
			:return: power_offset: Range: -5 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:MESSage:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, power_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:MESSage:POFFset \n
		Snippet: driver.configure.uplink.prach.message.set_poffset(power_offset = 1.0) \n
		Specifies the power difference between the last preamble transmitted and the RACH message part. \n
			:param power_offset: Range: -5 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(power_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:MESSage:POFFset {param}')

	def get_length(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:MESSage:LENGth \n
		Snippet: value: float = driver.configure.uplink.prach.message.get_length() \n
		Specifies the length of the RACH transmission time interval (TTI) . \n
			:return: msg_part_length: Range: 0.01 s to 0.02 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:MESSage:LENGth?')
		return Conversions.str_to_float(response)

	def set_length(self, msg_part_length: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:MESSage:LENGth \n
		Snippet: driver.configure.uplink.prach.message.set_length(msg_part_length = 1.0) \n
		Specifies the length of the RACH transmission time interval (TTI) . \n
			:param msg_part_length: Range: 0.01 s to 0.02 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(msg_part_length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:MESSage:LENGth {param}')
