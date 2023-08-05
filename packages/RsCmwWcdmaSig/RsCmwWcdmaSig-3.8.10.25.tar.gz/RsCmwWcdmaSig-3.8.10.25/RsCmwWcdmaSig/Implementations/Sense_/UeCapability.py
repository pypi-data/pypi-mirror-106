from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapability:
	"""UeCapability commands group definition. 29 total commands, 4 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueCapability", core, parent)

	@property
	def codec(self):
		"""codec commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_codec'):
			from .UeCapability_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .UeCapability_.Measurement import Measurement
			self._measurement = Measurement(self._core, self._base)
		return self._measurement

	@property
	def uePosition(self):
		"""uePosition commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_uePosition'):
			from .UeCapability_.UePosition import UePosition
			self._uePosition = UePosition(self._core, self._base)
		return self._uePosition

	@property
	def rfParameter(self):
		"""rfParameter commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfParameter'):
			from .UeCapability_.RfParameter import RfParameter
			self._rfParameter = RfParameter(self._core, self._base)
		return self._rfParameter

	# noinspection PyTypeChecker
	class HsupaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hsupa: enums.YesNoStatus: NO | YES Indicates whether the UE supports HSUPA
			- Phys_Layer_Cat_R_6: int: E-DCH physical layer category of the UE for release 6 call setup Range: 1 to 6
			- Phys_Layer_Cat_R_9: int: E-DCH physical layer category of the UE for release 9 call setup Range: 8 to 9
			- Phys_Layer_Cat_R_7: int: E-DCH physical layer category of the UE for release 7 call setup Range: 7 to 7
			- Phys_Layer_Cat_R_11: int: E-DCH physical layer category of the UE for release 11 call setup
			- Ergch_Bic_Trl: enums.YesNoStatus: NO | YES Indicates whether the UE supports common E-RGCH-based interference control in CELL_FACH state"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Hsupa', enums.YesNoStatus),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_6'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_9'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_7'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_11'),
			ArgStruct.scalar_enum('Ergch_Bic_Trl', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hsupa: enums.YesNoStatus = None
			self.Phys_Layer_Cat_R_6: int = None
			self.Phys_Layer_Cat_R_9: int = None
			self.Phys_Layer_Cat_R_7: int = None
			self.Phys_Layer_Cat_R_11: int = None
			self.Ergch_Bic_Trl: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_hsupa(self) -> HsupaStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:HSUPa \n
		Snippet: value: HsupaStruct = driver.sense.ueCapability.get_hsupa() \n
		Returns UE capability information related to HSUPA. \n
			:return: structure: for return value, see the help for HsupaStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:HSUPa?', self.__class__.HsupaStruct())

	# noinspection PyTypeChecker
	class HsdpaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hs_Pdsch: enums.YesNoStatus: NO | YES Indicates whether the UE supports the HS-PDSCH
			- Dl_Cap_Hsd_Sch: int: Supported DPCH data rate in case an HS-DSCH is configured simultaneously Range: 32 kbit/s to 384 kbit/s, Unit: kbit/s
			- Phys_Layer_Cat_R_5: int: HS-DSCH physical layer category of the UE for release 5 call setup Range: 1 to 24
			- Phys_Layer_Cat_R_7: int: HS-DSCH physical layer category of the UE for release 7 call setup Range: 1 to 24
			- Phys_Layer_Cat_R_8: int: HS-DSCH physical layer category of the UE for release 8 call setup Range: 1 to 24
			- Phys_Layer_Cat_R_9: int: HS-DSCH physical layer category of the UE for release 9 call setup
			- Hsdsch_Drx_Op: enums.YesNoStatus: NO | YES Indicates whether the UE supports the HS-DSCH DRX operation
			- Hs_Scch_Less: enums.YesNoStatus: NO | YES Indicates whether the UE supports the HS-SCCH less operation
			- Cell_Fach: enums.YesNoStatus: NO | YES Indicates whether the UE supports HS-PDSCH in CELL_FACH state
			- Cell_Pc_Hurapch: enums.YesNoStatus: NO | YES Indicates whether the UE supports the HS-PDSCH in CELL_PCH and URA_PCH states
			- Phys_Layer_Cat_R_10: int: HS-DSCH physical layer category of the UE for release 10 call setup Range: 29 to 32
			- Ma_Cehs: enums.YesNoStatus: NO | YES Indicates whether the UE supports the MAC-ehs
			- Phys_Layer_Cat_R_11: int: HS-DSCH physical layer category of the UE for release 11 call setup
			- Hsdpcch_Poff_Ext: enums.YesNoStatus: NO | YES Indicates whether the UE supports the values 9 and 10 of deltaACK, deltaNACK and deltaCQI power offset
			- Drx_Op_2nd_C: enums.YesNoStatus: NO | YES Indicates whether the UE supports HS-DSCH DRX operation with second DRX cycle in CELL_FACH state
			- Nb_Trg_Hsdpcch: enums.YesNoStatus: NO | YES Indicates whether the UE supports NodeB triggered HS-DPCCH transmission in CELL_FACH state
			- Hsdpcch_Ov_Hd_Rd: enums.YesNoStatus: NO | YES Indicates whether the UE supports HS-DPCCH overhead reduction"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Hs_Pdsch', enums.YesNoStatus),
			ArgStruct.scalar_int('Dl_Cap_Hsd_Sch'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_5'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_7'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_8'),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_9'),
			ArgStruct.scalar_enum('Hsdsch_Drx_Op', enums.YesNoStatus),
			ArgStruct.scalar_enum('Hs_Scch_Less', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cell_Fach', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cell_Pc_Hurapch', enums.YesNoStatus),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_10'),
			ArgStruct.scalar_enum('Ma_Cehs', enums.YesNoStatus),
			ArgStruct.scalar_int('Phys_Layer_Cat_R_11'),
			ArgStruct.scalar_enum('Hsdpcch_Poff_Ext', enums.YesNoStatus),
			ArgStruct.scalar_enum('Drx_Op_2nd_C', enums.YesNoStatus),
			ArgStruct.scalar_enum('Nb_Trg_Hsdpcch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Hsdpcch_Ov_Hd_Rd', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hs_Pdsch: enums.YesNoStatus = None
			self.Dl_Cap_Hsd_Sch: int = None
			self.Phys_Layer_Cat_R_5: int = None
			self.Phys_Layer_Cat_R_7: int = None
			self.Phys_Layer_Cat_R_8: int = None
			self.Phys_Layer_Cat_R_9: int = None
			self.Hsdsch_Drx_Op: enums.YesNoStatus = None
			self.Hs_Scch_Less: enums.YesNoStatus = None
			self.Cell_Fach: enums.YesNoStatus = None
			self.Cell_Pc_Hurapch: enums.YesNoStatus = None
			self.Phys_Layer_Cat_R_10: int = None
			self.Ma_Cehs: enums.YesNoStatus = None
			self.Phys_Layer_Cat_R_11: int = None
			self.Hsdpcch_Poff_Ext: enums.YesNoStatus = None
			self.Drx_Op_2nd_C: enums.YesNoStatus = None
			self.Nb_Trg_Hsdpcch: enums.YesNoStatus = None
			self.Hsdpcch_Ov_Hd_Rd: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_hsdpa(self) -> HsdpaStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:HSDPa \n
		Snippet: value: HsdpaStruct = driver.sense.ueCapability.get_hsdpa() \n
		Returns UE capability information related to HSDPA. \n
			:return: structure: for return value, see the help for HsdpaStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:HSDPa?', self.__class__.HsdpaStruct())

	# noinspection PyTypeChecker
	class GeneralStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Release: int: Access stratum release indicator, e.g. Rel. 99, Rel. 5 Range: 5 to 99
			- Batt_Consum_Opt: enums.YesNoStatus: NO | YES Indicates whether the UE benefits from NW-based battery consumption optimization
			- Mimo_Only_Single_Stream: enums.YesNoStatus: NO | YES Indicates whether the UE supports MIMO only single stream
			- Emeas_Report: enums.YesNoStatus: NO | YES Indicates whether the UE supports E-UTRAN measurement reporting
			- Adj_Frq_Mea_No_Cm: enums.YesNoStatus: NO | YES Indicates whether the UE supports adjacent frequency measurements without compressed mode
			- In_Bfrq_Meas_No_Cm: enums.YesNoStatus: NO | YES Indicates whether the UE supports inter-band frequency measurements without compressed mode
			- Sib_11_Bis: enums.YesNoStatus: NO | YES Indicates whether the UE supports system information block 11bis
			- Csg: enums.YesNoStatus: NO | YES Indicates whether the UE supports closed subscriber group (CSG)
			- Csg_Proximity: enums.YesNoStatus: NO | YES Indicates whether the UE supports CSG proximity indication
			- Cell_Tx_Div_Dc: enums.YesNoStatus: NO | YES Indicates whether the UE supports cell-specific TX diversity in dual cell operation
			- Ncell_Si_Acq: enums.YesNoStatus: NO | YES Indicates whether the UE supports a neighbor cell system information acquisition
			- Cs_Vo_Hspa: enums.YesNoStatus: NO | YES Indicates whether the UE supports CS voice over HSPA
			- Dc_Mimo_Diff_Bands: enums.YesNoStatus: NO | YES Indicates whether the UE supports dual cell with MIMO operation in different bands
			- Utran_Anr: enums.YesNoStatus: NO | YES Indicates whether the UE supports ANR
			- Um_Rlc_Re_Est_Re_Cnf: enums.YesNoStatus: NO | YES Indicates whether the UE supports UM RLC reestablishment via reconfiguration
			- Rf_Mfbi: enums.YesNoStatus: NO | YES Indicates whether the UE supports multiple frequency band indicators
			- Reserved: enums.YesNoStatus: NO | YES Reserved for future
			- Ext_Meas: enums.YesNoStatus: NO | YES Indicates whether the UE supports extended measurements
			- Fr_99_Prach: enums.YesNoStatus: NO | YES Indicates whether the UE supports fallback to R99 PRACH in CELL_FACH state and IDLE mode
			- Conc_Deployment: enums.YesNoStatus: NO | YES Indicates whether the UE supports concurrent deployment of 2 ms and 10 ms TTI in a cell in CELL_FACH state and IDLE mode
			- Tti_Align_Harq: enums.YesNoStatus: NO | YES Indicates whether the UE supports TTI alignment and per HARQ process activation and deactivation in CELL_FACH state and IDLE mode
			- Mimodsr_4_X_4: enums.YesNoStatus: NO | YES Indicates whether the UE supports MIMO mode with four transmit antennas only with restriction to dual stream operation
			- Ncmc_Mimo: enums.YesNoStatus: NO | YES Indicates whether the UE supports non-contiguous multi-cell operation on two, three or four cells with single gap in one band with MIMO
			- Dsac_Ppac_Cell_Dch: enums.YesNoStatus: NO | YES Indicates whether the UE supports DSAC and PPAC update in CELL_DCH
			- Acc_Grps_Acc_Ctrl: enums.YesNoStatus: NO | YES Indicates whether the UE supports access groups -based access control
			- En_Tti_Switching: enums.YesNoStatus: NO | YES Indicates whether the UE supports enhanced TTI switching
			- Impl_Grant: enums.YesNoStatus: NO | YES Indicates whether the UE supports implicit grant handling"""
		__meta_args_list = [
			ArgStruct.scalar_int('Release'),
			ArgStruct.scalar_enum('Batt_Consum_Opt', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mimo_Only_Single_Stream', enums.YesNoStatus),
			ArgStruct.scalar_enum('Emeas_Report', enums.YesNoStatus),
			ArgStruct.scalar_enum('Adj_Frq_Mea_No_Cm', enums.YesNoStatus),
			ArgStruct.scalar_enum('In_Bfrq_Meas_No_Cm', enums.YesNoStatus),
			ArgStruct.scalar_enum('Sib_11_Bis', enums.YesNoStatus),
			ArgStruct.scalar_enum('Csg', enums.YesNoStatus),
			ArgStruct.scalar_enum('Csg_Proximity', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cell_Tx_Div_Dc', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ncell_Si_Acq', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cs_Vo_Hspa', enums.YesNoStatus),
			ArgStruct.scalar_enum('Dc_Mimo_Diff_Bands', enums.YesNoStatus),
			ArgStruct.scalar_enum('Utran_Anr', enums.YesNoStatus),
			ArgStruct.scalar_enum('Um_Rlc_Re_Est_Re_Cnf', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rf_Mfbi', enums.YesNoStatus),
			ArgStruct.scalar_enum('Reserved', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ext_Meas', enums.YesNoStatus),
			ArgStruct.scalar_enum('Fr_99_Prach', enums.YesNoStatus),
			ArgStruct.scalar_enum('Conc_Deployment', enums.YesNoStatus),
			ArgStruct.scalar_enum('Tti_Align_Harq', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mimodsr_4_X_4', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ncmc_Mimo', enums.YesNoStatus),
			ArgStruct.scalar_enum('Dsac_Ppac_Cell_Dch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Acc_Grps_Acc_Ctrl', enums.YesNoStatus),
			ArgStruct.scalar_enum('En_Tti_Switching', enums.YesNoStatus),
			ArgStruct.scalar_enum('Impl_Grant', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Release: int = None
			self.Batt_Consum_Opt: enums.YesNoStatus = None
			self.Mimo_Only_Single_Stream: enums.YesNoStatus = None
			self.Emeas_Report: enums.YesNoStatus = None
			self.Adj_Frq_Mea_No_Cm: enums.YesNoStatus = None
			self.In_Bfrq_Meas_No_Cm: enums.YesNoStatus = None
			self.Sib_11_Bis: enums.YesNoStatus = None
			self.Csg: enums.YesNoStatus = None
			self.Csg_Proximity: enums.YesNoStatus = None
			self.Cell_Tx_Div_Dc: enums.YesNoStatus = None
			self.Ncell_Si_Acq: enums.YesNoStatus = None
			self.Cs_Vo_Hspa: enums.YesNoStatus = None
			self.Dc_Mimo_Diff_Bands: enums.YesNoStatus = None
			self.Utran_Anr: enums.YesNoStatus = None
			self.Um_Rlc_Re_Est_Re_Cnf: enums.YesNoStatus = None
			self.Rf_Mfbi: enums.YesNoStatus = None
			self.Reserved: enums.YesNoStatus = None
			self.Ext_Meas: enums.YesNoStatus = None
			self.Fr_99_Prach: enums.YesNoStatus = None
			self.Conc_Deployment: enums.YesNoStatus = None
			self.Tti_Align_Harq: enums.YesNoStatus = None
			self.Mimodsr_4_X_4: enums.YesNoStatus = None
			self.Ncmc_Mimo: enums.YesNoStatus = None
			self.Dsac_Ppac_Cell_Dch: enums.YesNoStatus = None
			self.Acc_Grps_Acc_Ctrl: enums.YesNoStatus = None
			self.En_Tti_Switching: enums.YesNoStatus = None
			self.Impl_Grant: enums.YesNoStatus = None

	def get_general(self) -> GeneralStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:GENeral \n
		Snippet: value: GeneralStruct = driver.sense.ueCapability.get_general() \n
		Returns general UE capability information. \n
			:return: structure: for return value, see the help for GeneralStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:GENeral?', self.__class__.GeneralStruct())

	# noinspection PyTypeChecker
	class MratStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Support_Gsm: enums.YesNoStatus: NO | YES Indicates whether the UE supports GSM
			- Multi_Carrier: enums.YesNoStatus: NO | YES Indicates whether the UE supports multi-carrier mode
			- Utran_Geran: enums.YesNoStatus: NO | YES Indicates whether the UE supports UTRAN to GERAN NACC
			- Handover_Gan: enums.YesNoStatus: NO | YES Indicates whether the UE supports CS handover to GAN
			- Ps_Inter_Rat: enums.YesNoStatus: NO | YES Indicates whether the UE supports Inter-RAT PS handover
			- Cipher_Alg_Uea_0: enums.YesNoStatus: NO | YES Indicates whether the UE supports ciphering algorithm UEA0
			- Cipher_Alg_Uea_1: enums.YesNoStatus: NO | YES Indicates whether the UE supports ciphering algorithm UEA1
			- Integrity_Uia_1: enums.YesNoStatus: NO | YES Indicates whether the UE supports integrity algorithm UIA1
			- Cipher_Alg_Uea_2: enums.YesNoStatus: NO | YES Indicates whether the UE supports ciphering algorithm UEA2
			- Integrity_Uia_2: enums.YesNoStatus: NO | YES Indicates whether the UE supports integrity algorithm UIA2
			- Trgt_Cell_Pre_Cfg: enums.YesNoStatus: NO | YES Indicates whether the UE supports target cell preconfiguration
			- Ps_Handover_Gan: enums.YesNoStatus: NO | YES Indicates whether the UE supports PS handover to GAN
			- Eutra_Fdd: enums.YesNoStatus: NO | YES Indicates whether the UE supports E-UTRA FDD
			- Eutra_Inter_Rat: enums.YesNoStatus: NO | YES Indicates whether the UE supports inter-RAT E-UTRA handover
			- U_2_Eu_Tra_Rrci_Dle: enums.YesNoStatus: NO | YES Indicates whether the UE supports cell reselection from UTRA CELL_PCH or URA_PCH to E-UTRA RRC_IDLE
			- Prio_Res_Utran: enums.YesNoStatus: NO | YES Indicates whether the UE supports priority reselection in UTRAN
			- Eutra_Fdd_Cfch: enums.YesNoStatus: NO | YES Indicates whether the UE supports E-UTRA measurements and reporting for CELL_FACH for E-UTRA FDD
			- Eutra_Tdd_Cdch: enums.YesNoStatus: NO | YES Indicates whether the UE supports E-UTRA measurements and reporting for CELL_FACH for E-UTRA TDD
			- Eutra_Mfbi: enums.YesNoStatus: NO | YES Indicates whether the UE supports E-UTRA multiple frequency band indicator measurements
			- Wlan_Ran_Rules: enums.YesNoStatus: NO | YES Indicates whether the UE supports RAN-assisted WLAN interworking RAN rules
			- Wlan_And_Sf: enums.YesNoStatus: NO | YES Indicates whether the UE supports RAN-assisted WLAN interworking ANDSF policies"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Support_Gsm', enums.YesNoStatus),
			ArgStruct.scalar_enum('Multi_Carrier', enums.YesNoStatus),
			ArgStruct.scalar_enum('Utran_Geran', enums.YesNoStatus),
			ArgStruct.scalar_enum('Handover_Gan', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ps_Inter_Rat', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cipher_Alg_Uea_0', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cipher_Alg_Uea_1', enums.YesNoStatus),
			ArgStruct.scalar_enum('Integrity_Uia_1', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cipher_Alg_Uea_2', enums.YesNoStatus),
			ArgStruct.scalar_enum('Integrity_Uia_2', enums.YesNoStatus),
			ArgStruct.scalar_enum('Trgt_Cell_Pre_Cfg', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ps_Handover_Gan', enums.YesNoStatus),
			ArgStruct.scalar_enum('Eutra_Fdd', enums.YesNoStatus),
			ArgStruct.scalar_enum('Eutra_Inter_Rat', enums.YesNoStatus),
			ArgStruct.scalar_enum('U_2_Eu_Tra_Rrci_Dle', enums.YesNoStatus),
			ArgStruct.scalar_enum('Prio_Res_Utran', enums.YesNoStatus),
			ArgStruct.scalar_enum('Eutra_Fdd_Cfch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Eutra_Tdd_Cdch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Eutra_Mfbi', enums.YesNoStatus),
			ArgStruct.scalar_enum('Wlan_Ran_Rules', enums.YesNoStatus),
			ArgStruct.scalar_enum('Wlan_And_Sf', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Support_Gsm: enums.YesNoStatus = None
			self.Multi_Carrier: enums.YesNoStatus = None
			self.Utran_Geran: enums.YesNoStatus = None
			self.Handover_Gan: enums.YesNoStatus = None
			self.Ps_Inter_Rat: enums.YesNoStatus = None
			self.Cipher_Alg_Uea_0: enums.YesNoStatus = None
			self.Cipher_Alg_Uea_1: enums.YesNoStatus = None
			self.Integrity_Uia_1: enums.YesNoStatus = None
			self.Cipher_Alg_Uea_2: enums.YesNoStatus = None
			self.Integrity_Uia_2: enums.YesNoStatus = None
			self.Trgt_Cell_Pre_Cfg: enums.YesNoStatus = None
			self.Ps_Handover_Gan: enums.YesNoStatus = None
			self.Eutra_Fdd: enums.YesNoStatus = None
			self.Eutra_Inter_Rat: enums.YesNoStatus = None
			self.U_2_Eu_Tra_Rrci_Dle: enums.YesNoStatus = None
			self.Prio_Res_Utran: enums.YesNoStatus = None
			self.Eutra_Fdd_Cfch: enums.YesNoStatus = None
			self.Eutra_Tdd_Cdch: enums.YesNoStatus = None
			self.Eutra_Mfbi: enums.YesNoStatus = None
			self.Wlan_Ran_Rules: enums.YesNoStatus = None
			self.Wlan_And_Sf: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_mrat(self) -> MratStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:MRAT \n
		Snippet: value: MratStruct = driver.sense.ueCapability.get_mrat() \n
		Returns UE capability information indicating the radio access technologies (RAT) that the UE supports. \n
			:return: structure: for return value, see the help for MratStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:MRAT?', self.__class__.MratStruct())

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.UtraMode:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:MMODe \n
		Snippet: value: enums.UtraMode = driver.sense.ueCapability.get_mmode() \n
		Returns UE capability information indicating whether the UE supports UTRA FDD or TDD or both. \n
			:return: utra: FDD | TDD | BOTH
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UECapability:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.UtraMode)

	# noinspection PyTypeChecker
	class PupLinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Simult_Transp_Ch: int: Maximum number of uplink transport channels that the UE is capable to process simultaneously, not considering the rate of each transport channel Range: 4 to 32
			- Simult_Cc_Tr_Ch: int: Maximum number of uplink coded composite transport channels (CCTrCH) that the UE is capable to process simultaneously Range: 1 to 8
			- Tti_Transp_Block: int: Maximum total number of transport blocks transmitted within transmission time intervals (TTI) that start at the same time Range: 4 to 512
			- Number_Of_Tfc: int: Maximum number of transport format combinations (TFC) in an uplink transport format combination set that the UE can store Range: 16 to 1024
			- Number_Of_Tf: int: Maximum number of uplink transport formats (TF) that the UE can store, where all transport formats for all uplink transport channels are counted Range: 32 to 1024
			- Turbo_Decoding: enums.YesNoStatus: NO | YES Support of turbo decoding
			- Tx_Bits_All: int: Maximum number of bits of all transport blocks being transmitted at an arbitrary time instant. All bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Tx_Bits_Conv: int: Maximum number of bits of all transport blocks being transmitted at an arbitrary time instant. Only convolutionally coded bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Tx_Bits_Turbo: int: Maximum number of bits of all transport blocks being transmitted at an arbitrary time instant. Only turbo coded bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Dpd_Ch_Bits: int: Maximum number of DPDCH bits the UE can transmit in 10 ms. The value applies to UE operation in non-compressed mode (if the value is 9600) or in both compressed and non-compressed mode (if the value is ≥9600) . Range: 600 bits to 57600 bits, Unit: bits
			- Dpcch_Dtx: enums.YesNoStatus: NO | YES Support of discontinuous uplink DPCCH transmission
			- Slot_Format_4: enums.YesNoStatus: NO | YES Support of DPCCH slot format 4
			- Common_Edch: enums.YesNoStatus: NO | YES Support of common E-DCH
			- Edpcch_Pwr_Boost: enums.YesNoStatus: NO | YES Support of E-DPCCH power boosting
			- Edpdch_Pwr_Interpol: enums.YesNoStatus: NO | YES Support of E-DPCCH power interpolation
			- Dtx_Enh: enums.YesNoStatus: NO | YES Support of DTX enhancements
			- Srv_Edc_Hcd_Op: enums.YesNoStatus: NO | YES Support of FDD serving E-DCH cell decoupling operation
			- Rlwo_Fdpch: enums.YesNoStatus: NO | YES Support of FDD radio link without DPCH or F-DPCH"""
		__meta_args_list = [
			ArgStruct.scalar_int('Simult_Transp_Ch'),
			ArgStruct.scalar_int('Simult_Cc_Tr_Ch'),
			ArgStruct.scalar_int('Tti_Transp_Block'),
			ArgStruct.scalar_int('Number_Of_Tfc'),
			ArgStruct.scalar_int('Number_Of_Tf'),
			ArgStruct.scalar_enum('Turbo_Decoding', enums.YesNoStatus),
			ArgStruct.scalar_int('Tx_Bits_All'),
			ArgStruct.scalar_int('Tx_Bits_Conv'),
			ArgStruct.scalar_int('Tx_Bits_Turbo'),
			ArgStruct.scalar_int('Dpd_Ch_Bits'),
			ArgStruct.scalar_enum('Dpcch_Dtx', enums.YesNoStatus),
			ArgStruct.scalar_enum('Slot_Format_4', enums.YesNoStatus),
			ArgStruct.scalar_enum('Common_Edch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Edpcch_Pwr_Boost', enums.YesNoStatus),
			ArgStruct.scalar_enum('Edpdch_Pwr_Interpol', enums.YesNoStatus),
			ArgStruct.scalar_enum('Dtx_Enh', enums.YesNoStatus),
			ArgStruct.scalar_enum('Srv_Edc_Hcd_Op', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rlwo_Fdpch', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Simult_Transp_Ch: int = None
			self.Simult_Cc_Tr_Ch: int = None
			self.Tti_Transp_Block: int = None
			self.Number_Of_Tfc: int = None
			self.Number_Of_Tf: int = None
			self.Turbo_Decoding: enums.YesNoStatus = None
			self.Tx_Bits_All: int = None
			self.Tx_Bits_Conv: int = None
			self.Tx_Bits_Turbo: int = None
			self.Dpd_Ch_Bits: int = None
			self.Dpcch_Dtx: enums.YesNoStatus = None
			self.Slot_Format_4: enums.YesNoStatus = None
			self.Common_Edch: enums.YesNoStatus = None
			self.Edpcch_Pwr_Boost: enums.YesNoStatus = None
			self.Edpdch_Pwr_Interpol: enums.YesNoStatus = None
			self.Dtx_Enh: enums.YesNoStatus = None
			self.Srv_Edc_Hcd_Op: enums.YesNoStatus = None
			self.Rlwo_Fdpch: enums.YesNoStatus = None

	def get_pup_link(self) -> PupLinkStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:PUPLink \n
		Snippet: value: PupLinkStruct = driver.sense.ueCapability.get_pup_link() \n
		Returns UE capability information describing the capacity of the UE to process and store uplink channels. \n
			:return: structure: for return value, see the help for PupLinkStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:PUPLink?', self.__class__.PupLinkStruct())

	# noinspection PyTypeChecker
	class PdownlinkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Simult_Transp_Ch: int: Maximum number of downlink transport channels that the UE is capable to process simultaneously, not considering the rate of each transport channel Range: 4 to 32
			- Simult_Cc_Tr_Ch: int: Maximum number of downlink coded composite transport channels (CCTrCH) that the UE is capable to process simultaneously. Interpret CCTrCH as consisting of DCH, FACH or DSCH. Range: 1 to 8
			- Tti_Transp_Block: int: Maximum total number of transport blocks received within transmission time intervals (TTIs) that end within the same 10 ms interval. This value includes all transport blocks that are to be simultaneously received by the UE on DCH, FACH, PCH and DSCH transport channels. Range: 4 to 512
			- Number_Of_Tfc: int: Maximum number of transport format combinations (TFC) in a downlink transport format combination set that the UE can store Range: 16 to 1024
			- Number_Of_Tf: int: Maximum number of downlink transport formats (TF) that the UE can store, where all transport formats for all downlink transport channels are counted Range: 32 to 1024
			- Turbo_Decoding: enums.YesNoStatus: NO | YES Support of turbo decoding
			- Rx_Bits_All: int: Maximum number of bits of all transport blocks being received at an arbitrary time instant. All bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Rx_Bits_Conv: int: Maximum number of bits of all transport blocks being received at an arbitrary time instant. Only convolutionally coded bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Rx_Bits_Turbo: int: Maximum number of bits of all transport blocks being received at an arbitrary time instant. Only turbo coded bits are considered. Range: 640 bits to 163840 bits, Unit: bits
			- Dpcch_Codes: int: Maximum number of DPCH codes to be simultaneously received. For DPCH in soft/softer handover, each DPCH is only calculated once. The capability does not include codes used for S-CCPCH. Range: 1 to 8
			- Physical_Ch_Bits: int: Maximum number of physical channel bits received in any 10 ms interval (DPCH, PDSCH, S-CCPCH) . For DPCH in soft/softer handover, each DPCH is only calculated once. Range: 600 bits to 76800 bits, Unit: bits
			- Sf_512: enums.YesNoStatus: NO | YES Support of spreading factor (SF) 512 in downlink.
			- Ma_Ciis: enums.YesNoStatus: NO | YES Support of MAC-i/is entity handling E-DCH
			- Fdpch: enums.YesNoStatus: NO | YES Support of FDD physical channel F-DPCH
			- Enhanced_Fdpch: enums.YesNoStatus: NO | YES Support of FDD physical channel enhanced F-DPCH
			- Dc_Henh: enums.DchEnhanced: NO | BASic | FULL Support of DCH enhancements
			- Simult_Dch_Enh_Cm: enums.YesNoStatus: NO | YES Support of simultaneous DCH enhancements and CM
			- Sdch_Enh_Dpcch: enums.YesNoStatus: NO | YES Support of simultaneous DCH enhancements and DPCCH DTX
			- Drx_Enh: enums.YesNoStatus: NO | YES Support of DRX enhancements
			- Dpcch_2_Trx: enums.YesNoStatus: NO | YES Support of FDD DPCCH2 transmission
			- Ftpi_Ch_Feedback: enums.YesNoStatus: NO | YES Support of FDD F-TPICH feedback from the multiflow assisting cell"""
		__meta_args_list = [
			ArgStruct.scalar_int('Simult_Transp_Ch'),
			ArgStruct.scalar_int('Simult_Cc_Tr_Ch'),
			ArgStruct.scalar_int('Tti_Transp_Block'),
			ArgStruct.scalar_int('Number_Of_Tfc'),
			ArgStruct.scalar_int('Number_Of_Tf'),
			ArgStruct.scalar_enum('Turbo_Decoding', enums.YesNoStatus),
			ArgStruct.scalar_int('Rx_Bits_All'),
			ArgStruct.scalar_int('Rx_Bits_Conv'),
			ArgStruct.scalar_int('Rx_Bits_Turbo'),
			ArgStruct.scalar_int('Dpcch_Codes'),
			ArgStruct.scalar_int('Physical_Ch_Bits'),
			ArgStruct.scalar_enum('Sf_512', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ma_Ciis', enums.YesNoStatus),
			ArgStruct.scalar_enum('Fdpch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Enhanced_Fdpch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Dc_Henh', enums.DchEnhanced),
			ArgStruct.scalar_enum('Simult_Dch_Enh_Cm', enums.YesNoStatus),
			ArgStruct.scalar_enum('Sdch_Enh_Dpcch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Drx_Enh', enums.YesNoStatus),
			ArgStruct.scalar_enum('Dpcch_2_Trx', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ftpi_Ch_Feedback', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Simult_Transp_Ch: int = None
			self.Simult_Cc_Tr_Ch: int = None
			self.Tti_Transp_Block: int = None
			self.Number_Of_Tfc: int = None
			self.Number_Of_Tf: int = None
			self.Turbo_Decoding: enums.YesNoStatus = None
			self.Rx_Bits_All: int = None
			self.Rx_Bits_Conv: int = None
			self.Rx_Bits_Turbo: int = None
			self.Dpcch_Codes: int = None
			self.Physical_Ch_Bits: int = None
			self.Sf_512: enums.YesNoStatus = None
			self.Ma_Ciis: enums.YesNoStatus = None
			self.Fdpch: enums.YesNoStatus = None
			self.Enhanced_Fdpch: enums.YesNoStatus = None
			self.Dc_Henh: enums.DchEnhanced = None
			self.Simult_Dch_Enh_Cm: enums.YesNoStatus = None
			self.Sdch_Enh_Dpcch: enums.YesNoStatus = None
			self.Drx_Enh: enums.YesNoStatus = None
			self.Dpcch_2_Trx: enums.YesNoStatus = None
			self.Ftpi_Ch_Feedback: enums.YesNoStatus = None

	def get_pdownlink(self) -> PdownlinkStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:PDOWnlink \n
		Snippet: value: PdownlinkStruct = driver.sense.ueCapability.get_pdownlink() \n
		Returns UE capability information describing the capacity of the UE to process and store downlink channels. \n
			:return: structure: for return value, see the help for PdownlinkStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:PDOWnlink?', self.__class__.PdownlinkStruct())

	# noinspection PyTypeChecker
	class RlcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Am_Buffer_Size: int: Maximum total buffer size across all RLC AM entities supported by the UE Range: 10 to 1000
			- Max_Rlc_Window: int: Maximum RLC window size supported by the UE Range: 0 to 4095
			- Am_Entities: int: Maximum number of AM entities supported by the UE Range: 3 to 30
			- Two_Logical_Ch: enums.YesNoStatus: NO | YES Support of AM entity configurated with two logical channels"""
		__meta_args_list = [
			ArgStruct.scalar_int('Am_Buffer_Size'),
			ArgStruct.scalar_int('Max_Rlc_Window'),
			ArgStruct.scalar_int('Am_Entities'),
			ArgStruct.scalar_enum('Two_Logical_Ch', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Am_Buffer_Size: int = None
			self.Max_Rlc_Window: int = None
			self.Am_Entities: int = None
			self.Two_Logical_Ch: enums.YesNoStatus = None

	def get_rlc(self) -> RlcStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RLC \n
		Snippet: value: RlcStruct = driver.sense.ueCapability.get_rlc() \n
		Returns UE capability information indicating in which way the UE supports the radio link control acknowledged mode (RLC
		AM) . \n
			:return: structure: for return value, see the help for RlcStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:RLC?', self.__class__.RlcStruct())

	# noinspection PyTypeChecker
	class PdcpStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Srns: enums.YesNoStatus: NO | YES Support of lossless SRNS relocation
			- Rfc_2507: enums.YesNoStatus: NO | YES Support of IP header compression according to RFC 2507
			- Rfc_3095: enums.YesNoStatus: NO | YES Support of robust header compression according to RFC 3095
			- Rfc_3095_Ctx_Reloc: enums.YesNoStatus: NO | YES Support of context relocation applied to the RFC 3095 header compression protocol
			- Header_Comp: int: Maximum header compression context size supported by the UE. This parameter is only applicable if the UE supports header compression according to RFC 2507 Range: 1024 to 131072
			- Max_Rohc: int: Maximum number of header compression context sessions supported by the UE. This parameter is only applicable if the UE supports header compression according to RFC3095. Range: 2 to 16384
			- Reverse_Decomp: int: Number of packets that can be reverse decompressed by the decompressor in the UE Range: 0 to 65535
			- Pdu_Size_Change: enums.YesNoStatus: NO | YES Support of lossless DL RLC PDU size change
			- Rfc_3095_Rspace: int: 16384 | 32768 | 65536 | 131072 Support of RFC 3095 relocation space Unit: byte"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Srns', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rfc_2507', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rfc_3095', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rfc_3095_Ctx_Reloc', enums.YesNoStatus),
			ArgStruct.scalar_int('Header_Comp'),
			ArgStruct.scalar_int('Max_Rohc'),
			ArgStruct.scalar_int('Reverse_Decomp'),
			ArgStruct.scalar_enum('Pdu_Size_Change', enums.YesNoStatus),
			ArgStruct.scalar_int('Rfc_3095_Rspace')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Srns: enums.YesNoStatus = None
			self.Rfc_2507: enums.YesNoStatus = None
			self.Rfc_3095: enums.YesNoStatus = None
			self.Rfc_3095_Ctx_Reloc: enums.YesNoStatus = None
			self.Header_Comp: int = None
			self.Max_Rohc: int = None
			self.Reverse_Decomp: int = None
			self.Pdu_Size_Change: enums.YesNoStatus = None
			self.Rfc_3095_Rspace: int = None

	# noinspection PyTypeChecker
	def get_pdcp(self) -> PdcpStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:PDCP \n
		Snippet: value: PdcpStruct = driver.sense.ueCapability.get_pdcp() \n
		Returns UE capability information indicating in which way the UE supports the packet data convergence protocol (PDCP)
		described in 3GPP TS 25.323 \n
			:return: structure: for return value, see the help for PdcpStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:PDCP?', self.__class__.PdcpStruct())

	# noinspection PyTypeChecker
	class ImsVoiceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Vo_Utra_Ps_Hs: enums.YesNoStatus: NO | YES Indicates if a UE supports IMS voice over UTRA PS HSPA connections
			- Srvcc_Utra_Utra: enums.YesNoStatus: NO | YES Indicates if a UE supports the single radio voice call continuity (SRVCC) from UTRA PS HS to UTRA CS
			- Srvcc_Utra_Geran: enums.YesNoStatus: NO | YES Indicates if a UE supports SRVCC from UTRA PS HS to GERAN CS
			- Rs_Rvcc_Ucs_Eu_Fdd: enums.YesNoStatus: NO | YES Indicates whether the UE supports reverse single radio voice call continuity (rSRVCC) handover from UTRA CS to EUTRA FDD
			- Rs_Rvcc_Ucs_Eu_Tdd: enums.YesNoStatus: NO | YES Indicates whether the UE supports rSRVCC handover from UTRA CS to EUTRA TDD"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Vo_Utra_Ps_Hs', enums.YesNoStatus),
			ArgStruct.scalar_enum('Srvcc_Utra_Utra', enums.YesNoStatus),
			ArgStruct.scalar_enum('Srvcc_Utra_Geran', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rs_Rvcc_Ucs_Eu_Fdd', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rs_Rvcc_Ucs_Eu_Tdd', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Vo_Utra_Ps_Hs: enums.YesNoStatus = None
			self.Srvcc_Utra_Utra: enums.YesNoStatus = None
			self.Srvcc_Utra_Geran: enums.YesNoStatus = None
			self.Rs_Rvcc_Ucs_Eu_Fdd: enums.YesNoStatus = None
			self.Rs_Rvcc_Ucs_Eu_Tdd: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_ims_voice(self) -> ImsVoiceStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:IMSVoice \n
		Snippet: value: ImsVoiceStruct = driver.sense.ueCapability.get_ims_voice() \n
		Indicates the IMS voice capability of the UE as defined in 3GPP TS 25.331, section 10.3.3.14b. \n
			:return: structure: for return value, see the help for ImsVoiceStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:IMSVoice?', self.__class__.ImsVoiceStruct())

	def clone(self) -> 'UeCapability':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapability(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
