from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 8 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def mpThroughput(self):
		"""mpThroughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mpThroughput'):
			from .Trace_.MpThroughput import MpThroughput
			self._mpThroughput = MpThroughput(self._core, self._base)
		return self._mpThroughput

	@property
	def meThroughput(self):
		"""meThroughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_meThroughput'):
			from .Trace_.MeThroughput import MeThroughput
			self._meThroughput = MeThroughput(self._core, self._base)
		return self._meThroughput

	@property
	def throughput(self):
		"""throughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_throughput'):
			from .Trace_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
