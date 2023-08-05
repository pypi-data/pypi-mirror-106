from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rohc:
	"""Rohc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rohc", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:ROHC:ENABle \n
		Snippet: value: bool = driver.configure.connection.packet.rohc.get_enable() \n
		Enables or disables robust header compression for PS connections. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:ROHC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:ROHC:ENABle \n
		Snippet: driver.configure.connection.packet.rohc.set_enable(enable = False) \n
		Enables or disables robust header compression for PS connections. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:ROHC:ENABle {param}')

	# noinspection PyTypeChecker
	class ProfilesStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Profiles_0_X_001: bool: OFF | ON IP/UDP/RTP
			- Profiles_0_X_002: bool: OFF | ON IP/UDP
			- Profiles_0_X_004: bool: OFF | ON IP"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Profiles_0_X_001'),
			ArgStruct.scalar_bool('Profiles_0_X_002'),
			ArgStruct.scalar_bool('Profiles_0_X_004')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Profiles_0_X_001: bool = None
			self.Profiles_0_X_002: bool = None
			self.Profiles_0_X_004: bool = None

	def get_profiles(self) -> ProfilesStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:ROHC:PROFiles \n
		Snippet: value: ProfilesStruct = driver.configure.connection.packet.rohc.get_profiles() \n
		Defines which profiles are allowed to be used by the UE in uplink. \n
			:return: structure: for return value, see the help for ProfilesStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:ROHC:PROFiles?', self.__class__.ProfilesStruct())

	def set_profiles(self, value: ProfilesStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:ROHC:PROFiles \n
		Snippet: driver.configure.connection.packet.rohc.set_profiles(value = ProfilesStruct()) \n
		Defines which profiles are allowed to be used by the UE in uplink. \n
			:param value: see the help for ProfilesStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:ROHC:PROFiles', value)
