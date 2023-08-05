from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 9 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_preamble'):
			from .Prach_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	@property
	def message(self):
		"""message commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_message'):
			from .Prach_.Message import Message
			self._message = Message(self._core, self._base)
		return self._message

	def get_drx_cycle(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:DRXCycle \n
		Snippet: value: int = driver.configure.uplink.prach.get_drx_cycle() \n
		Specifies the DRX cycle length. \n
			:return: cycle_length: Cycle length in multiples of 2 frames Range: 6 to 9
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:DRXCycle?')
		return Conversions.str_to_int(response)

	def set_drx_cycle(self, cycle_length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:PRACh:DRXCycle \n
		Snippet: driver.configure.uplink.prach.set_drx_cycle(cycle_length = 1) \n
		Specifies the DRX cycle length. \n
			:param cycle_length: Cycle length in multiples of 2 frames Range: 6 to 9
		"""
		param = Conversions.decimal_value_to_str(cycle_length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:PRACh:DRXCycle {param}')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
