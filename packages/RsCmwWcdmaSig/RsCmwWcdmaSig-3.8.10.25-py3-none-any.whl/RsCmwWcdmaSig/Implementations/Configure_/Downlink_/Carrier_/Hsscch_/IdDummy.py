from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdDummy:
	"""IdDummy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("idDummy", core, parent)

	def set(self, dummy_ueid: float, hSSCch=repcap.HSSCch.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:HSSCch<nr>:IDDummy \n
		Snippet: driver.configure.downlink.carrier.hsscch.idDummy.set(dummy_ueid = 1.0, hSSCch = repcap.HSSCch.Default) \n
		Sets the dummy UE identity to be sent in subframes which are not allocated to the UE. Individual values can be set per
		HS-SCCH. \n
			:param dummy_ueid: Range: 0 (#H0) to 65535 (#HFFFF)
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')"""
		param = Conversions.decimal_value_to_str(dummy_ueid)
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:HSSCch{hSSCch_cmd_val}:IDDummy {param}')

	def get(self, hSSCch=repcap.HSSCch.Default) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:HSSCch<nr>:IDDummy \n
		Snippet: value: float = driver.configure.downlink.carrier.hsscch.idDummy.get(hSSCch = repcap.HSSCch.Default) \n
		Sets the dummy UE identity to be sent in subframes which are not allocated to the UE. Individual values can be set per
		HS-SCCH. \n
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')
			:return: dummy_ueid: Range: 0 (#H0) to 65535 (#HFFFF)"""
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:HSSCch{hSSCch_cmd_val}:IDDummy?')
		return Conversions.str_to_float(response)
