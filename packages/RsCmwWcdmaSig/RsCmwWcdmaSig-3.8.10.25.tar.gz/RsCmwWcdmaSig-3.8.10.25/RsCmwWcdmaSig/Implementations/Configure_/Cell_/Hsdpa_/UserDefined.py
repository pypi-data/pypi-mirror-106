from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 6 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def rvcSequences(self):
		"""rvcSequences commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rvcSequences'):
			from .UserDefined_.RvcSequences import RvcSequences
			self._rvcSequences = RvcSequences(self._core, self._base)
		return self._rvcSequences

	def get_harq(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:HARQ \n
		Snippet: value: int = driver.configure.cell.hsdpa.userDefined.get_harq() \n
		Specifies the number of HARQ processes. \n
			:return: number: Range: 1 to 8
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:HARQ?')
		return Conversions.str_to_int(response)

	def set_harq(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:HARQ \n
		Snippet: driver.configure.cell.hsdpa.userDefined.set_harq(number = 1) \n
		Specifies the number of HARQ processes. \n
			:param number: Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:HARQ {param}')

	def get_ir_buffer(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:IRBuffer \n
		Snippet: value: int = driver.configure.cell.hsdpa.userDefined.get_ir_buffer() \n
		Queries the calculated size (no. of bits) of the virtual IR buffer used in the H-ARQ process. \n
			:return: buffer_size: Range: 0 bits to 384E+3 bits, Unit: bits
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:IRBuffer?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
