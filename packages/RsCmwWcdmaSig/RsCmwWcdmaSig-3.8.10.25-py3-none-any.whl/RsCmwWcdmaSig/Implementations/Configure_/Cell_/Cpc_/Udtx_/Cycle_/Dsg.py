from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dsg:
	"""Dsg commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dsg", core, parent)

	def set(self, default_sg: int, cycle=repcap.Cycle.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:DSG \n
		Snippet: driver.configure.cell.cpc.udtx.cycle.dsg.set(default_sg = 1, cycle = repcap.Cycle.Default) \n
		Indicates E-DCH serving grant index to be used in DTX-cycle-2, see 'Continuous Packet Connectivity (CPC) '. \n
			:param default_sg: 0 to 37: indicates E-DCH serving grant index as defined in 3GPP TS 25.321 38: zero grant Range: 0 to 38
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')"""
		param = Conversions.decimal_value_to_str(default_sg)
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:DSG {param}')

	def get(self, cycle=repcap.Cycle.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:DSG \n
		Snippet: value: int = driver.configure.cell.cpc.udtx.cycle.dsg.get(cycle = repcap.Cycle.Default) \n
		Indicates E-DCH serving grant index to be used in DTX-cycle-2, see 'Continuous Packet Connectivity (CPC) '. \n
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')
			:return: default_sg: 0 to 37: indicates E-DCH serving grant index as defined in 3GPP TS 25.321 38: zero grant Range: 0 to 38"""
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:DSG?')
		return Conversions.str_to_int(response)
