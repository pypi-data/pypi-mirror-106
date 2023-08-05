from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmode:
	"""Cmode commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmode", core, parent)

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_wcdma'):
			from .Cmode_.Wcdma import Wcdma
			self._wcdma = Wcdma(self._core, self._base)
		return self._wcdma

	@property
	def gsm(self):
		"""gsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsm'):
			from .Cmode_.Gsm import Gsm
			self._gsm = Gsm(self._core, self._base)
		return self._gsm

	@property
	def lte(self):
		"""lte commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lte'):
			from .Cmode_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	def clone(self) -> 'Cmode':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmode(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
