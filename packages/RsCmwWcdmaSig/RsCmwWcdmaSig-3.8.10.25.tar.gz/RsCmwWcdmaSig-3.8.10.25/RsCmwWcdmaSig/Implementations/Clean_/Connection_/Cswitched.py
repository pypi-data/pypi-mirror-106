from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def attempt(self):
		"""attempt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attempt'):
			from .Cswitched_.Attempt import Attempt
			self._attempt = Attempt(self._core, self._base)
		return self._attempt

	@property
	def reject(self):
		"""reject commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reject'):
			from .Cswitched_.Reject import Reject
			self._reject = Reject(self._core, self._base)
		return self._reject

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
