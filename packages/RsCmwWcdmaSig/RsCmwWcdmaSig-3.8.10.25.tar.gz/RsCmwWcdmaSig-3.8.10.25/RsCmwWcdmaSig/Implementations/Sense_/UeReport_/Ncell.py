from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncell:
	"""Ncell commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ncell", core, parent)
		
		self._base.multi_repcap_types = "DownCarrier,Cell"

	@property
	def gsm(self):
		"""gsm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Ncell_.Gsm import Gsm
			self._gsm = Gsm(self._core, self._base)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Ncell_.Wcdma import Wcdma
			self._wcdma = Wcdma(self._core, self._base)
		return self._wcdma

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Ncell_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Cpi_Ch_Rscp: List[float]: No parameter help available
			- Cpi_Ch_Ec_No: List[float]: No parameter help available
			- Rssi: List[float]: No parameter help available
			- Sfn_Cfn_Time_Diff: List[int]: No parameter help available
			- Pathloss: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Cpi_Ch_Rscp', DataType.FloatList, None, False, False, 2),
			ArgStruct('Cpi_Ch_Ec_No', DataType.FloatList, None, False, False, 2),
			ArgStruct('Rssi', DataType.FloatList, None, False, False, 2),
			ArgStruct('Sfn_Cfn_Time_Diff', DataType.IntegerList, None, False, False, 2),
			ArgStruct.scalar_float('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cpi_Ch_Rscp: List[float] = None
			self.Cpi_Ch_Ec_No: List[float] = None
			self.Rssi: List[float] = None
			self.Sfn_Cfn_Time_Diff: List[int] = None
			self.Pathloss: float = None

	def get(self, downCarrier=repcap.DownCarrier.Dc1) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UEReport:NCELl<nr> \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.get(downCarrier = repcap.DownCarrier.Dc1) \n
		Returns the UE measurement report contents for additional carrier in multi-carrier operation. See also 'UTRA FDD (Carrier
		2 / Carrier 3) '. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:param downCarrier: optional repeated capability selector. Default value: Dc1
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		downCarrier_cmd_val = self._base.get_repcap_cmd_value(downCarrier, repcap.DownCarrier)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UEReport:NCELl{downCarrier_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Ncell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ncell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
