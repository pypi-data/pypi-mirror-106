from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 28 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def hsdpa(self):
		"""hsdpa commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsdpa'):
			from .Carrier_.Hsdpa import Hsdpa
			self._hsdpa = Hsdpa(self._core, self._base)
		return self._hsdpa

	@property
	def hsupa(self):
		"""hsupa commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsupa'):
			from .Carrier_.Hsupa import Hsupa
			self._hsupa = Hsupa(self._core, self._base)
		return self._hsupa

	@property
	def horder(self):
		"""horder commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_horder'):
			from .Carrier_.Horder import Horder
			self._horder = Horder(self._core, self._base)
		return self._horder

	def get_scode(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:SCODe \n
		Snippet: value: float = driver.configure.cell.carrier.get_scode() \n
		Specifies index i for calculation of the primary scrambling code number by multiplication with 16. For details, see
		'Scrambling Codes'. \n
			:return: code: Range: #H0 to #H1FF
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:SCODe?')
		return Conversions.str_to_float(response)

	def set_scode(self, code: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:SCODe \n
		Snippet: driver.configure.cell.carrier.set_scode(code = 1.0) \n
		Specifies index i for calculation of the primary scrambling code number by multiplication with 16. For details, see
		'Scrambling Codes'. \n
			:param code: Range: #H0 to #H1FF
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:SCODe {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
