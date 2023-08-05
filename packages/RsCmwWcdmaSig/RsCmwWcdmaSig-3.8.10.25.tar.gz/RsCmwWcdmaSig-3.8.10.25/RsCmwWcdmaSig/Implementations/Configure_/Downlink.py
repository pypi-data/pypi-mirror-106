from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 58 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Downlink_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_level'):
			from .Downlink_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def code(self):
		"""code commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_code'):
			from .Downlink_.Code import Code
			self._code = Code(self._core, self._base)
		return self._code

	@property
	def enhanced(self):
		"""enhanced commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_enhanced'):
			from .Downlink_.Enhanced import Enhanced
			self._enhanced = Enhanced(self._core, self._base)
		return self._enhanced

	@property
	def pcontrol(self):
		"""pcontrol commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_pcontrol'):
			from .Downlink_.Pcontrol import Pcontrol
			self._pcontrol = Pcontrol(self._core, self._base)
		return self._pcontrol

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
