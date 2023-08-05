from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enhanced:
	"""Enhanced commands group definition. 7 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enhanced", core, parent)

	@property
	def dpch(self):
		"""dpch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpch'):
			from .Enhanced_.Dpch import Dpch
			self._dpch = Dpch(self._core, self._base)
		return self._dpch

	@property
	def pcpich(self):
		"""pcpich commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcpich'):
			from .Enhanced_.Pcpich import Pcpich
			self._pcpich = Pcpich(self._core, self._base)
		return self._pcpich

	@property
	def hsPdsch(self):
		"""hsPdsch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hsPdsch'):
			from .Enhanced_.HsPdsch import HsPdsch
			self._hsPdsch = HsPdsch(self._core, self._base)
		return self._hsPdsch

	@property
	def hsscch(self):
		"""hsscch commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_hsscch'):
			from .Enhanced_.Hsscch import Hsscch
			self._hsscch = Hsscch(self._core, self._base)
		return self._hsscch

	def clone(self) -> 'Enhanced':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Enhanced(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
