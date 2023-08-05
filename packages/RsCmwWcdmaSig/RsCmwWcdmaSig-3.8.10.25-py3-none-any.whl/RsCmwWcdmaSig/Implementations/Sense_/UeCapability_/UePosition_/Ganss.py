from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ganss:
	"""Ganss commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ganss", core, parent)

	# noinspection PyTypeChecker
	class GalileoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if a UE supports the navigation standard indicated by the last mnemonic
			- Mode: enums.UeNaviSupport: NONE | NETWork | UE | NUE Indicates if a UE supports the 'network-based' and/or 'UE-based' navigation standard indicated by the last mnemonic
			- Signal_Id: int: The GANSS signal ID encodes the identification of the signal for each GANSS. It depends on the GANSS ID as specified in 3GPP TS 25.331, section 10.3.3.45a.
			- Signal_Ids_Ext: int: GANSS signal IDs extension specifies the UE capability to measure on more than one GANSS signal and which signals are supported (see 3GPP TS 25.331, section 10.3.3.45, note 2) .
			- Timing_Cell_Frms: enums.YesNoStatus: NO | YES Support of GANSS timing of cell frames measurement
			- Carrier_Phase: enums.YesNoStatus: NO | YES Support of GANSS carrier-phase measurement
			- Non_Native_Assist: enums.YesNoStatus: NO | YES Support of non-native assistance choices
			- Sbas_Id: int: Coding is specified in 3GPP TS 25.331, section 10.3.3.45, note 1. This parameter is only available for SBAS standard."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mode', enums.UeNaviSupport),
			ArgStruct.scalar_int('Signal_Id'),
			ArgStruct.scalar_int('Signal_Ids_Ext'),
			ArgStruct.scalar_enum('Timing_Cell_Frms', enums.YesNoStatus),
			ArgStruct.scalar_enum('Carrier_Phase', enums.YesNoStatus),
			ArgStruct.scalar_enum('Non_Native_Assist', enums.YesNoStatus),
			ArgStruct.scalar_int('Sbas_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Mode: enums.UeNaviSupport = None
			self.Signal_Id: int = None
			self.Signal_Ids_Ext: int = None
			self.Timing_Cell_Frms: enums.YesNoStatus = None
			self.Carrier_Phase: enums.YesNoStatus = None
			self.Non_Native_Assist: enums.YesNoStatus = None
			self.Sbas_Id: int = None

	# noinspection PyTypeChecker
	def get_galileo(self) -> GalileoStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs:GALileo \n
		Snippet: value: GalileoStruct = driver.sense.ueCapability.uePosition.ganss.get_galileo() \n
		Returns UE capability information related to the navigation standards indicated by the last mnemonic: Galileo, global
		navigation satellite system (GLONASS) , modernized global positioning system (GPS) , quasi-zenith satellite system (QZSS)
		, satellite-based augmentation system (SBAS) \n
			:return: structure: for return value, see the help for GalileoStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs:GALileo?', self.__class__.GalileoStruct())

	# noinspection PyTypeChecker
	class SbasStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if a UE supports the navigation standard indicated by the last mnemonic
			- Mode: enums.UeNaviSupport: NONE | NETWork | UE | NUE Indicates if a UE supports the 'network-based' and/or 'UE-based' navigation standard indicated by the last mnemonic
			- Signal_Id: int: The GANSS signal ID encodes the identification of the signal for each GANSS. It depends on the GANSS ID as specified in 3GPP TS 25.331, section 10.3.3.45a.
			- Signal_Ids_Ext: int: GANSS signal IDs extension specifies the UE capability to measure on more than one GANSS signal and which signals are supported (see 3GPP TS 25.331, section 10.3.3.45, note 2) .
			- Timing_Cell_Frms: enums.YesNoStatus: NO | YES Support of GANSS timing of cell frames measurement
			- Carrier_Phase: enums.YesNoStatus: NO | YES Support of GANSS carrier-phase measurement
			- Non_Native_Assist: enums.YesNoStatus: NO | YES Support of non-native assistance choices
			- Sbas_Id: int: Coding is specified in 3GPP TS 25.331, section 10.3.3.45, note 1. This parameter is only available for SBAS standard."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mode', enums.UeNaviSupport),
			ArgStruct.scalar_int('Signal_Id'),
			ArgStruct.scalar_int('Signal_Ids_Ext'),
			ArgStruct.scalar_enum('Timing_Cell_Frms', enums.YesNoStatus),
			ArgStruct.scalar_enum('Carrier_Phase', enums.YesNoStatus),
			ArgStruct.scalar_enum('Non_Native_Assist', enums.YesNoStatus),
			ArgStruct.scalar_int('Sbas_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Mode: enums.UeNaviSupport = None
			self.Signal_Id: int = None
			self.Signal_Ids_Ext: int = None
			self.Timing_Cell_Frms: enums.YesNoStatus = None
			self.Carrier_Phase: enums.YesNoStatus = None
			self.Non_Native_Assist: enums.YesNoStatus = None
			self.Sbas_Id: int = None

	# noinspection PyTypeChecker
	def get_sbas(self) -> SbasStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs:SBAS \n
		Snippet: value: SbasStruct = driver.sense.ueCapability.uePosition.ganss.get_sbas() \n
		Returns UE capability information related to the navigation standards indicated by the last mnemonic: Galileo, global
		navigation satellite system (GLONASS) , modernized global positioning system (GPS) , quasi-zenith satellite system (QZSS)
		, satellite-based augmentation system (SBAS) \n
			:return: structure: for return value, see the help for SbasStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs:SBAS?', self.__class__.SbasStruct())

	# noinspection PyTypeChecker
	class MgpsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if a UE supports the navigation standard indicated by the last mnemonic
			- Mode: enums.UeNaviSupport: NONE | NETWork | UE | NUE Indicates if a UE supports the 'network-based' and/or 'UE-based' navigation standard indicated by the last mnemonic
			- Signal_Id: int: The GANSS signal ID encodes the identification of the signal for each GANSS. It depends on the GANSS ID as specified in 3GPP TS 25.331, section 10.3.3.45a.
			- Signal_Ids_Ext: int: GANSS signal IDs extension specifies the UE capability to measure on more than one GANSS signal and which signals are supported (see 3GPP TS 25.331, section 10.3.3.45, note 2) .
			- Timing_Cell_Frms: enums.YesNoStatus: NO | YES Support of GANSS timing of cell frames measurement
			- Carrier_Phase: enums.YesNoStatus: NO | YES Support of GANSS carrier-phase measurement
			- Non_Native_Assist: enums.YesNoStatus: NO | YES Support of non-native assistance choices
			- Sbas_Id: int: Coding is specified in 3GPP TS 25.331, section 10.3.3.45, note 1. This parameter is only available for SBAS standard."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mode', enums.UeNaviSupport),
			ArgStruct.scalar_int('Signal_Id'),
			ArgStruct.scalar_int('Signal_Ids_Ext'),
			ArgStruct.scalar_enum('Timing_Cell_Frms', enums.YesNoStatus),
			ArgStruct.scalar_enum('Carrier_Phase', enums.YesNoStatus),
			ArgStruct.scalar_enum('Non_Native_Assist', enums.YesNoStatus),
			ArgStruct.scalar_int('Sbas_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Mode: enums.UeNaviSupport = None
			self.Signal_Id: int = None
			self.Signal_Ids_Ext: int = None
			self.Timing_Cell_Frms: enums.YesNoStatus = None
			self.Carrier_Phase: enums.YesNoStatus = None
			self.Non_Native_Assist: enums.YesNoStatus = None
			self.Sbas_Id: int = None

	# noinspection PyTypeChecker
	def get_mgps(self) -> MgpsStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs:MGPS \n
		Snippet: value: MgpsStruct = driver.sense.ueCapability.uePosition.ganss.get_mgps() \n
		Returns UE capability information related to the navigation standards indicated by the last mnemonic: Galileo, global
		navigation satellite system (GLONASS) , modernized global positioning system (GPS) , quasi-zenith satellite system (QZSS)
		, satellite-based augmentation system (SBAS) \n
			:return: structure: for return value, see the help for MgpsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs:MGPS?', self.__class__.MgpsStruct())

	# noinspection PyTypeChecker
	class QzssStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if a UE supports the navigation standard indicated by the last mnemonic
			- Mode: enums.UeNaviSupport: NONE | NETWork | UE | NUE Indicates if a UE supports the 'network-based' and/or 'UE-based' navigation standard indicated by the last mnemonic
			- Signal_Id: int: The GANSS signal ID encodes the identification of the signal for each GANSS. It depends on the GANSS ID as specified in 3GPP TS 25.331, section 10.3.3.45a.
			- Signal_Ids_Ext: int: GANSS signal IDs extension specifies the UE capability to measure on more than one GANSS signal and which signals are supported (see 3GPP TS 25.331, section 10.3.3.45, note 2) .
			- Timing_Cell_Frms: enums.YesNoStatus: NO | YES Support of GANSS timing of cell frames measurement
			- Carrier_Phase: enums.YesNoStatus: NO | YES Support of GANSS carrier-phase measurement
			- Non_Native_Assist: enums.YesNoStatus: NO | YES Support of non-native assistance choices
			- Sbas_Id: int: Coding is specified in 3GPP TS 25.331, section 10.3.3.45, note 1. This parameter is only available for SBAS standard."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mode', enums.UeNaviSupport),
			ArgStruct.scalar_int('Signal_Id'),
			ArgStruct.scalar_int('Signal_Ids_Ext'),
			ArgStruct.scalar_enum('Timing_Cell_Frms', enums.YesNoStatus),
			ArgStruct.scalar_enum('Carrier_Phase', enums.YesNoStatus),
			ArgStruct.scalar_enum('Non_Native_Assist', enums.YesNoStatus),
			ArgStruct.scalar_int('Sbas_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Mode: enums.UeNaviSupport = None
			self.Signal_Id: int = None
			self.Signal_Ids_Ext: int = None
			self.Timing_Cell_Frms: enums.YesNoStatus = None
			self.Carrier_Phase: enums.YesNoStatus = None
			self.Non_Native_Assist: enums.YesNoStatus = None
			self.Sbas_Id: int = None

	# noinspection PyTypeChecker
	def get_qzss(self) -> QzssStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs:QZSS \n
		Snippet: value: QzssStruct = driver.sense.ueCapability.uePosition.ganss.get_qzss() \n
		Returns UE capability information related to the navigation standards indicated by the last mnemonic: Galileo, global
		navigation satellite system (GLONASS) , modernized global positioning system (GPS) , quasi-zenith satellite system (QZSS)
		, satellite-based augmentation system (SBAS) \n
			:return: structure: for return value, see the help for QzssStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs:QZSS?', self.__class__.QzssStruct())

	# noinspection PyTypeChecker
	class GlonassStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if a UE supports the navigation standard indicated by the last mnemonic
			- Mode: enums.UeNaviSupport: NONE | NETWork | UE | NUE Indicates if a UE supports the 'network-based' and/or 'UE-based' navigation standard indicated by the last mnemonic
			- Signal_Id: int: The GANSS signal ID encodes the identification of the signal for each GANSS. It depends on the GANSS ID as specified in 3GPP TS 25.331, section 10.3.3.45a.
			- Signal_Ids_Ext: int: GANSS signal IDs extension specifies the UE capability to measure on more than one GANSS signal and which signals are supported (see 3GPP TS 25.331, section 10.3.3.45, note 2) .
			- Timing_Cell_Frms: enums.YesNoStatus: NO | YES Support of GANSS timing of cell frames measurement
			- Carrier_Phase: enums.YesNoStatus: NO | YES Support of GANSS carrier-phase measurement
			- Non_Native_Assist: enums.YesNoStatus: NO | YES Support of non-native assistance choices
			- Sbas_Id: int: Coding is specified in 3GPP TS 25.331, section 10.3.3.45, note 1. This parameter is only available for SBAS standard."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Mode', enums.UeNaviSupport),
			ArgStruct.scalar_int('Signal_Id'),
			ArgStruct.scalar_int('Signal_Ids_Ext'),
			ArgStruct.scalar_enum('Timing_Cell_Frms', enums.YesNoStatus),
			ArgStruct.scalar_enum('Carrier_Phase', enums.YesNoStatus),
			ArgStruct.scalar_enum('Non_Native_Assist', enums.YesNoStatus),
			ArgStruct.scalar_int('Sbas_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Mode: enums.UeNaviSupport = None
			self.Signal_Id: int = None
			self.Signal_Ids_Ext: int = None
			self.Timing_Cell_Frms: enums.YesNoStatus = None
			self.Carrier_Phase: enums.YesNoStatus = None
			self.Non_Native_Assist: enums.YesNoStatus = None
			self.Sbas_Id: int = None

	# noinspection PyTypeChecker
	def get_glonass(self) -> GlonassStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs:GLONass \n
		Snippet: value: GlonassStruct = driver.sense.ueCapability.uePosition.ganss.get_glonass() \n
		Returns UE capability information related to the navigation standards indicated by the last mnemonic: Galileo, global
		navigation satellite system (GLONASS) , modernized global positioning system (GPS) , quasi-zenith satellite system (QZSS)
		, satellite-based augmentation system (SBAS) \n
			:return: structure: for return value, see the help for GlonassStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs:GLONass?', self.__class__.GlonassStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Galileo: enums.YesNoStatus: NO | YES Indicates if a UE supports Galileo standard
			- Sbas: enums.YesNoStatus: NO | YES Indicates if a UE supports the satellite-based augmentation system
			- Modernized_Gps: enums.YesNoStatus: NO | YES Indicates if a UE supports the modernized global positioning system
			- Qzss: enums.YesNoStatus: NO | YES Indicates if a UE supports the quasi-zenith satellite system
			- Glonass: enums.YesNoStatus: NO | YES Indicates if a UE supports the global navigation satellite system"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Galileo', enums.YesNoStatus),
			ArgStruct.scalar_enum('Sbas', enums.YesNoStatus),
			ArgStruct.scalar_enum('Modernized_Gps', enums.YesNoStatus),
			ArgStruct.scalar_enum('Qzss', enums.YesNoStatus),
			ArgStruct.scalar_enum('Glonass', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Galileo: enums.YesNoStatus = None
			self.Sbas: enums.YesNoStatus = None
			self.Modernized_Gps: enums.YesNoStatus = None
			self.Qzss: enums.YesNoStatus = None
			self.Glonass: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition:GANSs \n
		Snippet: value: ValueStruct = driver.sense.ueCapability.uePosition.ganss.get_value() \n
		Returns UE capability information related to the Galileo and additional navigation satellite systems (GANSS) . \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition:GANSs?', self.__class__.ValueStruct())
