from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 12 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_etfci'):
			from .Carrier_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	@property
	def rsn(self):
		"""rsn commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rsn'):
			from .Carrier_.Rsn import Rsn
			self._rsn = Rsn(self._core, self._base)
		return self._rsn

	@property
	def hbit(self):
		"""hbit commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hbit'):
			from .Carrier_.Hbit import Hbit
			self._hbit = Hbit(self._core, self._base)
		return self._hbit

	@property
	def dpcch(self):
		"""dpcch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dpcch'):
			from .Carrier_.Dpcch import Dpcch
			self._dpcch = Dpcch(self._core, self._base)
		return self._dpcch

	@property
	def anack(self):
		"""anack commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_anack'):
			from .Carrier_.Anack import Anack
			self._anack = Anack(self._core, self._base)
		return self._anack

	@property
	def cqi(self):
		"""cqi commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cqi'):
			from .Carrier_.Cqi import Cqi
			self._cqi = Cqi(self._core, self._base)
		return self._cqi

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
