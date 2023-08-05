from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ehrch:
	"""Ehrch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ehrch", core, parent)

	def get_fuf_dummies(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHRCh:FUFDummies \n
		Snippet: value: bool = driver.configure.cell.carrier.hsupa.ehrch.get_fuf_dummies() \n
		Enables or disables filling-up the frame with dummies. This feature is only relevant for 10 ms TTI. Here E-RGCH and
		E-HICH messages for the UE are transmitted in 12 slots per frame. The command defines the behavior in the remaining three
		slots. \n
			:return: enable: OFF | ON OFF: switch off channels (DTX) ON: fill-up with dummies, continuous signal
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHRCh:FUFDummies?')
		return Conversions.str_to_bool(response)

	def set_fuf_dummies(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EHRCh:FUFDummies \n
		Snippet: driver.configure.cell.carrier.hsupa.ehrch.set_fuf_dummies(enable = False) \n
		Enables or disables filling-up the frame with dummies. This feature is only relevant for 10 ms TTI. Here E-RGCH and
		E-HICH messages for the UE are transmitted in 12 slots per frame. The command defines the behavior in the remaining three
		slots. \n
			:param enable: OFF | ON OFF: switch off channels (DTX) ON: fill-up with dummies, continuous signal
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EHRCh:FUFDummies {param}')
