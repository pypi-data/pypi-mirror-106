from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 2 total commands, 1 Sub-groups, 1 group commands
	Repeated Capability: Band, default value after init: Band.B1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("band", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_band_get', 'repcap_band_set', repcap.Band.B1)

	def repcap_band_set(self, enum_value: repcap.Band) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Band.Default
		Default value after init: Band.B1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_band_get(self) -> repcap.Band:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def nc(self):
		"""nc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nc'):
			from .Band_.Nc import Nc
			self._nc = Nc(self._core, self._base)
		return self._nc

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Support of non-contiguous multi-cell operation
			- Power_Class: int: The UE power class
			- Add_Sec_Cells: int: Number of additional secondary serving cells supported by the UE. The absence of this IE means that the UE does not support multi-cell operation on three or four cells.
			- Ul_Oltd: enums.YesNoStatus: NO | YES Support of uplink open loop transmit diversity
			- Nc_2_C: enums.YesNoStatus: NO | YES Support of non-contiguous multi-cell operation on two cells
			- Nc_3_C: enums.YesNoStatus: NO | YES Support of non-contiguous multi-cell operation on three cells
			- Nc_4_C: enums.YesNoStatus: NO | YES Support of non-contiguous multi-cell operation on four cells
			- Ul_Cltd: enums.YesNoStatus: NO | YES Support of uplink closed loop transmit diversity in CELL_DCH
			- Ul_Mimo: enums.YesNoStatus: NO | YES Support of uplink MIMO in CELL_DCH
			- Mimo_4_X_4_Mode: enums.YesNoStatus: NO | YES Support of MIMO mode with four transmit antennas in CELL_DCH
			- Freq_Spec_Cmn_Cop: enums.YesNoStatus: NO | YES Support of frequency-specific compressed mode for intra-band non-contiguous operation"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class'),
			ArgStruct.scalar_int('Add_Sec_Cells'),
			ArgStruct.scalar_enum('Ul_Oltd', enums.YesNoStatus),
			ArgStruct.scalar_enum('Nc_2_C', enums.YesNoStatus),
			ArgStruct.scalar_enum('Nc_3_C', enums.YesNoStatus),
			ArgStruct.scalar_enum('Nc_4_C', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ul_Cltd', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ul_Mimo', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mimo_4_X_4_Mode', enums.YesNoStatus),
			ArgStruct.scalar_enum('Freq_Spec_Cmn_Cop', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Power_Class: int = None
			self.Add_Sec_Cells: int = None
			self.Ul_Oltd: enums.YesNoStatus = None
			self.Nc_2_C: enums.YesNoStatus = None
			self.Nc_3_C: enums.YesNoStatus = None
			self.Nc_4_C: enums.YesNoStatus = None
			self.Ul_Cltd: enums.YesNoStatus = None
			self.Ul_Mimo: enums.YesNoStatus = None
			self.Mimo_4_X_4_Mode: enums.YesNoStatus = None
			self.Freq_Spec_Cmn_Cop: enums.YesNoStatus = None

	def get(self, band=repcap.Band.Default) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RFParameter:BAND<band> \n
		Snippet: value: GetStruct = driver.sense.ueCapability.rfParameter.band.get(band = repcap.Band.Default) \n
		Queries the UE capabilities for the selected band related to non-contiguous multi-cell operation. \n
			:param band: optional repeated capability selector. Default value: B1 (settable in the interface 'Band')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		band_cmd_val = self._base.get_repcap_cmd_value(band, repcap.Band)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UECapability:RFParameter:BAND{band_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Band':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Band(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
