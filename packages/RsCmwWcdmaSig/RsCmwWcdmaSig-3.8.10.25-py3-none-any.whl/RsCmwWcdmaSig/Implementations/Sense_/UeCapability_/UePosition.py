from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePosition:
	"""UePosition commands group definition. 7 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uePosition", core, parent)

	@property
	def ganss(self):
		"""ganss commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_ganss'):
			from .UePosition_.Ganss import Ganss
			self._ganss = Ganss(self._core, self._base)
		return self._ganss

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Location_Method: enums.YesNoStatus: NO | YES Indicates if a UE can measure its location by some means unrelated to UTRAN (e.g. if the UE has access to a standalone GPS receiver)
			- Network_Agps: enums.NetworkAndGps: NONE | NETWork | UE | BOTH Indicates if a UE supports the assisted GPS schemes network-based and/or UE-based
			- Ref_Time_Gps: enums.YesNoStatus: NO | YES Indicates UE capability to measure GPS reference time as defined in 3GPP TS 25.215
			- Ipdl: enums.YesNoStatus: NO | YES Indicates UE capability to use idle periods in the downlink (IPDL) to enhance its 'SFN-SFN observed time difference – type 2' measurement
			- Otdoa: enums.YesNoStatus: NO | YES Indicates if a UE supports the observed time difference of arrival (OTDOA) UE-based schemes
			- Rx_Tx_Time_Diff: enums.YesNoStatus: NO | YES Indicates UE capability to measure the Rx-Tx time difference type 2
			- Cell_Ur_Apch: enums.YesNoStatus: NO | YES Indicates whether the UE positioning measurements using the assisted GPS method are valid in CELL_PCH and URA_PCH RRC states
			- Sfn_Sfn_Time_Diff: enums.YesNoStatus: NO | YES Indicates UE capability to perform the SFN-SFN observed time difference type 2 measurement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Location_Method', enums.YesNoStatus),
			ArgStruct.scalar_enum('Network_Agps', enums.NetworkAndGps),
			ArgStruct.scalar_enum('Ref_Time_Gps', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ipdl', enums.YesNoStatus),
			ArgStruct.scalar_enum('Otdoa', enums.YesNoStatus),
			ArgStruct.scalar_enum('Rx_Tx_Time_Diff', enums.YesNoStatus),
			ArgStruct.scalar_enum('Cell_Ur_Apch', enums.YesNoStatus),
			ArgStruct.scalar_enum('Sfn_Sfn_Time_Diff', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Location_Method: enums.YesNoStatus = None
			self.Network_Agps: enums.NetworkAndGps = None
			self.Ref_Time_Gps: enums.YesNoStatus = None
			self.Ipdl: enums.YesNoStatus = None
			self.Otdoa: enums.YesNoStatus = None
			self.Rx_Tx_Time_Diff: enums.YesNoStatus = None
			self.Cell_Ur_Apch: enums.YesNoStatus = None
			self.Sfn_Sfn_Time_Diff: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:UEPosition \n
		Snippet: value: ValueStruct = driver.sense.ueCapability.uePosition.get_value() \n
		Returns UE capability information related to UE positioning. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:UEPosition?', self.__class__.ValueStruct())

	def clone(self) -> 'UePosition':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UePosition(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
