from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
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
			- Rssi: List[float]: BCCH RSSI: low and high value range Range: -50 dBm to 34 dBm, Unit: dBm
			- Bsic: enums.Bsic: NONVerified | VERified NONV: RSSI measurement without BSIC decoding VER: RSSI measurement with BSIC decoding"""
		__meta_args_list = [
			ArgStruct('Rssi', DataType.FloatList, None, False, False, 2),
			ArgStruct.scalar_enum('Bsic', enums.Bsic)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rssi: List[float] = None
			self.Bsic: enums.Bsic = None

	def get(self, cell=repcap.Cell.Nr1) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UEReport:NCELl:GSM:CELL<nr> \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.gsm.cell.get(cell = repcap.Cell.Nr1) \n
		Returns the UE measurement report contents for GSM neighbor cell. See also 'Neighbor Cell Settings'. \n
			:param cell: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UEReport:NCELl:GSM:CELL{cell_cmd_val}?', self.__class__.GetStruct())
