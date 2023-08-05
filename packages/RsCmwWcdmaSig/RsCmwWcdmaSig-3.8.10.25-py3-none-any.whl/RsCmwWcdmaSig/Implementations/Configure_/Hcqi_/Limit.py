from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 5 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def awgn(self):
		"""awgn commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_awgn'):
			from .Limit_.Awgn import Awgn
			self._awgn = Awgn(self._core, self._base)
		return self._awgn

	@property
	def fading(self):
		"""fading commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fading'):
			from .Limit_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
