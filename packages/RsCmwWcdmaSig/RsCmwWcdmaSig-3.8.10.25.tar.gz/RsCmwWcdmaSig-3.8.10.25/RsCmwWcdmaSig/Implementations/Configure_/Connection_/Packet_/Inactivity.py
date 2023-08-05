from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inactivity:
	"""Inactivity commands group definition. 10 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("inactivity", core, parent)

	@property
	def dch(self):
		"""dch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dch'):
			from .Inactivity_.Dch import Dch
			self._dch = Dch(self._core, self._base)
		return self._dch

	@property
	def fach(self):
		"""fach commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fach'):
			from .Inactivity_.Fach import Fach
			self._fach = Fach(self._core, self._base)
		return self._fach

	@property
	def cpch(self):
		"""cpch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpch'):
			from .Inactivity_.Cpch import Cpch
			self._cpch = Cpch(self._core, self._base)
		return self._cpch

	@property
	def upch(self):
		"""upch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upch'):
			from .Inactivity_.Upch import Upch
			self._upch = Upch(self._core, self._base)
		return self._upch

	def clone(self) -> 'Inactivity':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Inactivity(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
