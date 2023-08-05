from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpch:
	"""Dpch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpch", core, parent)

	def get_reported(self) -> float:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:DPCH:REPorted \n
		Snippet: value: float = driver.sense.downlink.carrier.enhanced.dpch.get_reported() \n
		Displays the downlink DPCH/F-DPCH level reported by the UE. \n
			:return: level: DPCH/F-DPCH level relative to the base level Ior Range: -80 dB to 0 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:DPCH:REPorted?')
		return Conversions.str_to_float(response)
