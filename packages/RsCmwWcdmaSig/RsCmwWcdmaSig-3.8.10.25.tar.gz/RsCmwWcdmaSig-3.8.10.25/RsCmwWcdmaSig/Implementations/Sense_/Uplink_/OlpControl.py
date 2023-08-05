from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OlpControl:
	"""OlpControl commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("olpControl", core, parent)

	def get_eip_power(self) -> float:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UL:OLPControl:EIPPower \n
		Snippet: value: float = driver.sense.uplink.olpControl.get_eip_power() \n
		Queries the expected initial preamble power. \n
			:return: exp_preamble_pwr: Range: -160 dBm to 33 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UL:OLPControl:EIPPower?')
		return Conversions.str_to_float(response)
