from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ToPower:
	"""ToPower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("toPower", core, parent)

	def get_total(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:TOPower:TOTal \n
		Snippet: value: float = driver.configure.rfSettings.toPower.get_total() \n
		Queries the sum of the output channel power (Ior) and the AWGN power (Ioc) . For scenarios with multi-carrier, the result
		indicates the sum of the Ior and Ioc values of all carriers. \n
			:return: comb_tot_out_pwr: Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:TOPower:TOTal?')
		return Conversions.str_to_float(response)
