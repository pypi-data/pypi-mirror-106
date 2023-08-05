from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ithreshold:
	"""Ithreshold commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ithreshold", core, parent)

	def set(self, threshold: int, cycle=repcap.Cycle.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:ITHReshold \n
		Snippet: driver.configure.cell.cpc.udtx.cycle.ithreshold.set(threshold = 1, cycle = repcap.Cycle.Default) \n
		Defines when to activate the UE DTX cycle 2 after the last uplink data transmission, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:param threshold: Only the following values are allowed (in E-DCH TTI) : 1 | 4 | 8 | 16 | 32 | 64 | 128 | 256 If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 256 E-DCH TTI
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')"""
		param = Conversions.decimal_value_to_str(threshold)
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:ITHReshold {param}')

	def get(self, cycle=repcap.Cycle.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:ITHReshold \n
		Snippet: value: int = driver.configure.cell.cpc.udtx.cycle.ithreshold.get(cycle = repcap.Cycle.Default) \n
		Defines when to activate the UE DTX cycle 2 after the last uplink data transmission, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')
			:return: threshold: Only the following values are allowed (in E-DCH TTI) : 1 | 4 | 8 | 16 | 32 | 64 | 128 | 256 If you enter another value, the nearest allowed value is set instead. Range: 1 E-DCH TTI to 256 E-DCH TTI"""
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:ITHReshold?')
		return Conversions.str_to_int(response)
