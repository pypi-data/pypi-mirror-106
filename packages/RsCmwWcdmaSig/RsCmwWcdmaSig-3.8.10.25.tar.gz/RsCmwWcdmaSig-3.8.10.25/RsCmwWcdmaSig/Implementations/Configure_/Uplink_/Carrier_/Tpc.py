from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	def get_tpower(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:TPC:TPOWer \n
		Snippet: value: float = driver.configure.uplink.carrier.tpc.get_tpower() \n
		Specifies a target power for the target power precondition and for the closed loop setup.
			INTRO_CMD_HELP: The allowed range depends on the active setup: \n
			- 0 dBm to 33 dBm for setups 'Max. Power E-DCH' and 'DC HSPA In-Band Emission'
			- 50 dBm to 33 dBm for other setups
		For the secondary uplink carrier it the target power is calculated as follows: Target Power (secondary carrier) = Target
		Power - Target Power Offset \n
			:return: target_power: Range: depends on active setup, see above , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:TPC:TPOWer?')
		return Conversions.str_to_float(response)

	def set_tpower(self, target_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:TPC:TPOWer \n
		Snippet: driver.configure.uplink.carrier.tpc.set_tpower(target_power = 1.0) \n
		Specifies a target power for the target power precondition and for the closed loop setup.
			INTRO_CMD_HELP: The allowed range depends on the active setup: \n
			- 0 dBm to 33 dBm for setups 'Max. Power E-DCH' and 'DC HSPA In-Band Emission'
			- 50 dBm to 33 dBm for other setups
		For the secondary uplink carrier it the target power is calculated as follows: Target Power (secondary carrier) = Target
		Power - Target Power Offset \n
			:param target_power: Range: depends on active setup, see above , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(target_power)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:TPC:TPOWer {param}')
