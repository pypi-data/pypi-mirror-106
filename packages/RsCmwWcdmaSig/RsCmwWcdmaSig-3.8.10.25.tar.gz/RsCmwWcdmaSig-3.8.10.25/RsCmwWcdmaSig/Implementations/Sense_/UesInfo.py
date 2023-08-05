from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UesInfo:
	"""UesInfo commands group definition. 15 total commands, 2 Sub-groups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uesInfo", core, parent)

	@property
	def ueAddress(self):
		"""ueAddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueAddress'):
			from .UesInfo_.UeAddress import UeAddress
			self._ueAddress = UeAddress(self._core, self._base)
		return self._ueAddress

	@property
	def connection(self):
		"""connection commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_connection'):
			from .UesInfo_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	def get_apn(self) -> List[str]:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:APN \n
		Snippet: value: List[str] = driver.sense.uesInfo.get_apn() \n
		Returns all access point names used by the UE during a packet data connection. \n
			:return: apn: The names of all connected APNs as a string
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:APN?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	class DulAlignmentStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Carrier_1: float: Range: 0 chips to 10000 chips, Unit: chips
			- Carrier_2: float: Range: 0 chips to 10000 chips, Unit: chips"""
		__meta_args_list = [
			ArgStruct.scalar_float('Carrier_1'),
			ArgStruct.scalar_float('Carrier_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Carrier_1: float = None
			self.Carrier_2: float = None

	def get_dul_alignment(self) -> DulAlignmentStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:DULalignment \n
		Snippet: value: DulAlignmentStruct = driver.sense.uesInfo.get_dul_alignment() \n
		Returns the offset between DL DPCH and UL DPCH at the RF connectors of the instrument per carrier. \n
			:return: structure: for return value, see the help for DulAlignmentStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:DULalignment?', self.__class__.DulAlignmentStruct())

	# noinspection PyTypeChecker
	class DinfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cmw_Demod_Info: str: 'Uplink Power Underflow': the UL signal power is too low 'Uplink Power in Range': the UL signal power is in range 'Uplink Power Overflow': the UL signal power is too high
			- Power_C_1: enums.CellPower: UFL | OK | OFL Cell 1 information: UFL: the UL signal power is too low OK: the UL signal power is in range OFL: the UL signal power is too high
			- Sync_C_1: enums.Sync: NOSYnc | OK Cell 1 information: NOSYnc: synchronization to the uplink signal failed OK: successful synchronization to the uplink signal
			- Power_C_2: enums.CellPower: UFL | OK | OFL Cell 2 information: UFL: the UL signal power is too low OK: the UL signal power is in range OFL: the UL signal power is too high
			- Sync_C_2: enums.Sync: NOSYnc | OK Cell 2 information: NOSYnc: synchronization to the uplink signal failed OK: successful synchronization to the uplink signal"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cmw_Demod_Info'),
			ArgStruct.scalar_enum('Power_C_1', enums.CellPower),
			ArgStruct.scalar_enum('Sync_C_1', enums.Sync),
			ArgStruct.scalar_enum('Power_C_2', enums.CellPower),
			ArgStruct.scalar_enum('Sync_C_2', enums.Sync)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cmw_Demod_Info: str = None
			self.Power_C_1: enums.CellPower = None
			self.Sync_C_1: enums.Sync = None
			self.Power_C_2: enums.CellPower = None
			self.Sync_C_2: enums.Sync = None

	def get_dinfo(self) -> DinfoStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:DINFo \n
		Snippet: value: DinfoStruct = driver.sense.uesInfo.get_dinfo() \n
		Queries the demodulation info provided by the demodulator stage of the instrument while it perceives an uplink signal.
		Information about cell two are relevant only if the dual carrier HSPA scenario is active. \n
			:return: structure: for return value, see the help for DinfoStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:DINFo?', self.__class__.DinfoStruct())

	def get_imei(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:IMEI \n
		Snippet: value: str = driver.sense.uesInfo.get_imei() \n
		Queries the IMEI of the UE. \n
			:return: imei: IMEI as string with up to 18 digits.
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:IMEI?')
		return trim_str_response(response)

	def get_ridentity(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:RIDentity \n
		Snippet: value: str = driver.sense.uesInfo.get_ridentity() \n
		Queries the registration identity received from the UE during registration. \n
			:return: identity: Registration identity as string with up to 18 digits.
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:RIDentity?')
		return trim_str_response(response)

	def get_ri_type(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:RITYpe \n
		Snippet: value: str = driver.sense.uesInfo.get_ri_type() \n
		Queries the type of the registration identity received from the UE during registration. \n
			:return: ri_type: 'IMSI' | 'IMEI' | 'IMSISV' | 'TMSI' | 'UNKN' Registration identity type as string. 'UNKN' means unknown.
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:RITYpe?')
		return trim_str_response(response)

	def get_tty(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:TTY \n
		Snippet: value: str = driver.sense.uesInfo.get_tty() \n
		Queries whether the UE supports cellular text telephony (CTM) . \n
			:return: tty: 'supported' | 'not supported' 'supported': CTM supported 'not supported': CTM not supported
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:TTY?')
		return trim_str_response(response)

	def get_cnumber(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:CNUMber \n
		Snippet: value: str = driver.sense.uesInfo.get_cnumber() \n
		Queries the calling number for a UE originated call. \n
			:return: number: Calling number as string with up to 129 digits.
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:CNUMber?')
		return trim_str_response(response)

	def get_dnumber(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:DNUMber \n
		Snippet: value: str = driver.sense.uesInfo.get_dnumber() \n
		Queries the number dialed at the UE. \n
			:return: number: Dialed number as string with up to 129 digits.
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:DNUMber?')
		return trim_str_response(response)

	def get_emergency(self) -> bool:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:EMERgency \n
		Snippet: value: bool = driver.sense.uesInfo.get_emergency() \n
		Queries whether the established connection is an emergency call. \n
			:return: active: OFF | ON ON: emergency call OFF: no emergency call
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:EMERgency?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	class EsCategoryStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Police: bool: OFF | ON OFF: no emergency call to police ON: emergency call to police
			- Ambulance: bool: OFF | ON
			- Fire_Brigade: bool: OFF | ON
			- Marine_Guard: bool: OFF | ON
			- Mountain_Rescue: bool: OFF | ON
			- Manual: bool: OFF | ON OFF: no emergency calls set up manually ON: emergency calls set up manually
			- Automatical: bool: OFF | ON OFF: no emergency calls set up automatically ON: emergency calls set up automatically"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Police'),
			ArgStruct.scalar_bool('Ambulance'),
			ArgStruct.scalar_bool('Fire_Brigade'),
			ArgStruct.scalar_bool('Marine_Guard'),
			ArgStruct.scalar_bool('Mountain_Rescue'),
			ArgStruct.scalar_bool('Manual'),
			ArgStruct.scalar_bool('Automatical')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Police: bool = None
			self.Ambulance: bool = None
			self.Fire_Brigade: bool = None
			self.Marine_Guard: bool = None
			self.Mountain_Rescue: bool = None
			self.Manual: bool = None
			self.Automatical: bool = None

	def get_es_category(self) -> EsCategoryStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:ESCategory \n
		Snippet: value: EsCategoryStruct = driver.sense.uesInfo.get_es_category() \n
		Returns the service category used during emergency call. \n
			:return: structure: for return value, see the help for EsCategoryStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:ESCategory?', self.__class__.EsCategoryStruct())

	# noinspection PyTypeChecker
	def get_rrc(self) -> enums.RrcState:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:RRC \n
		Snippet: value: enums.RrcState = driver.sense.uesInfo.get_rrc() \n
		Returns the RRC protocol state of the UE. \n
			:return: state: IDLE | FACH | CPCH | UPCH | DCH Idle mode, CELL_FACH, CELL_PCH, URA_PCH, CELL_DCH
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:RRC?')
		return Conversions.str_to_scalar_enum(response, enums.RrcState)

	def clone(self) -> 'UesInfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UesInfo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
