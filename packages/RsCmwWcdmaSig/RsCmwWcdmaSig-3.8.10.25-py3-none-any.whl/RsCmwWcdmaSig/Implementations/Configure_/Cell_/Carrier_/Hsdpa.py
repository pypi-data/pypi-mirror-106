from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsdpa:
	"""Hsdpa commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsdpa", core, parent)

	@property
	def cqi(self):
		"""cqi commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cqi'):
			from .Hsdpa_.Cqi import Cqi
			self._cqi = Cqi(self._core, self._base)
		return self._cqi

	@property
	def userDefined(self):
		"""userDefined commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_userDefined'):
			from .Hsdpa_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	def clone(self) -> 'Hsdpa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsdpa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
