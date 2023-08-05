from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enhanced:
	"""Enhanced commands group definition. 12 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enhanced", core, parent)

	@property
	def dpch(self):
		"""dpch commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_dpch'):
			from .Enhanced_.Dpch import Dpch
			self._dpch = Dpch(self._core, self._base)
		return self._dpch

	@property
	def aich(self):
		"""aich commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_aich'):
			from .Enhanced_.Aich import Aich
			self._aich = Aich(self._core, self._base)
		return self._aich

	@property
	def scpich(self):
		"""scpich commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scpich'):
			from .Enhanced_.Scpich import Scpich
			self._scpich = Scpich(self._core, self._base)
		return self._scpich

	def clone(self) -> 'Enhanced':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Enhanced(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
