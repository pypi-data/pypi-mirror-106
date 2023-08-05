from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class T:
	"""T commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Timer, default value after init: Timer.T313"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("t", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_timer_get', 'repcap_timer_set', repcap.Timer.T313)

	def repcap_timer_set(self, enum_value: repcap.Timer) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Timer.Default
		Default value after init: Timer.T313"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_timer_get(self) -> repcap.Timer:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, value: int, timer=repcap.Timer.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:T<nr> \n
		Snippet: driver.configure.cell.timeout.t.set(value = 1, timer = repcap.Timer.Default) \n
		Set the timeout value for timer T3212 and T3312. \n
			:param value: Range: 0 to 255, Unit: 6 minutes for T3212, 2 seconds for T3312
			:param timer: optional repeated capability selector. Default value: T313 (settable in the interface 'T')"""
		param = Conversions.decimal_value_to_str(value)
		timer_cmd_val = self._base.get_repcap_cmd_value(timer, repcap.Timer)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:T{timer_cmd_val} {param}')

	def get(self, timer=repcap.Timer.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:T<nr> \n
		Snippet: value: int = driver.configure.cell.timeout.t.get(timer = repcap.Timer.Default) \n
		Set the timeout value for timer T3212 and T3312. \n
			:param timer: optional repeated capability selector. Default value: T313 (settable in the interface 'T')
			:return: value: Range: 0 to 255, Unit: 6 minutes for T3212, 2 seconds for T3312"""
		timer_cmd_val = self._base.get_repcap_cmd_value(timer, repcap.Timer)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:T{timer_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'T':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = T(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
