from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rsrp: List[float]: Range: -19.5 dB to -3 dB , Unit: dB
			- Rsrq: List[float]: Range: -140 dBm to -44 dBm , Unit: dBm"""
		__meta_args_list = [
			ArgStruct('Rsrp', DataType.FloatList, None, False, False, 2),
			ArgStruct('Rsrq', DataType.FloatList, None, False, False, 2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp: List[float] = None
			self.Rsrq: List[float] = None

	def get(self, cell=repcap.Cell.Nr1) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UEReport:NCELl:LTE:CELL<nr> \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.lte.cell.get(cell = repcap.Cell.Nr1) \n
		Returns the low and high value ranges reported for a selected LTE neighbor cell. See also 'Neighbor Cell Settings'. \n
			:param cell: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UEReport:NCELl:LTE:CELL{cell_cmd_val}?', self.__class__.GetStruct())
