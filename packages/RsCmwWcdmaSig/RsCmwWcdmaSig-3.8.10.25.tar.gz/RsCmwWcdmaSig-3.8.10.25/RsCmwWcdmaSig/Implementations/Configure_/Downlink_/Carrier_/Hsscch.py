from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsscch:
	"""Hsscch commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
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

	@property
	def ueId(self):
		"""ueId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueId'):
			from .Hsscch_.UeId import UeId
			self._ueId = UeId(self._core, self._base)
		return self._ueId

	@property
	def idDummy(self):
		"""idDummy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idDummy'):
			from .Hsscch_.IdDummy import IdDummy
			self._idDummy = IdDummy(self._core, self._base)
		return self._idDummy

	def clone(self) -> 'Hsscch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsscch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
