from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_total'):
			from .Throughput_.Total import Total
			self._total = Total(self._core, self._base)
		return self._total

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
