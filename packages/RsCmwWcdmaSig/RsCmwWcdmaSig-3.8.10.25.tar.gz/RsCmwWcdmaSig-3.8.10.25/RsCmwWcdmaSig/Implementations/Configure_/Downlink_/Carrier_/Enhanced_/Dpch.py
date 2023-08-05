from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpch:
	"""Dpch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpch", core, parent)

	def get_fs_format(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:DPCH:FSFormat \n
		Snippet: value: int = driver.configure.downlink.carrier.enhanced.dpch.get_fs_format() \n
		Sets F-DPCH slot format according to 3GPP TS 25.211, table 16C. \n
			:return: slot_format: Range: 0 to 9
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:DPCH:FSFormat?')
		return Conversions.str_to_int(response)

	def set_fs_format(self, slot_format: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:DPCH:FSFormat \n
		Snippet: driver.configure.downlink.carrier.enhanced.dpch.set_fs_format(slot_format = 1) \n
		Sets F-DPCH slot format according to 3GPP TS 25.211, table 16C. \n
			:param slot_format: Range: 0 to 9
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(slot_format)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:DPCH:FSFormat {param}')
