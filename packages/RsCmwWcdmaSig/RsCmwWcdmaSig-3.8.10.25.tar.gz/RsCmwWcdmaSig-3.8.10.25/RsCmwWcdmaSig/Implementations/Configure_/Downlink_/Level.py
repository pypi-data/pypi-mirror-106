from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 6 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adjust'):
			from .Level_.Adjust import Adjust
			self._adjust = Adjust(self._core, self._base)
		return self._adjust

	def get_scpich(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:SCPich \n
		Snippet: value: float or bool = driver.configure.downlink.level.get_scpich() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:SCPich?')
		return Conversions.str_to_float_or_bool(response)

	def set_scpich(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:SCPich \n
		Snippet: driver.configure.downlink.level.set_scpich(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:SCPich {param}')

	def get_sccpch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:SCCPch \n
		Snippet: value: float or bool = driver.configure.downlink.level.get_sccpch() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:SCCPch?')
		return Conversions.str_to_float_or_bool(response)

	def set_sccpch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:SCCPch \n
		Snippet: driver.configure.downlink.level.set_sccpch(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:SCCPch {param}')

	def get_pich(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:PICH \n
		Snippet: value: float or bool = driver.configure.downlink.level.get_pich() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:PICH?')
		return Conversions.str_to_float_or_bool(response)

	def set_pich(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:PICH \n
		Snippet: driver.configure.downlink.level.set_pich(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:PICH {param}')

	def get_aich(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:AICH \n
		Snippet: value: float or bool = driver.configure.downlink.level.get_aich() \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:return: level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:AICH?')
		return Conversions.str_to_float_or_bool(response)

	def set_aich(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:AICH \n
		Snippet: driver.configure.downlink.level.set_aich(level = 1.0) \n
		Set the level of the channel indicated by the last mnemonic. Setting a power level also activates the channel. \n
			:param level: Range: -80 dB to 0 dB, AICH: -50 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:AICH {param}')

	def get_dpch(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:DPCH \n
		Snippet: value: float or bool = driver.configure.downlink.level.get_dpch() \n
		Set the level of DPCH. The settings of DPCH level and F-DPCH level are equal. \n
			:return: level: Range: -80 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:DPCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_dpch(self, level: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:DPCH \n
		Snippet: driver.configure.downlink.level.set_dpch(level = 1.0) \n
		Set the level of DPCH. The settings of DPCH level and F-DPCH level are equal. \n
			:param level: Range: -80 dB to 0 dB , Unit: dB Additional parameters: OFF | ON (disables the channel | enables the channel using the previous/default level)
		"""
		param = Conversions.decimal_or_bool_value_to_str(level)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:DPCH {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
