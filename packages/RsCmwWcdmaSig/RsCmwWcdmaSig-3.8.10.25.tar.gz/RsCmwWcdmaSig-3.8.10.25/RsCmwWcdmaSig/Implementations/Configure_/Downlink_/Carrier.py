from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 29 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def ocns(self):
		"""ocns commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ocns'):
			from .Carrier_.Ocns import Ocns
			self._ocns = Ocns(self._core, self._base)
		return self._ocns

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 10 commands."""
		if not hasattr(self, '_level'):
			from .Carrier_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def code(self):
		"""code commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_code'):
			from .Carrier_.Code import Code
			self._code = Code(self._core, self._base)
		return self._code

	@property
	def enhanced(self):
		"""enhanced commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_enhanced'):
			from .Carrier_.Enhanced import Enhanced
			self._enhanced = Enhanced(self._core, self._base)
		return self._enhanced

	@property
	def hsscch(self):
		"""hsscch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsscch'):
			from .Carrier_.Hsscch import Hsscch
			self._hsscch = Hsscch(self._core, self._base)
		return self._hsscch

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
