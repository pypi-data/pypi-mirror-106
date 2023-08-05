from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReport:
	"""UeReport commands group definition. 5 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueReport", core, parent)

	@property
	def ncell(self):
		"""ncell commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncell'):
			from .UeReport_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	# noinspection PyTypeChecker
	class CcellStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cpi_Ch_Rscp: List[float]: No parameter help available
			- Cpi_Ch_Ec_No: List[float]: No parameter help available
			- Tch_Bler: List[float]: No parameter help available
			- Tx_Power: List[float]: No parameter help available
			- Rx_Tx_Time_Diff: List[int]: No parameter help available
			- Pathloss: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Cpi_Ch_Rscp', DataType.FloatList, None, False, False, 2),
			ArgStruct('Cpi_Ch_Ec_No', DataType.FloatList, None, False, False, 2),
			ArgStruct('Tch_Bler', DataType.FloatList, None, False, False, 2),
			ArgStruct('Tx_Power', DataType.FloatList, None, False, False, 2),
			ArgStruct('Rx_Tx_Time_Diff', DataType.IntegerList, None, False, False, 2),
			ArgStruct.scalar_float('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cpi_Ch_Rscp: List[float] = None
			self.Cpi_Ch_Ec_No: List[float] = None
			self.Tch_Bler: List[float] = None
			self.Tx_Power: List[float] = None
			self.Rx_Tx_Time_Diff: List[int] = None
			self.Pathloss: float = None

	def get_ccell(self) -> CcellStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UEReport:CCELl \n
		Snippet: value: CcellStruct = driver.sense.ueReport.get_ccell() \n
		Returns the UE measurement report contents for the current cell. See also 'UTRA FDD (Current Cell) '. The number to the
		left of each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for CcellStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UEReport:CCELl?', self.__class__.CcellStruct())

	def clone(self) -> 'UeReport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
