from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 12 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def tblock(self):
		"""tblock commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tblock'):
			from .Carrier_.Tblock import Tblock
			self._tblock = Tblock(self._core, self._base)
		return self._tblock

	@property
	def code(self):
		"""code commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_code'):
			from .Carrier_.Code import Code
			self._code = Code(self._core, self._base)
		return self._code

	@property
	def modulation(self):
		"""modulation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Carrier_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
