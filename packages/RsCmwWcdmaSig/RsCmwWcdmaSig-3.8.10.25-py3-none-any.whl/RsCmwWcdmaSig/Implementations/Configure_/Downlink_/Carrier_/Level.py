from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 11 total commands, 1 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	@property
	def hsscch(self):
		"""hsscch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsscch'):
			from .Level_.Hsscch import Hsscch
			self._hsscch = Hsscch(self._core, self._base)
		return self._hsscch

	def get_apower(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:APOWer \n
		Snippet: value: float = driver.configure.downlink.carrier.level.get_apower() \n
		Queries the accumulated power (total power of all active channels relative to the base level of the generator) . \n
			:return: power: Range: -80 dB to 10 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:APOWer?')
		return Conversions.str_to_float(response)

	def get_ehich(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:EHICh \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_ehich() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel indicated
		by the last mnemonic. E-HICH and E-RGCH use the same power level. Setting the level for one channel sets the same level
		for the other channel. Disabling the E-HICH disables also the E-RGCH. Enabling the E-RGCH enables also the E-HICH. \n
			:return: level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:EHICh?')
		return Conversions.str_to_float_or_bool(response)

	def set_ehich(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:EHICh \n
		Snippet: driver.configure.downlink.carrier.level.set_ehich(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel indicated
		by the last mnemonic. E-HICH and E-RGCH use the same power level. Setting the level for one channel sets the same level
		for the other channel. Disabling the E-HICH disables also the E-RGCH. Enabling the E-RGCH enables also the E-HICH. \n
			:param level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:EHICh {param}')

	def get_ergch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:ERGCh \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_ergch() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel indicated
		by the last mnemonic. E-HICH and E-RGCH use the same power level. Setting the level for one channel sets the same level
		for the other channel. Disabling the E-HICH disables also the E-RGCH. Enabling the E-RGCH enables also the E-HICH. \n
			:return: level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:ERGCh?')
		return Conversions.str_to_float_or_bool(response)

	def set_ergch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:ERGCh \n
		Snippet: driver.configure.downlink.carrier.level.set_ergch(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel indicated
		by the last mnemonic. E-HICH and E-RGCH use the same power level. Setting the level for one channel sets the same level
		for the other channel. Disabling the E-HICH disables also the E-RGCH. Enabling the E-RGCH enables also the E-HICH. \n
			:param level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:ERGCh {param}')

	def get_eagch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:EAGCh \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_eagch() \n
		Sets the level of the E-AGCH. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:EAGCh?')
		return Conversions.str_to_float_or_bool(response)

	def set_eagch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:EAGCh \n
		Snippet: driver.configure.downlink.carrier.level.set_eagch(level = 1.0) \n
		Sets the level of the E-AGCH. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:EAGCh {param}')

	def get_hs_pdsch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:HSPDsch \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_hs_pdsch() \n
		Sets the level of the HS-PDSCH summed over all active codes. Setting a power level also enables the channel. \n
			:return: level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disable | enable the channel)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:HSPDsch?')
		return Conversions.str_to_float_or_bool(response)

	def set_hs_pdsch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:HSPDsch \n
		Snippet: driver.configure.downlink.carrier.level.set_hs_pdsch(level = 1.0) \n
		Sets the level of the HS-PDSCH summed over all active codes. Setting a power level also enables the channel. \n
			:param level: Range: -80 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disable | enable the channel)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:HSPDsch {param}')

	def get_psch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PSCH \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_psch() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PSCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_psch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PSCH \n
		Snippet: driver.configure.downlink.carrier.level.set_psch(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PSCH {param}')

	def get_ssch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:SSCH \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_ssch() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:SSCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_ssch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:SSCH \n
		Snippet: driver.configure.downlink.carrier.level.set_ssch(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:SSCH {param}')

	def get_pcpich(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PCPich \n
		Snippet: value: float = driver.configure.downlink.carrier.level.get_pcpich() \n
		Sets the level of the P-CPICH. \n
			:return: level: Range: -80 dB to 0 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PCPich?')
		return Conversions.str_to_float(response)

	def set_pcpich(self, level: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PCPich \n
		Snippet: driver.configure.downlink.carrier.level.set_pcpich(level = 1.0) \n
		Sets the level of the P-CPICH. \n
			:param level: Range: -80 dB to 0 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PCPich {param}')

	def get_pccpch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PCCPch \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_pccpch() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PCCPch?')
		return Conversions.str_to_float_or_bool(response)

	def set_pccpch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:PCCPch \n
		Snippet: driver.configure.downlink.carrier.level.set_pccpch(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:PCCPch {param}')

	def get_fdpch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:FDPCh \n
		Snippet: value: float or bool = driver.configure.downlink.carrier.level.get_fdpch() \n
		Sets the level of F-DPCH. The settings of DPCH level and F-DPCH level are equal. F-DPCH is activated instead of DPCH
		while the CPC feature is active or while a secondary uplink is enabled \n
			:return: level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:FDPCh?')
		return Conversions.str_to_float_or_bool(response)

	def set_fdpch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:LEVel:FDPCh \n
		Snippet: driver.configure.downlink.carrier.level.set_fdpch(level = 1.0) \n
		Sets the level of F-DPCH. The settings of DPCH level and F-DPCH level are equal. F-DPCH is activated instead of DPCH
		while the CPC feature is active or while a secondary uplink is enabled \n
			:param level: Range: -80 dB to 0 dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:LEVel:FDPCh {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
