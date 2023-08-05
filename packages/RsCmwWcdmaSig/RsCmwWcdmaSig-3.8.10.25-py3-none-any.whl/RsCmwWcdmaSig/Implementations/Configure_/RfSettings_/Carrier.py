from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 16 total commands, 7 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def edc(self):
		"""edc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_edc'):
			from .Carrier_.Edc import Edc
			self._edc = Edc(self._core, self._base)
		return self._edc

	@property
	def eattenuation(self):
		"""eattenuation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Carrier_.Eattenuation import Eattenuation
			self._eattenuation = Eattenuation(self._core, self._base)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_channel'):
			from .Carrier_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Carrier_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_foffset'):
			from .Carrier_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Carrier_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Carrier_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	def get_gmt_factor(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:GMTFactor \n
		Snippet: value: float = driver.configure.rfSettings.carrier.get_gmt_factor() \n
		Queries the ratio of the output channel power (Ior) to the AWGN power (Ioc) . INV indicates that AWGN noise is disabled. \n
			:return: ratio: Range: -25.4 dB to 44.9 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:GMTFactor?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	class AwgnStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the AWGN signal
			- Level: float: The range of the AWGN level can be calculated as follows from the range of the output power stated below: Min (AWGN) = Min (Output Power) - External Attenuation Max (AWGN) = Max (Output Power) - External Attenuation - Base Level Range: -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet , Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Level: float = None

	def get_awgn(self) -> AwgnStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:AWGN \n
		Snippet: value: AwgnStruct = driver.configure.rfSettings.carrier.get_awgn() \n
		Enables or disables AWGN insertion via the signaling unit and sets the total AWGN level within the channel bandwidth. For
		multi-carrier, the same settings are applied to all carriers. Thus it is sufficient to configure one carrier. \n
			:return: structure: for return value, see the help for AwgnStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:AWGN?', self.__class__.AwgnStruct())

	def set_awgn(self, value: AwgnStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:AWGN \n
		Snippet: driver.configure.rfSettings.carrier.set_awgn(value = AwgnStruct()) \n
		Enables or disables AWGN insertion via the signaling unit and sets the total AWGN level within the channel bandwidth. For
		multi-carrier, the same settings are applied to all carriers. Thus it is sufficient to configure one carrier. \n
			:param value: see the help for AwgnStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:AWGN', value)

	def get_co_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:COPower \n
		Snippet: value: float = driver.configure.rfSettings.carrier.get_co_power() \n
		Sets the base level of the generator. For multi-carrier, it can be set per carrier. The allowed value range can be
		calculated as follows: Range (Base Level) = Range (Output Power) - External Attenuation - Insertion Loss + Baseband Level
		Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted
		in the data sheet. Insertion loss is only relevant for internal fading. Baseband level only relevant for external fading. \n
			:return: out_channel_pow: Range: see above , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:COPower?')
		return Conversions.str_to_float(response)

	def set_co_power(self, out_channel_pow: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:COPower \n
		Snippet: driver.configure.rfSettings.carrier.set_co_power(out_channel_pow = 1.0) \n
		Sets the base level of the generator. For multi-carrier, it can be set per carrier. The allowed value range can be
		calculated as follows: Range (Base Level) = Range (Output Power) - External Attenuation - Insertion Loss + Baseband Level
		Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted
		in the data sheet. Insertion loss is only relevant for internal fading. Baseband level only relevant for external fading. \n
			:param out_channel_pow: Range: see above , Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(out_channel_pow)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:COPower {param}')

	def get_to_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:TOPower \n
		Snippet: value: float = driver.configure.rfSettings.carrier.get_to_power() \n
		Queries the sum of the output channel power (Ior) and the AWGN power (Ioc) . \n
			:return: total_output_pow: Unit: dBm
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:TOPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
