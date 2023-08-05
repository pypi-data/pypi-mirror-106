from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("burst", core, parent)

	def set(self, burst: int, cycle=repcap.Cycle.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:BURSt \n
		Snippet: driver.configure.cell.cpc.udtx.cycle.burst.set(burst = 1, cycle = repcap.Cycle.Default) \n
		Length of DPCCH transmission during UE DTX cycle, see 'Continuous Packet Connectivity (CPC) '. \n
			:param burst: Only the following values are allowed (in subframes) : 1 | 2 | 5 If you enter another value, the nearest allowed value is set instead. Range: 1 Subframe to 5 Subframe
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')"""
		param = Conversions.decimal_value_to_str(burst)
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:BURSt {param}')

	def get(self, cycle=repcap.Cycle.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CYCLe<nr>:BURSt \n
		Snippet: value: int = driver.configure.cell.cpc.udtx.cycle.burst.get(cycle = repcap.Cycle.Default) \n
		Length of DPCCH transmission during UE DTX cycle, see 'Continuous Packet Connectivity (CPC) '. \n
			:param cycle: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cycle')
			:return: burst: Only the following values are allowed (in subframes) : 1 | 2 | 5 If you enter another value, the nearest allowed value is set instead. Range: 1 Subframe to 5 Subframe"""
		cycle_cmd_val = self._base.get_repcap_cmd_value(cycle, repcap.Cycle)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CYCLe{cycle_cmd_val}:BURSt?')
		return Conversions.str_to_int(response)
