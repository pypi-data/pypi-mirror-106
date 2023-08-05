from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HlOperation:
	"""HlOperation commands group definition. 4 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hlOperation", core, parent)

	@property
	def tblock(self):
		"""tblock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tblock'):
			from .HlOperation_.Tblock import Tblock
			self._tblock = Tblock(self._core, self._base)
		return self._tblock

	@property
	def scSupport(self):
		"""scSupport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scSupport'):
			from .HlOperation_.ScSupport import ScSupport
			self._scSupport = ScSupport(self._core, self._base)
		return self._scSupport

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:ENABle \n
		Snippet: value: bool = driver.configure.cell.cpc.hlOperation.get_enable() \n
		Enables/disables HS-SCCH less operation \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:ENABle \n
		Snippet: driver.configure.cell.cpc.hlOperation.set_enable(enable = False) \n
		Enables/disables HS-SCCH less operation \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:ENABle {param}')

	def get_nt_block(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:NTBLock \n
		Snippet: value: int = driver.configure.cell.cpc.hlOperation.get_nt_block() \n
		Selects the number of preconfiguration set (column of the table 'No. of Transport Block Size Indicies') to be used for
		the initial transmission of HS-SCCH less operation. See also: CONFigure:WCDMa:SIGN<i>:CELL:CPC:HLOPeration:TBLock<index>
		CONFigure:WCDMa:SIGN<i>:CELL:CPC:HLOPeration:SCSupport<index> \n
			:return: number: Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:NTBLock?')
		return Conversions.str_to_int(response)

	def set_nt_block(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:NTBLock \n
		Snippet: driver.configure.cell.cpc.hlOperation.set_nt_block(number = 1) \n
		Selects the number of preconfiguration set (column of the table 'No. of Transport Block Size Indicies') to be used for
		the initial transmission of HS-SCCH less operation. See also: CONFigure:WCDMa:SIGN<i>:CELL:CPC:HLOPeration:TBLock<index>
		CONFigure:WCDMa:SIGN<i>:CELL:CPC:HLOPeration:SCSupport<index> \n
			:param number: Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:NTBLock {param}')

	def clone(self) -> 'HlOperation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HlOperation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
