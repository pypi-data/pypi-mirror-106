from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpcset:
	"""Tpcset commands group definition. 10 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpcset", core, parent)

	@property
	def pconfig(self):
		"""pconfig commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_pconfig'):
			from .Tpcset_.Pconfig import Pconfig
			self._pconfig = Pconfig(self._core, self._base)
		return self._pconfig

	@property
	def precondition(self):
		"""precondition commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_precondition'):
			from .Tpcset_.Precondition import Precondition
			self._precondition = Precondition(self._core, self._base)
		return self._precondition

	def clone(self) -> 'Tpcset':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpcset(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
