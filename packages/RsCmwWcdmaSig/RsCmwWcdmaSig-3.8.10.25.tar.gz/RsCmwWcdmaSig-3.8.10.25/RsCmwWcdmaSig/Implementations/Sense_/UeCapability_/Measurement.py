from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 5 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	@property
	def cmode(self):
		"""cmode commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmode'):
			from .Measurement_.Cmode import Cmode
			self._cmode = Cmode(self._core, self._base)
		return self._cmode

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Inter_Freq_Detect: enums.YesNoStatus: NO | YES Indicates whether the UE is able to measure inter-frequency detected set.
			- Enh_Inter_Freq: enums.YesNoStatus: NO | YES Indicates whether the UE requires compressed mode for measurements on two additional frequencies.
			- Freq_Specific_Cm: enums.YesNoStatus: NO | YES Indicates whether the UE can apply compressed mode outside of the used frequency bands only to the configured frequencies. This information is relevant only for the dual band operation.
			- Intr_Frq_Cc_Wo_Cm: enums.YesNoStatus: NO | YES Indicates whether the UE requires compressed mode to measure on the frequencies which are configured for HS-DSCH operation and associated with the secondary serving HS-DSCH cells
			- Ceds_Meas: enums.YesNoStatus: NO | YES Indicates whether the UE supports exclusion of cells from intra-frequency detected set measurements
			- Wr_Srq_Fdd_Meas: enums.YesNoStatus: NO | YES Indicates whether the UE is able to perform wideband RSRQ FDD measurements
			- Ev_2_Grep_Sec_Dl_Frq: enums.YesNoStatus: NO | YES Indicates whether the UE supports event 2G reporting on a secondary DL frequency
			- Ext_Rs_Rq_Lwr_Rng: enums.YesNoStatus: NO | YES Indicates whether the UE supports extended RSRQ lower value range
			- Rsrq_On_All_Sym: enums.YesNoStatus: NO | YES Indicates whether the UE supports RSRQ on all symbols
			- Inc_Ue_Cr_Mn_Utra: enums.YesNoStatus: NO | YES Indicates whether the UE supports increased number of UTRA carrier monitoring in connected and idle mode
			- Inc_Ue_Cr_Mn_Eutra: enums.YesNoStatus: NO | YES Indicates whether the UE supports increased number of E-UTRA carrier monitoring in connected and idle mode
			- Enh_Uph_Reporting: enums.YesNoStatus: NO | YES Indicates whether the UE supports enhanced UPH reporting
			- Escce_1_Cop: enums.YesNoStatus: NO | YES Indicates whether the UE supports enhanced serving cell change for event 1c operation
			- Cri_Reporting: enums.YesNoStatus: NO | YES Indicates whether the UE supports cell resellection indication reporting"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Inter_Freq_Detect', enums.YesNoStatus),
			ArgStruct.scalar_enum('Enh_Inter_Freq', enums.YesNoStatus),
			ArgStruct.scalar_enum('Freq_Specific_Cm', enums.YesNoStatus),
			ArgStruct.scalar_enum('Intr_Frq_Cc_Wo_Cm', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ceds_Meas', enums.YesNoStatus),
			ArgStruct.scalar_enum('Wr_Srq_Fdd_Meas', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ev_2_Grep_Sec_Dl_Frq', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ext_Rs_Rq_Lwr_Rng', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rsrq_On_All_Sym', enums.YesNoStatus),
			ArgStruct.scalar_enum('Inc_Ue_Cr_Mn_Utra', enums.YesNoStatus),
			ArgStruct.scalar_enum('Inc_Ue_Cr_Mn_Eutra', enums.YesNoStatus),
			ArgStruct.scalar_enum('Enh_Uph_Reporting', enums.YesNoStatus),
			ArgStruct.scalar_enum('Escce_1_Cop', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cri_Reporting', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Inter_Freq_Detect: enums.YesNoStatus = None
			self.Enh_Inter_Freq: enums.YesNoStatus = None
			self.Freq_Specific_Cm: enums.YesNoStatus = None
			self.Intr_Frq_Cc_Wo_Cm: enums.YesNoStatus = None
			self.Ceds_Meas: enums.YesNoStatus = None
			self.Wr_Srq_Fdd_Meas: enums.YesNoStatus = None
			self.Ev_2_Grep_Sec_Dl_Frq: enums.YesNoStatus = None
			self.Ext_Rs_Rq_Lwr_Rng: enums.YesNoStatus = None
			self.Rsrq_On_All_Sym: enums.YesNoStatus = None
			self.Inc_Ue_Cr_Mn_Utra: enums.YesNoStatus = None
			self.Inc_Ue_Cr_Mn_Eutra: enums.YesNoStatus = None
			self.Enh_Uph_Reporting: enums.YesNoStatus = None
			self.Escce_1_Cop: enums.YesNoStatus = None
			self.Cri_Reporting: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:MEASurement \n
		Snippet: value: ValueStruct = driver.sense.ueCapability.measurement.get_value() \n
		Queries the UE capabilities related to inter-frequency measurements. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:MEASurement?', self.__class__.ValueStruct())

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
