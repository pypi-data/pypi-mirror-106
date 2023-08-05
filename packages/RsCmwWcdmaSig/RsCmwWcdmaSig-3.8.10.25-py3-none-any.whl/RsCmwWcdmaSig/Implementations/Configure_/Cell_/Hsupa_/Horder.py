from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Horder:
	"""Horder commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("horder", core, parent)

	@property
	def send(self):
		"""send commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_send'):
			from .Horder_.Send import Send
			self._send = Send(self._core, self._base)
		return self._send

	def get_sdc_order(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SDCorder \n
		Snippet: value: bool = driver.configure.cell.hsupa.horder.get_sdc_order() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SDCorder?')
		return Conversions.str_to_bool(response)

	def set_sdc_order(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SDCorder \n
		Snippet: driver.configure.cell.hsupa.horder.set_sdc_order(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SDCorder {param}')

	def get_suf_order(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SUForder \n
		Snippet: value: bool = driver.configure.cell.hsupa.horder.get_suf_order() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SUForder?')
		return Conversions.str_to_bool(response)

	def set_suf_order(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SUForder \n
		Snippet: driver.configure.cell.hsupa.horder.set_suf_order(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SUForder {param}')

	def clone(self) -> 'Horder':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Horder(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
