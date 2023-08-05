from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nc:
	"""Nc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: NonContigCell, default value after init: NonContigCell.Nc2"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_nonContigCell_get', 'repcap_nonContigCell_set', repcap.NonContigCell.Nc2)

	def repcap_nonContigCell_set(self, enum_value: repcap.NonContigCell) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to NonContigCell.Default
		Default value after init: NonContigCell.Nc2"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_nonContigCell_get(self) -> repcap.NonContigCell:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Supported: enums.YesNoStatus: NO | YES Indicates if the UE supports non-contiguous multi-cell operation for the selected band/cell combination
			- Gap_Size: enums.GapSize: M5 | M10 | ANY The maximum gap size between the aggregated cells supported by the UE M5: 5 MHz M10: 10 MHz ANY: any multiple of 5 MHz
			- Nc_Comb_22: enums.YesNoStatus: NO | YES Indicates if the UE supports an equal number of contiguous cells on each side of the gap
			- Nc_Comb_1331: enums.YesNoStatus: NO | YES Indicates if the UE supports a different number of contiguous cells on each side of the gap"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Supported', enums.YesNoStatus),
			ArgStruct.scalar_enum('Gap_Size', enums.GapSize),
			ArgStruct.scalar_enum('Nc_Comb_22', enums.YesNoStatus),
			ArgStruct.scalar_enum('Nc_Comb_1331', enums.YesNoStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Supported: enums.YesNoStatus = None
			self.Gap_Size: enums.GapSize = None
			self.Nc_Comb_22: enums.YesNoStatus = None
			self.Nc_Comb_1331: enums.YesNoStatus = None

	def get(self, band=repcap.Band.Default, nonContigCell=repcap.NonContigCell.Default) -> GetStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:RFParameter:BAND<band>:NC<cell> \n
		Snippet: value: GetStruct = driver.sense.ueCapability.rfParameter.band.nc.get(band = repcap.Band.Default, nonContigCell = repcap.NonContigCell.Default) \n
		Queries the UE capabilities related to non-contiguous multi-cell operation. \n
			:param band: optional repeated capability selector. Default value: B1 (settable in the interface 'Band')
			:param nonContigCell: optional repeated capability selector. Default value: Nc2 (settable in the interface 'Nc')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		band_cmd_val = self._base.get_repcap_cmd_value(band, repcap.Band)
		nonContigCell_cmd_val = self._base.get_repcap_cmd_value(nonContigCell, repcap.NonContigCell)
		return self._core.io.query_struct(f'SENSe:WCDMa:SIGNaling<Instance>:UECapability:RFParameter:BAND{band_cmd_val}:NC{nonContigCell_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Nc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
