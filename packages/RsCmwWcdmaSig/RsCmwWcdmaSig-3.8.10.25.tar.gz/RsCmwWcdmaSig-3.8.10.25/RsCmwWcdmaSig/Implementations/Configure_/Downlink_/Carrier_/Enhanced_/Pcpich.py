from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcpich:
	"""Pcpich commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcpich", core, parent)

	def get_slevel(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:PCPich:SLEVel \n
		Snippet: value: float = driver.configure.downlink.carrier.enhanced.pcpich.get_slevel() \n
		Defines the P-CPICH power level to be reported to the UE. \n
			:return: signalled_level: Range: -10 dBm to 50 dBm, Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:PCPich:SLEVel?')
		return Conversions.str_to_float(response)

	def set_slevel(self, signalled_level: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:PCPich:SLEVel \n
		Snippet: driver.configure.downlink.carrier.enhanced.pcpich.set_slevel(signalled_level = 1.0) \n
		Defines the P-CPICH power level to be reported to the UE. \n
			:param signalled_level: Range: -10 dBm to 50 dBm, Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(signalled_level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:PCPich:SLEVel {param}')
