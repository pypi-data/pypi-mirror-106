from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCategory:
	"""UeCategory commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueCategory", core, parent)

	@property
	def reported(self):
		"""reported commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reported'):
			from .UeCategory_.Reported import Reported
			self._reported = Reported(self._core, self._base)
		return self._reported

	def get_manual(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UECategory:MANual \n
		Snippet: value: int = driver.configure.cell.hsdpa.ueCategory.get_manual() \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UeCategory.Reported.set. \n
			:return: ue_cat_manual: Range: 1 to 24, 29 to 32
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UECategory:MANual?')
		return Conversions.str_to_int(response)

	def set_manual(self, ue_cat_manual: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UECategory:MANual \n
		Snippet: driver.configure.cell.hsdpa.ueCategory.set_manual(ue_cat_manual = 1) \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UeCategory.Reported.set. \n
			:param ue_cat_manual: Range: 1 to 24, 29 to 32
		"""
		param = Conversions.decimal_value_to_str(ue_cat_manual)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UECategory:MANual {param}')

	def clone(self) -> 'UeCategory':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCategory(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
