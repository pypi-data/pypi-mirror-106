from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ehich:
	"""Ehich commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ehich", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EhichIndicatorMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHICh:MODE \n
		Snippet: value: enums.EhichIndicatorMode = driver.configure.cell.carrier.hsupa.ehich.get_mode() \n
		Specifies the HARQ acknowledgement indicator sequence transmitted via the E-HICH. \n
			:return: mode: CRC | ALTernating | ACK | NACK | DTX CRC: react on UL CRC (ACK, NACK or DTX) ALTernating: alternating ACK, NACK ACK: all ACK NACK: all NACK DTX: all DTX
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHICh:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EhichIndicatorMode)

	def set_mode(self, mode: enums.EhichIndicatorMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHICh:MODE \n
		Snippet: driver.configure.cell.carrier.hsupa.ehich.set_mode(mode = enums.EhichIndicatorMode.ACK) \n
		Specifies the HARQ acknowledgement indicator sequence transmitted via the E-HICH. \n
			:param mode: CRC | ALTernating | ACK | NACK | DTX CRC: react on UL CRC (ACK, NACK or DTX) ALTernating: alternating ACK, NACK ACK: all ACK NACK: all NACK DTX: all DTX
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(mode, enums.EhichIndicatorMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHICh:MODE {param}')

	def get_signature(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHICh:SIGNature \n
		Snippet: value: int = driver.configure.cell.carrier.hsupa.ehich.get_signature() \n
		Specifies the E-HICH signature. \n
			:return: signature: Range: 0 to 39
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHICh:SIGNature?')
		return Conversions.str_to_int(response)

	def set_signature(self, signature: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHICh:SIGNature \n
		Snippet: driver.configure.cell.carrier.hsupa.ehich.set_signature(signature = 1) \n
		Specifies the E-HICH signature. \n
			:param signature: Range: 0 to 39
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(signature)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHICh:SIGNature {param}')
