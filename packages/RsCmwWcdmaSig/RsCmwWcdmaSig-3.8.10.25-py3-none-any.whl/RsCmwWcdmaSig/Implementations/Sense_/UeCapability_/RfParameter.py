from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfParameter:
	"""RfParameter commands group definition. 5 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfParameter", core, parent)

	@property
	def band(self):
		"""band commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .RfParameter_.Band import Band
			self._band = Band(self._core, self._base)
		return self._band

	@property
	def bc(self):
		"""bc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bc'):
			from .RfParameter_.Bc import Bc
			self._bc = Bc(self._core, self._base)
		return self._bc

	# noinspection PyTypeChecker
	class BcListStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bcomb_1: enums.YesNoStatus: NO | YES Indicates if the UE supports the band combination 1+8
			- Bcomb_2: enums.YesNoStatus: NO | YES Indicates if the UE supports the band combination 2+4
			- Bcomb_3: enums.YesNoStatus: NO | YES Indicates if the UE supports the band combination 1+5
			- Bcomb_4: enums.YesNoStatus: NO | YES Indicates if the UE supports the band combination 1+6
			- Bcomb_5: enums.YesNoStatus: NO | YES Indicates if the UE supports the band combination 2+5"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bcomb_1', enums.YesNoStatus),
			ArgStruct.scalar_enum('Bcomb_2', enums.YesNoStatus),
			ArgStruct.scalar_enum('Bcomb_3', enums.YesNoStatus),
			ArgStruct.scalar_enum('Bcomb_4', enums.YesNoStatus),
			ArgStruct.scalar_enum('Bcomb_5', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bcomb_1: enums.YesNoStatus = None
			self.Bcomb_2: enums.YesNoStatus = None
			self.Bcomb_3: enums.YesNoStatus = None
			self.Bcomb_4: enums.YesNoStatus = None
			self.Bcomb_5: enums.YesNoStatus = None

	# noinspection PyTypeChecker
	def get_bc_list(self) -> BcListStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RFParameter:BCList \n
		Snippet: value: BcListStruct = driver.sense.ueCapability.rfParameter.get_bc_list() \n
		Indicates which band combination the UE supports. \n
			:return: structure: for return value, see the help for BcListStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:RFParameter:BCList?', self.__class__.BcListStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Supported_1: enums.YesNoStatus: No parameter help available
			- Power_Class_1: int: UE power class for band I Range: 1 to 4
			- Band_Supported_2: enums.YesNoStatus: No parameter help available
			- Power_Class_2: int: No parameter help available
			- Band_Supported_3: enums.YesNoStatus: No parameter help available
			- Power_Class_3: int: No parameter help available
			- Band_Supported_4: enums.YesNoStatus: No parameter help available
			- Power_Class_4: int: No parameter help available
			- Band_Supported_5: enums.YesNoStatus: No parameter help available
			- Power_Class_5: int: No parameter help available
			- Band_Supported_6: enums.YesNoStatus: No parameter help available
			- Power_Class_6: int: No parameter help available
			- Band_Supported_7: enums.YesNoStatus: No parameter help available
			- Power_Class_7: int: No parameter help available
			- Band_Supported_8: enums.YesNoStatus: No parameter help available
			- Power_Class_8: int: No parameter help available
			- Band_Supported_9: enums.YesNoStatus: No parameter help available
			- Power_Class_9: int: No parameter help available
			- Band_Supported_10: enums.YesNoStatus: No parameter help available
			- Power_Class_10: int: No parameter help available
			- Band_Supported_11: enums.YesNoStatus: No parameter help available
			- Power_Class_11: int: No parameter help available
			- Band_Supported_12: enums.YesNoStatus: No parameter help available
			- Power_Class_12: int: No parameter help available
			- Band_Supported_13: enums.YesNoStatus: No parameter help available
			- Power_Class_13: int: No parameter help available
			- Band_Supported_14: enums.YesNoStatus: No parameter help available
			- Power_Class_14: int: UE power class for band XIV
			- Band_Supported_19: enums.YesNoStatus: No parameter help available
			- Power_Class_19: int: UE power class for band XIX
			- Band_Supported_20: enums.YesNoStatus: No parameter help available
			- Power_Class_20: int: No parameter help available
			- Band_Supported_21: enums.YesNoStatus: No parameter help available
			- Power_Class_21: int: UE power class for band XXI
			- Band_Supported_15: enums.YesNoStatus: No parameter help available
			- Power_Class_15: int: UE power class for band XV
			- Band_Supported_16: enums.YesNoStatus: No parameter help available
			- Power_Class_16: int: No parameter help available
			- Band_Supported_17: enums.YesNoStatus: No parameter help available
			- Power_Class_17: enums.YesNoStatus: No parameter help available
			- Band_Supported_18: enums.YesNoStatus: No parameter help available
			- Power_Class_18: int: UE power class for band XVIII
			- Band_Supported_22: enums.YesNoStatus: No parameter help available
			- Power_Class_22: int: UE power class for band XXII
			- Band_Supported_25: enums.YesNoStatus: No parameter help available
			- Power_Class_25: int: UE power class for band XXV
			- Band_Supported_26: enums.YesNoStatus: No parameter help available
			- Power_Class_26: int: UE power class for band XXVI
			- Band_Supported_32: enums.YesNoStatus: No parameter help available
			- Power_Class_32: int: UE power class for band XXXII"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Supported_1', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_1'),
			ArgStruct.scalar_enum('Band_Supported_2', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_2'),
			ArgStruct.scalar_enum('Band_Supported_3', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_3'),
			ArgStruct.scalar_enum('Band_Supported_4', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_4'),
			ArgStruct.scalar_enum('Band_Supported_5', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_5'),
			ArgStruct.scalar_enum('Band_Supported_6', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_6'),
			ArgStruct.scalar_enum('Band_Supported_7', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_7'),
			ArgStruct.scalar_enum('Band_Supported_8', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_8'),
			ArgStruct.scalar_enum('Band_Supported_9', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_9'),
			ArgStruct.scalar_enum('Band_Supported_10', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_10'),
			ArgStruct.scalar_enum('Band_Supported_11', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_11'),
			ArgStruct.scalar_enum('Band_Supported_12', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_12'),
			ArgStruct.scalar_enum('Band_Supported_13', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_13'),
			ArgStruct.scalar_enum('Band_Supported_14', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_14'),
			ArgStruct.scalar_enum('Band_Supported_19', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_19'),
			ArgStruct.scalar_enum('Band_Supported_20', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_20'),
			ArgStruct.scalar_enum('Band_Supported_21', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_21'),
			ArgStruct.scalar_enum('Band_Supported_15', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_15'),
			ArgStruct.scalar_enum('Band_Supported_16', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_16'),
			ArgStruct.scalar_enum('Band_Supported_17', enums.YesNoStatus),
			ArgStruct.scalar_enum('Power_Class_17', enums.YesNoStatus),
			ArgStruct.scalar_enum('Band_Supported_18', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_18'),
			ArgStruct.scalar_enum('Band_Supported_22', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_22'),
			ArgStruct.scalar_enum('Band_Supported_25', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_25'),
			ArgStruct.scalar_enum('Band_Supported_26', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_26'),
			ArgStruct.scalar_enum('Band_Supported_32', enums.YesNoStatus),
			ArgStruct.scalar_int('Power_Class_32')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Supported_1: enums.YesNoStatus = None
			self.Power_Class_1: int = None
			self.Band_Supported_2: enums.YesNoStatus = None
			self.Power_Class_2: int = None
			self.Band_Supported_3: enums.YesNoStatus = None
			self.Power_Class_3: int = None
			self.Band_Supported_4: enums.YesNoStatus = None
			self.Power_Class_4: int = None
			self.Band_Supported_5: enums.YesNoStatus = None
			self.Power_Class_5: int = None
			self.Band_Supported_6: enums.YesNoStatus = None
			self.Power_Class_6: int = None
			self.Band_Supported_7: enums.YesNoStatus = None
			self.Power_Class_7: int = None
			self.Band_Supported_8: enums.YesNoStatus = None
			self.Power_Class_8: int = None
			self.Band_Supported_9: enums.YesNoStatus = None
			self.Power_Class_9: int = None
			self.Band_Supported_10: enums.YesNoStatus = None
			self.Power_Class_10: int = None
			self.Band_Supported_11: enums.YesNoStatus = None
			self.Power_Class_11: int = None
			self.Band_Supported_12: enums.YesNoStatus = None
			self.Power_Class_12: int = None
			self.Band_Supported_13: enums.YesNoStatus = None
			self.Power_Class_13: int = None
			self.Band_Supported_14: enums.YesNoStatus = None
			self.Power_Class_14: int = None
			self.Band_Supported_19: enums.YesNoStatus = None
			self.Power_Class_19: int = None
			self.Band_Supported_20: enums.YesNoStatus = None
			self.Power_Class_20: int = None
			self.Band_Supported_21: enums.YesNoStatus = None
			self.Power_Class_21: int = None
			self.Band_Supported_15: enums.YesNoStatus = None
			self.Power_Class_15: int = None
			self.Band_Supported_16: enums.YesNoStatus = None
			self.Power_Class_16: int = None
			self.Band_Supported_17: enums.YesNoStatus = None
			self.Power_Class_17: enums.YesNoStatus = None
			self.Band_Supported_18: enums.YesNoStatus = None
			self.Power_Class_18: int = None
			self.Band_Supported_22: enums.YesNoStatus = None
			self.Power_Class_22: int = None
			self.Band_Supported_25: enums.YesNoStatus = None
			self.Power_Class_25: int = None
			self.Band_Supported_26: enums.YesNoStatus = None
			self.Power_Class_26: int = None
			self.Band_Supported_32: enums.YesNoStatus = None
			self.Power_Class_32: int = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RFParameter \n
		Snippet: value: ValueStruct = driver.sense.ueCapability.rfParameter.get_value() \n
		Returns RF UE capability information. The value pairs are returned 25 times (band I to XXII, band XXV, XXVI and XXXII) . \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:UECapability:RFParameter?', self.__class__.ValueStruct())

	def clone(self) -> 'RfParameter':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfParameter(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
