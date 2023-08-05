from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 64 total commands, 11 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def elogging(self):
		"""elogging commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_elogging'):
			from .Sense_.Elogging import Elogging
			self._elogging = Elogging(self._core, self._base)
		return self._elogging

	@property
	def ueReport(self):
		"""ueReport commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueReport'):
			from .Sense_.UeReport import UeReport
			self._ueReport = UeReport(self._core, self._base)
		return self._ueReport

	@property
	def ueCapability(self):
		"""ueCapability commands group. 4 Sub-classes, 10 commands."""
		if not hasattr(self, '_ueCapability'):
			from .Sense_.UeCapability import UeCapability
			self._ueCapability = UeCapability(self._core, self._base)
		return self._ueCapability

	@property
	def uesInfo(self):
		"""uesInfo commands group. 2 Sub-classes, 12 commands."""
		if not hasattr(self, '_uesInfo'):
			from .Sense_.UesInfo import UesInfo
			self._uesInfo = UesInfo(self._core, self._base)
		return self._uesInfo

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Sense_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def iqOut(self):
		"""iqOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOut'):
			from .Sense_.IqOut import IqOut
			self._iqOut = IqOut(self._core, self._base)
		return self._iqOut

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Sense_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Sense_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_connection'):
			from .Sense_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def sms(self):
		"""sms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sense_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def fading(self):
		"""fading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Sense_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
