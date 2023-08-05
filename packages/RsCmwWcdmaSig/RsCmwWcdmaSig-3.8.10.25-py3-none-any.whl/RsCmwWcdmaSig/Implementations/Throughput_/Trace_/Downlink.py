from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def sdu(self):
		"""sdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdu'):
			from .Downlink_.Sdu import Sdu
			self._sdu = Sdu(self._core, self._base)
		return self._sdu

	@property
	def pdu(self):
		"""pdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdu'):
			from .Downlink_.Pdu import Pdu
			self._pdu = Pdu(self._core, self._base)
		return self._pdu

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
