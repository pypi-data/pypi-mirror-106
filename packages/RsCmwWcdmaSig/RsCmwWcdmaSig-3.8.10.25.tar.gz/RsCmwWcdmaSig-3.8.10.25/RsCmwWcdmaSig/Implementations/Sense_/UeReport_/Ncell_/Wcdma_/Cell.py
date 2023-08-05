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
			- Rscp: List[float]: CPICH RSCP: low and high value range Range: -120 dBm to -25 dBm , Unit: dBm
			- Ecn_0: List[float]: CPICH Ec/No: low and high value range Range: -24 dB to 0 dB , Unit: dB
			- Rssi: List[float]: CPICH RSSI Range: -50 dBm to 34 dBm, Unit: dBm
			- Sfn_Cfn: List[float]: SFN-CFN time difference: low end high value range Range: 768 chips to 1280 chips , Unit: chips
			- Pathloss: float: Range: 46 dB to 158 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct('Rscp', DataType.FloatList, None, False, False, 2),
			ArgStruct('Ecn_0', DataType.FloatList, None, False, False, 2),
			ArgStruct('Rssi', DataType.FloatList, None, False, False, 2),
			ArgStruct('Sfn_Cfn', DataType.FloatList, None, False, False, 2),
			ArgStruct.scalar_float('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rscp: List[float] = None
			self.Ecn_0: List[float] = None
			self.Rssi: List[float] = None
			self.Sfn_Cfn: List[float] = None
			self.Pathloss: float = None

	def get(self, cell=repcap.Cell.Nr1) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UEReport:NCELl:WCDMa:CELL<nr> \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.wcdma.cell.get(cell = repcap.Cell.Nr1) \n
		Returns the UE measurement report contents for WCDMA neighbor cell. See also 'Neighbor Cells UTRA FDD'. \n
			:param cell: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UEReport:NCELl:WCDMa:CELL{cell_cmd_val}?', self.__class__.GetStruct())
