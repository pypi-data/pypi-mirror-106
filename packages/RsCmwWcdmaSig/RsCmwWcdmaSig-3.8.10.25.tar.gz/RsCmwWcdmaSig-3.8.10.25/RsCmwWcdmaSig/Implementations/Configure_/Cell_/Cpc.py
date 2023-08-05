from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cpc:
	"""Cpc commands group definition. 22 total commands, 6 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cpc", core, parent)

	@property
	def dtrx(self):
		"""dtrx commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dtrx'):
			from .Cpc_.Dtrx import Dtrx
			self._dtrx = Dtrx(self._core, self._base)
		return self._dtrx

	@property
	def udtx(self):
		"""udtx commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_udtx'):
			from .Cpc_.Udtx import Udtx
			self._udtx = Udtx(self._core, self._base)
		return self._udtx

	@property
	def ddrx(self):
		"""ddrx commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ddrx'):
			from .Cpc_.Ddrx import Ddrx
			self._ddrx = Ddrx(self._core, self._base)
		return self._ddrx

	@property
	def mac(self):
		"""mac commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Cpc_.Mac import Mac
			self._mac = Mac(self._core, self._base)
		return self._mac

	@property
	def hlOperation(self):
		"""hlOperation commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_hlOperation'):
			from .Cpc_.HlOperation import HlOperation
			self._hlOperation = HlOperation(self._core, self._base)
		return self._hlOperation

	@property
	def horder(self):
		"""horder commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_horder'):
			from .Cpc_.Horder import Horder
			self._horder = Horder(self._core, self._base)
		return self._horder

	def get_sformat(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:SFORmat \n
		Snippet: value: int = driver.configure.cell.cpc.get_sformat() \n
		Configures HS-SCCH less operation to reduce the HS-SCCH overhead and UE battery consumption. \n
			:return: slot_format: Uplink DPCCH slot format Range: 1 | 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:SFORmat?')
		return Conversions.str_to_int(response)

	def set_sformat(self, slot_format: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:SFORmat \n
		Snippet: driver.configure.cell.cpc.set_sformat(slot_format = 1) \n
		Configures HS-SCCH less operation to reduce the HS-SCCH overhead and UE battery consumption. \n
			:param slot_format: Uplink DPCCH slot format Range: 1 | 4
		"""
		param = Conversions.decimal_value_to_str(slot_format)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:SFORmat {param}')

	def clone(self) -> 'Cpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
