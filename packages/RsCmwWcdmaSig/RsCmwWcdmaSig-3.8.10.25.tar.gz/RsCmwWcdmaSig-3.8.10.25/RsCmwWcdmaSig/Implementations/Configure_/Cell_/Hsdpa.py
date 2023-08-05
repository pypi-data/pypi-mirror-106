from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsdpa:
	"""Hsdpa commands group definition. 23 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsdpa", core, parent)

	@property
	def ueCategory(self):
		"""ueCategory commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .Hsdpa_.UeCategory import UeCategory
			self._ueCategory = UeCategory(self._core, self._base)
		return self._ueCategory

	@property
	def fixed(self):
		"""fixed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fixed'):
			from .Hsdpa_.Fixed import Fixed
			self._fixed = Fixed(self._core, self._base)
		return self._fixed

	@property
	def cqi(self):
		"""cqi commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_cqi'):
			from .Hsdpa_.Cqi import Cqi
			self._cqi = Cqi(self._core, self._base)
		return self._cqi

	@property
	def userDefined(self):
		"""userDefined commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_userDefined'):
			from .Hsdpa_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	def get_anr_factor(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:ANRFactor \n
		Snippet: value: int = driver.configure.cell.hsdpa.get_anr_factor() \n
		Specifies the number of transmissions of the same ACK/NACK (ACK/NACK repetition factor) . \n
			:return: factor: Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:ANRFactor?')
		return Conversions.str_to_int(response)

	def set_anr_factor(self, factor: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:ANRFactor \n
		Snippet: driver.configure.cell.hsdpa.set_anr_factor(factor = 1) \n
		Specifies the number of transmissions of the same ACK/NACK (ACK/NACK repetition factor) . \n
			:param factor: Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(factor)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:ANRFactor {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.ChannelType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:TYPE \n
		Snippet: value: enums.ChannelType = driver.configure.cell.hsdpa.get_type_py() \n
		Selects the configuration type of the high-speed downlink shared channel (HS-DSCH) . \n
			:return: channel_type: FIXed | CQI | UDEFined FIXed: fixed reference channel CQI: channel for CQI reporting tests UDEFined: user-defined channel configuration
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelType)

	def set_type_py(self, channel_type: enums.ChannelType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:TYPE \n
		Snippet: driver.configure.cell.hsdpa.set_type_py(channel_type = enums.ChannelType.CQI) \n
		Selects the configuration type of the high-speed downlink shared channel (HS-DSCH) . \n
			:param channel_type: FIXed | CQI | UDEFined FIXed: fixed reference channel CQI: channel for CQI reporting tests UDEFined: user-defined channel configuration
		"""
		param = Conversions.enum_scalar_to_str(channel_type, enums.ChannelType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:TYPE {param}')

	def clone(self) -> 'Hsdpa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsdpa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
