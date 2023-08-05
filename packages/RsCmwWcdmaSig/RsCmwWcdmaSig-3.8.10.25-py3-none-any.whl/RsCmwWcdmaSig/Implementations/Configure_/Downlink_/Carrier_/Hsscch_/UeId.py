from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeId:
	"""UeId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueId", core, parent)

	def set(self, ue_id: float, hSSCch=repcap.HSSCch.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:HSSCch<nr>:UEID \n
		Snippet: driver.configure.downlink.carrier.hsscch.ueId.set(ue_id = 1.0, hSSCch = repcap.HSSCch.Default) \n
		Sets the UE identity for an HS-SCCH channel. In the current software version, only one UE ID is configured for the
		HS-SCCH set of one carrier. Changing the value for one channel changes also the values of the other channels. \n
			:param ue_id: Range: 0 (#H0) to 65535 (#HFFFF)
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')"""
		param = Conversions.decimal_value_to_str(ue_id)
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:HSSCch{hSSCch_cmd_val}:UEID {param}')

	def get(self, hSSCch=repcap.HSSCch.Default) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:HSSCch<nr>:UEID \n
		Snippet: value: float = driver.configure.downlink.carrier.hsscch.ueId.get(hSSCch = repcap.HSSCch.Default) \n
		Sets the UE identity for an HS-SCCH channel. In the current software version, only one UE ID is configured for the
		HS-SCCH set of one carrier. Changing the value for one channel changes also the values of the other channels. \n
		Global Repeated Capabilities: repcap.Carrier
			:param hSSCch: optional repeated capability selector. Default value: No1 (settable in the interface 'Hsscch')
			:return: ue_id: Range: 0 (#H0) to 65535 (#HFFFF)"""
		hSSCch_cmd_val = self._base.get_repcap_cmd_value(hSSCch, repcap.HSSCch)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:HSSCch{hSSCch_cmd_val}:UEID?')
		return Conversions.str_to_float(response)
