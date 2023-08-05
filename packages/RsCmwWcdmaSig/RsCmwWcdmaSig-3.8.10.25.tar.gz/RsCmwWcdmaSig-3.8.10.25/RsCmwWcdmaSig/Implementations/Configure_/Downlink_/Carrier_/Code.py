from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 7 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("code", core, parent)

	@property
	def hsscch(self):
		"""hsscch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsscch'):
			from .Code_.Hsscch import Hsscch
			self._hsscch = Hsscch(self._core, self._base)
		return self._hsscch

	# noinspection PyTypeChecker
	class ConflictStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Ocns: bool: OFF | ON
			- Pcpich: bool: OFF | ON
			- Scpich: bool: OFF | ON
			- Pccpch: bool: OFF | ON
			- Sccpch: bool: OFF | ON
			- Pich: bool: OFF | ON
			- Aich: bool: OFF | ON
			- Dpch: bool: OFF | ON
			- Hsscch_1: bool: OFF | ON
			- Hsscch_2: bool: OFF | ON
			- Hsscch_3: bool: OFF | ON
			- Hsscch_4: bool: OFF | ON
			- Hs_Pdsch: bool: OFF | ON
			- Eagch: bool: OFF | ON
			- Ehich: bool: OFF | ON
			- Ergch: bool: OFF | ON
			- Fdpch: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Ocns'),
			ArgStruct.scalar_bool('Pcpich'),
			ArgStruct.scalar_bool('Scpich'),
			ArgStruct.scalar_bool('Pccpch'),
			ArgStruct.scalar_bool('Sccpch'),
			ArgStruct.scalar_bool('Pich'),
			ArgStruct.scalar_bool('Aich'),
			ArgStruct.scalar_bool('Dpch'),
			ArgStruct.scalar_bool('Hsscch_1'),
			ArgStruct.scalar_bool('Hsscch_2'),
			ArgStruct.scalar_bool('Hsscch_3'),
			ArgStruct.scalar_bool('Hsscch_4'),
			ArgStruct.scalar_bool('Hs_Pdsch'),
			ArgStruct.scalar_bool('Eagch'),
			ArgStruct.scalar_bool('Ehich'),
			ArgStruct.scalar_bool('Ergch'),
			ArgStruct.scalar_bool('Fdpch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ocns: bool = None
			self.Pcpich: bool = None
			self.Scpich: bool = None
			self.Pccpch: bool = None
			self.Sccpch: bool = None
			self.Pich: bool = None
			self.Aich: bool = None
			self.Dpch: bool = None
			self.Hsscch_1: bool = None
			self.Hsscch_2: bool = None
			self.Hsscch_3: bool = None
			self.Hsscch_4: bool = None
			self.Hs_Pdsch: bool = None
			self.Eagch: bool = None
			self.Ehich: bool = None
			self.Ergch: bool = None
			self.Fdpch: bool = None

	def get_conflict(self) -> ConflictStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:CONFlict \n
		Snippet: value: ConflictStruct = driver.configure.downlink.carrier.code.get_conflict() \n
			INTRO_CMD_HELP: Queries the channelization code conflict status of the physical channels: \n
			- OFF: channel causes no code conflict
			- ON: code settings of this channel conflict with the code settings of another channel \n
			:return: structure: for return value, see the help for ConflictStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:CONFlict?', self.__class__.ConflictStruct())

	def get_hs_pdsch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:HSPDsch \n
		Snippet: value: int = driver.configure.downlink.carrier.code.get_hs_pdsch() \n
		Sets the first channelization code number of the HS-PDSCH. The number of assigned codes depends on the HSDPA channel
		configuration. For a fixed reference channel for example, it depends on the H-Set. For a user-defined channel, the number
		is configured directly. \n
			:return: channel_code: Range: 0 to 16 - number of assigned codes
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:HSPDsch?')
		return Conversions.str_to_int(response)

	def set_hs_pdsch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:HSPDsch \n
		Snippet: driver.configure.downlink.carrier.code.set_hs_pdsch(channel_code = 1) \n
		Sets the first channelization code number of the HS-PDSCH. The number of assigned codes depends on the HSDPA channel
		configuration. For a fixed reference channel for example, it depends on the H-Set. For a user-defined channel, the number
		is configured directly. \n
			:param channel_code: Range: 0 to 16 - number of assigned codes
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:HSPDsch {param}')

	def get_eagch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:EAGCh \n
		Snippet: value: int = driver.configure.downlink.carrier.code.get_eagch() \n
		Sets the channelization code number of the E-AGCH. \n
			:return: channel_code: Range: 0 to 255
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:EAGCh?')
		return Conversions.str_to_int(response)

	def set_eagch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:EAGCh \n
		Snippet: driver.configure.downlink.carrier.code.set_eagch(channel_code = 1) \n
		Sets the channelization code number of the E-AGCH. \n
			:param channel_code: Range: 0 to 255
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:EAGCh {param}')

	def get_ergch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:ERGCh \n
		Snippet: value: int = driver.configure.downlink.carrier.code.get_ergch() \n
		E-HICH and E-RGCH use the same channelization code number. Any of the two commands sets the channelization code number
		for both channels. \n
			:return: channel_code: Range: 0 to 127
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:ERGCh?')
		return Conversions.str_to_int(response)

	def set_ergch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:ERGCh \n
		Snippet: driver.configure.downlink.carrier.code.set_ergch(channel_code = 1) \n
		E-HICH and E-RGCH use the same channelization code number. Any of the two commands sets the channelization code number
		for both channels. \n
			:param channel_code: Range: 0 to 127
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:ERGCh {param}')

	def get_ehich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:EHICh \n
		Snippet: value: int = driver.configure.downlink.carrier.code.get_ehich() \n
		E-HICH and E-RGCH use the same channelization code number. Any of the two commands sets the channelization code number
		for both channels. \n
			:return: channel_code: Range: 0 to 127
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:EHICh?')
		return Conversions.str_to_int(response)

	def set_ehich(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:EHICh \n
		Snippet: driver.configure.downlink.carrier.code.set_ehich(channel_code = 1) \n
		E-HICH and E-RGCH use the same channelization code number. Any of the two commands sets the channelization code number
		for both channels. \n
			:param channel_code: Range: 0 to 127
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:EHICh {param}')

	def get_pcpich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:CODE:PCPich \n
		Snippet: value: int = driver.configure.downlink.carrier.code.get_pcpich() \n
		Queries the channelization code number of the P-CPICH. \n
			:return: channel_code: The returned value is fixed. Range: 0
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:CODE:PCPich?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Code':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Code(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
