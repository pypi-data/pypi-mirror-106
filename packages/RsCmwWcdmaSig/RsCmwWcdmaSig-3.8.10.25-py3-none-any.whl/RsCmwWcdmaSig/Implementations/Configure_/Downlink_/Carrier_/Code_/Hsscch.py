from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsscch:
	"""Hsscch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: HSSCch, default value after init: HSSCch.No1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsscch", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_hSSCch_get', 'repcap_hSSCch_set', repcap.HSSCch.No1)

	def repcap_hSSCch_set(self, enum_value: repcap.HSSCch) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HSSCch.Default
		Default value after init: HSSCch.No1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_hSSCch_get(self) -> repcap.HSSCch:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, channel_code: int, hSSCch=repcap.HSSCch.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:HSSCch<nr> \n
		Snippet: driver.configure.downlink.carrier.code.hsscch.set(channel_code = 1, hSSCch = repcap.HSSCch.Default) \n
		Sets the channelization code number of an HS-SCCH channel. \n
			:param channel_code: Range: 0 to 127
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')"""
		param = Conversions.decimal_value_to_str(channel_code)
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:HSSCch{hSSCch_cmd_val} {param}')

	def get(self, hSSCch=repcap.HSSCch.Default) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:HSSCch<nr> \n
		Snippet: value: int = driver.configure.downlink.carrier.code.hsscch.get(hSSCch = repcap.HSSCch.Default) \n
		Sets the channelization code number of an HS-SCCH channel. \n
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')
			:return: channel_code: Range: 0 to 127"""
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:HSSCch{hSSCch_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Hsscch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsscch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
