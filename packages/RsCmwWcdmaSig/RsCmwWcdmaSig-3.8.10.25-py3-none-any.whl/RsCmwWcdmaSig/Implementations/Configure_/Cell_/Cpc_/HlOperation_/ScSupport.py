from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScSupport:
	"""ScSupport commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: SecondCode, default value after init: SecondCode.Sc1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scSupport", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondCode_get', 'repcap_secondCode_set', repcap.SecondCode.Sc1)

	def repcap_secondCode_set(self, enum_value: repcap.SecondCode) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondCode.Default
		Default value after init: SecondCode.Sc1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondCode_get(self) -> repcap.SecondCode:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, enable: List[bool], secondCode=repcap.SecondCode.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:SCSupport<index> \n
		Snippet: driver.configure.cell.cpc.hlOperation.scSupport.set(enable = [True, False, True], secondCode = repcap.SecondCode.Default) \n
		Predefines the support of HS-PDSCH second code for HS-SCCH less operation. \n
			:param enable: OFF | ON
			:param secondCode: optional repeated capability selector. Default value: Sc1 (settable in the interface 'ScSupport')"""
		param = Conversions.list_to_csv_str(enable)
		secondCode_cmd_val = self._base.get_repcap_cmd_value(secondCode, repcap.SecondCode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:SCSupport{secondCode_cmd_val} {param}')

	def get(self, secondCode=repcap.SecondCode.Default) -> List[bool]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HLOPeration:SCSupport<index> \n
		Snippet: value: List[bool] = driver.configure.cell.cpc.hlOperation.scSupport.get(secondCode = repcap.SecondCode.Default) \n
		Predefines the support of HS-PDSCH second code for HS-SCCH less operation. \n
			:param secondCode: optional repeated capability selector. Default value: Sc1 (settable in the interface 'ScSupport')
			:return: enable: OFF | ON"""
		secondCode_cmd_val = self._base.get_repcap_cmd_value(secondCode, repcap.SecondCode)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HLOPeration:SCSupport{secondCode_cmd_val}?')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'ScSupport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScSupport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
