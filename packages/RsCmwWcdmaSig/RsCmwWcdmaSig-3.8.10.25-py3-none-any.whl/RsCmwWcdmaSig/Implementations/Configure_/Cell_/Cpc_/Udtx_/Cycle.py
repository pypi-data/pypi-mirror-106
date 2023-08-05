from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cycle:
	"""Cycle commands group definition. 4 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: Cycle, default value after init: Cycle.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cycle", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_cycle_get', 'repcap_cycle_set', repcap.Cycle.Nr1)

	def repcap_cycle_set(self, enum_value: repcap.Cycle) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cycle.Default
		Default value after init: Cycle.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_cycle_get(self) -> repcap.Cycle:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def apattern(self):
		"""apattern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apattern'):
			from .Cycle_.Apattern import Apattern
			self._apattern = Apattern(self._core, self._base)
		return self._apattern

	@property
	def burst(self):
		"""burst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_burst'):
			from .Cycle_.Burst import Burst
			self._burst = Burst(self._core, self._base)
		return self._burst

	@property
	def ithreshold(self):
		"""ithreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ithreshold'):
			from .Cycle_.Ithreshold import Ithreshold
			self._ithreshold = Ithreshold(self._core, self._base)
		return self._ithreshold

	@property
	def dsg(self):
		"""dsg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsg'):
			from .Cycle_.Dsg import Dsg
			self._dsg = Dsg(self._core, self._base)
		return self._dsg

	def clone(self) -> 'Cycle':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cycle(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
