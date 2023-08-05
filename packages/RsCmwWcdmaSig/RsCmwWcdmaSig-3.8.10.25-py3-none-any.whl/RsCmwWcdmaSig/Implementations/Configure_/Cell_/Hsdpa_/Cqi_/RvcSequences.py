from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvcSequences:
	"""RvcSequences commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rvcSequences", core, parent)

	@property
	def qpsk(self):
		"""qpsk commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qpsk'):
			from .RvcSequences_.Qpsk import Qpsk
			self._qpsk = Qpsk(self._core, self._base)
		return self._qpsk

	@property
	def qam(self):
		"""qam commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_qam'):
			from .RvcSequences_.Qam import Qam
			self._qam = Qam(self._core, self._base)
		return self._qam

	def clone(self) -> 'RvcSequences':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RvcSequences(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
