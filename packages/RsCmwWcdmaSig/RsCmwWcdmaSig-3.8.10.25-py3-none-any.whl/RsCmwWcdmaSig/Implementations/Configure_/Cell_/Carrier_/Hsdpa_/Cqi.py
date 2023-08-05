from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqi:
	"""Cqi commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cqi", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:ENABle \n
		Snippet: value: bool = driver.configure.cell.carrier.hsdpa.cqi.get_enable() \n
		Enables or disables the multi-carrier operation for data transport via additional HS-DSCH. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:ENABle \n
		Snippet: driver.configure.cell.carrier.hsdpa.cqi.set_enable(enable = False) \n
		Enables or disables the multi-carrier operation for data transport via additional HS-DSCH. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:ENABle {param}')

	def get_fixed(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:FIXed \n
		Snippet: value: int = driver.configure.cell.carrier.hsdpa.cqi.get_fixed() \n
		Selects the CQI table index to be used if FIXed is configured via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.tindex. \n
			:return: fixed_value: Range: 1 to 30
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:FIXed?')
		return Conversions.str_to_int(response)

	def set_fixed(self, fixed_value: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:FIXed \n
		Snippet: driver.configure.cell.carrier.hsdpa.cqi.set_fixed(fixed_value = 1) \n
		Selects the CQI table index to be used if FIXed is configured via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.tindex. \n
			:param fixed_value: Range: 1 to 30
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(fixed_value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:FIXed {param}')

	def get_conformance(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:CONFormance \n
		Snippet: value: int = driver.configure.cell.carrier.hsdpa.cqi.get_conformance() \n
		Defines the CQI value used in the first stage of the test where the downlink transport format is fixed and the frequency
		distribution of the reported CQI values is calculated. To use this value, configure CONFormance via method RsCmwWcdmaSig.
		Configure.Cell.Hsdpa.Cqi.tindex. \n
			:return: value: Range: 1 to 30
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:CONFormance?')
		return Conversions.str_to_int(response)

	def set_conformance(self, value: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:CQI:CONFormance \n
		Snippet: driver.configure.cell.carrier.hsdpa.cqi.set_conformance(value = 1) \n
		Defines the CQI value used in the first stage of the test where the downlink transport format is fixed and the frequency
		distribution of the reported CQI values is calculated. To use this value, configure CONFormance via method RsCmwWcdmaSig.
		Configure.Cell.Hsdpa.Cqi.tindex. \n
			:param value: Range: 1 to 30
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:CQI:CONFormance {param}')
