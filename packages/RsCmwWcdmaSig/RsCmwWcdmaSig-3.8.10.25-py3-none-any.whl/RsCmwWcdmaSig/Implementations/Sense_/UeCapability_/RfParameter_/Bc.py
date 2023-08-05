from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bc:
	"""Bc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: BandCombination, default value after init: BandCombination.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_bandCombination_get', 'repcap_bandCombination_set', repcap.BandCombination.Nr1)

	def repcap_bandCombination_set(self, enum_value: repcap.BandCombination) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BandCombination.Default
		Default value after init: BandCombination.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_bandCombination_get(self) -> repcap.BandCombination:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ccomp_12: enums.YesNoStatus: NO | YES Indicates if the UE supports one contiguous carrier in band A and the maximum number of two contiguous carriers in band B
			- Ccomp_21: enums.YesNoStatus: NO | YES Indicates if the UE supports the maximum number of two contiguous carriers in band A and one contiguous carrier in band B
			- Ccomp_13: enums.YesNoStatus: NO | YES Indicates if the UE supports one contiguous carrier in band A and the maximum number of three contiguous carriers in band B
			- Ccomp_31: enums.YesNoStatus: NO | YES Indicates if the UE supports the maximum number of three contiguous carriers in band A and one contiguous carrier in band B
			- Ccomp_22: enums.YesNoStatus: NO | YES Indicates if the UE supports the maximum number of two contiguous carriers in band A and the maximum number of two contiguous carriers in band B"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ccomp_12', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ccomp_21', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ccomp_13', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ccomp_31', enums.YesNoStatus),
			ArgStruct.scalar_enum('Ccomp_22', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ccomp_12: enums.YesNoStatus = None
			self.Ccomp_21: enums.YesNoStatus = None
			self.Ccomp_13: enums.YesNoStatus = None
			self.Ccomp_31: enums.YesNoStatus = None
			self.Ccomp_22: enums.YesNoStatus = None

	def get(self, bandCombination=repcap.BandCombination.Default) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RFParameter:BC<nr> \n
		Snippet: value: GetStruct = driver.sense.ueCapability.rfParameter.bc.get(bandCombination = repcap.BandCombination.Default) \n
		Indicates which carrier combination for specific band combination the UE supports. \n
			:param bandCombination: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		bandCombination_cmd_val = self._base.get_repcap_cmd_value(bandCombination, repcap.BandCombination)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UECapability:RFParameter:BC{bandCombination_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Bc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
