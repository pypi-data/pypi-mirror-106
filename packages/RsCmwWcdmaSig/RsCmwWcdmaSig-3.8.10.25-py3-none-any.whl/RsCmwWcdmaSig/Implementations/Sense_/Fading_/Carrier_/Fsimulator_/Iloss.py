from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iloss:
	"""Iloss commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iloss", core, parent)

	def get_csamples(self) -> float:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ILOSs:CSAMples \n
		Snippet: value: float = driver.sense.fading.carrier.fsimulator.iloss.get_csamples() \n
		Displays the percentage of clipped samples. \n
			:return: clipped_samples: Range: 0 % to 100, Unit: %
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ILOSs:CSAMples?')
		return Conversions.str_to_float(response)
