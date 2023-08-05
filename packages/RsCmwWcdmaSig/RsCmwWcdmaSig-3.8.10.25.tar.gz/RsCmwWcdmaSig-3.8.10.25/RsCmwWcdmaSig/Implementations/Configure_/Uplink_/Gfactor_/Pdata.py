from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdata:
	"""Pdata commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: PacketData, default value after init: PacketData.Pd8"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdata", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_packetData_get', 'repcap_packetData_set', repcap.PacketData.Pd8)

	def repcap_packetData_set(self, enum_value: repcap.PacketData) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PacketData.Default
		Default value after init: PacketData.Pd8"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_packetData_get(self) -> repcap.PacketData:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class PdataStruct(StructBase):
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

	def set(self, structure: PdataStruct, packetData=repcap.PacketData.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:PDATa<nr> \n
		Snippet: driver.configure.uplink.gfactor.pdata.set(value = [PROPERTY_STRUCT_NAME](), packetData = repcap.PacketData.Default) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for packet data connections. \n
			:param structure: for set value, see the help for PdataStruct structure arguments.
			:param packetData: optional repeated capability selector. Default value: Pd8 (settable in the interface 'Pdata')"""
		packetData_cmd_val = self._base.get_repcap_cmd_value(packetData, repcap.PacketData)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:PDATa{packetData_cmd_val}', structure)

	def get(self, packetData=repcap.PacketData.Default) -> PdataStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:PDATa<nr> \n
		Snippet: value: PdataStruct = driver.configure.uplink.gfactor.pdata.get(packetData = repcap.PacketData.Default) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for packet data connections. \n
			:param packetData: optional repeated capability selector. Default value: Pd8 (settable in the interface 'Pdata')
			:return: structure: for return value, see the help for PdataStruct structure arguments."""
		packetData_cmd_val = self._base.get_repcap_cmd_value(packetData, repcap.PacketData)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:PDATa{packetData_cmd_val}?', self.__class__.PdataStruct())

	def clone(self) -> 'Pdata':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdata(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
