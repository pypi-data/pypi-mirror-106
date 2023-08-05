from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("foffset", core, parent)

	def get_uplink(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FOFFset:UL \n
		Snippet: value: float = driver.configure.rfSettings.carrier.foffset.get_uplink() \n
		Specifies a positive or negative frequency offset to be added to the uplink center frequency of the configured channel,
		see method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Frequency.uplink . \n
			:return: freq_offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FOFFset:UL?')
		return Conversions.str_to_float(response)

	def set_uplink(self, freq_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FOFFset:UL \n
		Snippet: driver.configure.rfSettings.carrier.foffset.set_uplink(freq_offset = 1.0) \n
		Specifies a positive or negative frequency offset to be added to the uplink center frequency of the configured channel,
		see method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Frequency.uplink . \n
			:param freq_offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(freq_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FOFFset:UL {param}')

	def get_downlink(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FOFFset:DL \n
		Snippet: value: float = driver.configure.rfSettings.carrier.foffset.get_downlink() \n
		Specifies a positive or negative frequency offset to be added to the downlink center frequency of the configured channel,
		see method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Frequency.downlink. \n
			:return: freq_offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FOFFset:DL?')
		return Conversions.str_to_float(response)

	def set_downlink(self, freq_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:FOFFset:DL \n
		Snippet: driver.configure.rfSettings.carrier.foffset.set_downlink(freq_offset = 1.0) \n
		Specifies a positive or negative frequency offset to be added to the downlink center frequency of the configured channel,
		see method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Frequency.downlink. \n
			:param freq_offset: Range: -100000 Hz to 100000 Hz , Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(freq_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:FOFFset:DL {param}')
