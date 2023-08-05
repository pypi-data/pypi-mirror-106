from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tblock:
	"""Tblock commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: TransportBlock, default value after init: TransportBlock.TBl1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tblock", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_transportBlock_get', 'repcap_transportBlock_set', repcap.TransportBlock.TBl1)

	def repcap_transportBlock_set(self, enum_value: repcap.TransportBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TransportBlock.Default
		Default value after init: TransportBlock.TBl1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_transportBlock_get(self) -> repcap.TransportBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, index: List[int], transportBlock=repcap.TransportBlock.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:TBLock<index> \n
		Snippet: driver.configure.cell.cpc.hlOperation.tblock.set(index = [1, 2, 3], transportBlock = repcap.TransportBlock.Default) \n
		Predefines the transport block size index for HS-SCCH less operation. \n
			:param index: 1..4 Number of preconfiguration set
			:param transportBlock: optional repeated capability selector. Default value: TBl1 (settable in the interface 'Tblock')"""
		param = Conversions.list_to_csv_str(index)
		transportBlock_cmd_val = self._base.get_repcap_cmd_value(transportBlock, repcap.TransportBlock)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:TBLock{transportBlock_cmd_val} {param}')

	def get(self, transportBlock=repcap.TransportBlock.Default) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:TBLock<index> \n
		Snippet: value: List[int] = driver.configure.cell.cpc.hlOperation.tblock.get(transportBlock = repcap.TransportBlock.Default) \n
		Predefines the transport block size index for HS-SCCH less operation. \n
			:param transportBlock: optional repeated capability selector. Default value: TBl1 (settable in the interface 'Tblock')
			:return: index: 1..4 Number of preconfiguration set"""
		transportBlock_cmd_val = self._base.get_repcap_cmd_value(transportBlock, repcap.TransportBlock)
		response = self._core.io.query_bin_or_ascii_int_list(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:TBLock{transportBlock_cmd_val}?')
		return response

	def clone(self) -> 'Tblock':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tblock(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
