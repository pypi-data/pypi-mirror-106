from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: RefMeasChannel, default value after init: RefMeasChannel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_refMeasChannel_get', 'repcap_refMeasChannel_set', repcap.RefMeasChannel.Ch1)

	def repcap_refMeasChannel_set(self, enum_value: repcap.RefMeasChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RefMeasChannel.Default
		Default value after init: RefMeasChannel.Ch1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_refMeasChannel_get(self) -> repcap.RefMeasChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class RmcStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Beta_C: int: Range: 1 to 15
			- Beta_D: int: Range: 1 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_int('Beta_C'),
			ArgStruct.scalar_int('Beta_D')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Beta_C: int = None
			self.Beta_D: int = None

	def set(self, structure: RmcStruct, refMeasChannel=repcap.RefMeasChannel.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:RMC<nr> \n
		Snippet: driver.configure.uplink.gfactor.rmc.set(value = [PROPERTY_STRUCT_NAME](), refMeasChannel = repcap.RefMeasChannel.Default) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for RMC connections with the selected data rate. \n
			:param structure: for set value, see the help for RmcStruct structure arguments.
			:param refMeasChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Rmc')"""
		refMeasChannel_cmd_val = self._base.get_repcap_cmd_value(refMeasChannel, repcap.RefMeasChannel)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:RMC{refMeasChannel_cmd_val}', structure)

	def get(self, refMeasChannel=repcap.RefMeasChannel.Default) -> RmcStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:RMC<nr> \n
		Snippet: value: RmcStruct = driver.configure.uplink.gfactor.rmc.get(refMeasChannel = repcap.RefMeasChannel.Default) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for RMC connections with the selected data rate. \n
			:param refMeasChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Rmc')
			:return: structure: for return value, see the help for RmcStruct structure arguments."""
		refMeasChannel_cmd_val = self._base.get_repcap_cmd_value(refMeasChannel, repcap.RefMeasChannel)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:RMC{refMeasChannel_cmd_val}?', self.__class__.RmcStruct())

	def clone(self) -> 'Rmc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
