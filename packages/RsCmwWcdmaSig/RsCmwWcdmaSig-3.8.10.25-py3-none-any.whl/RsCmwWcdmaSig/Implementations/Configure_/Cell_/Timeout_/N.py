from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N:
	"""N commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: CounterNo, default value after init: CounterNo.Nr313"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("n", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_counterNo_get', 'repcap_counterNo_set', repcap.CounterNo.Nr313)

	def repcap_counterNo_set(self, enum_value: repcap.CounterNo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CounterNo.Default
		Default value after init: CounterNo.Nr313"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_counterNo_get(self) -> repcap.CounterNo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, value: enums.CounterValue, counterNo=repcap.CounterNo.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:N<nr> \n
		Snippet: driver.configure.cell.timeout.n.set(value = enums.CounterValue.N1, counterNo = repcap.CounterNo.Default) \n
		Sets a maximum value for counter N313. The UE counts successive 'out of sync' indications received from layer 1. When the
		maximum value is reached, the UE considers a 'radio link failure' condition and a connection release. \n
			:param value: N1 | N2 | N4 | N10 | N20 | N50 | N100 | N200 Maximum counter value prefixed by N.
			:param counterNo: optional repeated capability selector. Default value: Nr313 (settable in the interface 'N')"""
		param = Conversions.enum_scalar_to_str(value, enums.CounterValue)
		counterNo_cmd_val = self._base.get_repcap_cmd_value(counterNo, repcap.CounterNo)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:N{counterNo_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, counterNo=repcap.CounterNo.Default) -> enums.CounterValue:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:N<nr> \n
		Snippet: value: enums.CounterValue = driver.configure.cell.timeout.n.get(counterNo = repcap.CounterNo.Default) \n
		Sets a maximum value for counter N313. The UE counts successive 'out of sync' indications received from layer 1. When the
		maximum value is reached, the UE considers a 'radio link failure' condition and a connection release. \n
			:param counterNo: optional repeated capability selector. Default value: Nr313 (settable in the interface 'N')
			:return: value: N1 | N2 | N4 | N10 | N20 | N50 | N100 | N200 Maximum counter value prefixed by N."""
		counterNo_cmd_val = self._base.get_repcap_cmd_value(counterNo, repcap.CounterNo)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:N{counterNo_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.CounterValue)

	def clone(self) -> 'N':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = N(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
