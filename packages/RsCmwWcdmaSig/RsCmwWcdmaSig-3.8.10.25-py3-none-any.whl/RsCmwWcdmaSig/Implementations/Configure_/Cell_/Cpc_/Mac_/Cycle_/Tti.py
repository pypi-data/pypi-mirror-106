from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tti:
	"""Tti commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: TransTimeInterval, default value after init: TransTimeInterval.Tti2"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tti", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_transTimeInterval_get', 'repcap_transTimeInterval_set', repcap.TransTimeInterval.Tti2)

	def repcap_transTimeInterval_set(self, enum_value: repcap.TransTimeInterval) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TransTimeInterval.Default
		Default value after init: TransTimeInterval.Tti2"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_transTimeInterval_get(self) -> repcap.TransTimeInterval:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, pattern: int, transTimeInterval=repcap.TransTimeInterval.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:MAC:CYCLe:TTI<ms> \n
		Snippet: driver.configure.cell.cpc.mac.cycle.tti.set(pattern = 1, transTimeInterval = repcap.TransTimeInterval.Default) \n
		Pattern where the start of uplink E-DCH transmission after inactivity is allowed, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:param pattern: Only the following values are allowed (in subframes) : 5 | 10 | 20 for 10 ms TTI 1 | 4 | 5 | 8 | 10 | 16 | 20 for 2 ms TTI If you enter another value, the nearest allowed value is set instead. Range: 1 Subframe to 20 Subframe
			:param transTimeInterval: optional repeated capability selector. Default value: Tti2 (settable in the interface 'Tti')"""
		param = Conversions.decimal_value_to_str(pattern)
		transTimeInterval_cmd_val = self._base.get_repcap_cmd_value(transTimeInterval, repcap.TransTimeInterval)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:MAC:CYCLe:TTI{transTimeInterval_cmd_val} {param}')

	def get(self, transTimeInterval=repcap.TransTimeInterval.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:MAC:CYCLe:TTI<ms> \n
		Snippet: value: int = driver.configure.cell.cpc.mac.cycle.tti.get(transTimeInterval = repcap.TransTimeInterval.Default) \n
		Pattern where the start of uplink E-DCH transmission after inactivity is allowed, see 'Continuous Packet Connectivity
		(CPC) '. \n
			:param transTimeInterval: optional repeated capability selector. Default value: Tti2 (settable in the interface 'Tti')
			:return: pattern: Only the following values are allowed (in subframes) : 5 | 10 | 20 for 10 ms TTI 1 | 4 | 5 | 8 | 10 | 16 | 20 for 2 ms TTI If you enter another value, the nearest allowed value is set instead. Range: 1 Subframe to 20 Subframe"""
		transTimeInterval_cmd_val = self._base.get_repcap_cmd_value(transTimeInterval, repcap.TransTimeInterval)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:MAC:CYCLe:TTI{transTimeInterval_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Tti':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tti(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
