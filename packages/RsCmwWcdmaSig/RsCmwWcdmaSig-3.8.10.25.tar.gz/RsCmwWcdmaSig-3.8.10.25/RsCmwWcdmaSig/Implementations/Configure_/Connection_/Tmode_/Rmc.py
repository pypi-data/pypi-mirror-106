from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmc:
	"""Rmc commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmc", core, parent)

	# noinspection PyTypeChecker
	def get_domain(self) -> enums.RmcDomain:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DOMain \n
		Snippet: value: enums.RmcDomain = driver.configure.connection.tmode.rmc.get_domain() \n
		Specifies the CS or PS domain for RMC connections in test mode. \n
			:return: domain: CS | PS Circuit switched, packet switched
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DOMain?')
		return Conversions.str_to_scalar_enum(response, enums.RmcDomain)

	def set_domain(self, domain: enums.RmcDomain) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DOMain \n
		Snippet: driver.configure.connection.tmode.rmc.set_domain(domain = enums.RmcDomain.CS) \n
		Specifies the CS or PS domain for RMC connections in test mode. \n
			:param domain: CS | PS Circuit switched, packet switched
		"""
		param = Conversions.enum_scalar_to_str(domain, enums.RmcDomain)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DOMain {param}')

	# noinspection PyTypeChecker
	def get_data(self) -> enums.BitPattern:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DATA \n
		Snippet: value: enums.BitPattern = driver.configure.connection.tmode.rmc.get_data() \n
		Selects the bit pattern transmitted as user information on the DTCH. Besides 'All 0', 'All 1' and 'Alternating 0101...',
		pseudo-random bit sequences of variable length are available. \n
			:return: pattern: ALL0 | ALL1 | ALTernating | PRBS9 | PRBS11 | PRBS13 | PRBS15
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.BitPattern)

	def set_data(self, pattern: enums.BitPattern) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DATA \n
		Snippet: driver.configure.connection.tmode.rmc.set_data(pattern = enums.BitPattern.ALL0) \n
		Selects the bit pattern transmitted as user information on the DTCH. Besides 'All 0', 'All 1' and 'Alternating 0101...',
		pseudo-random bit sequences of variable length are available. \n
			:param pattern: ALL0 | ALL1 | ALTernating | PRBS9 | PRBS11 | PRBS13 | PRBS15
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.BitPattern)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DATA {param}')

	# noinspection PyTypeChecker
	def get_dl_resources(self) -> enums.FilledBlocks:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DLRessources \n
		Snippet: value: enums.FilledBlocks = driver.configure.connection.tmode.rmc.get_dl_resources() \n
		Selects the percentage of DL RMC transport blocks that are filled with information bits. The percentages are rounded,
		indicated in one-tenth of a percent and correspond to values 1/N, indicating that out of N transport blocks, only one is
		fully filled with data. (N – 1) blocks are empty. Example: P0125 = 125 ‰ = 0.125 = 1/8. Each 8th block is filled. \n
			:return: filled_blocks: P0031 | P0033 | P0036 | P0038 | P0042 | P0045 | P0050 | P0056 | P0062 | P0071 | P0083 | P0100 | P0125 | P0167 | P0250 | P0500 | P1000 P0031: 1/32 P0033: 1/30 P0036: 1/28 P0038: 1/26 P0042: 1/24 P0045: 1/22 P0050: 1/20 P0056: 1/18 P0062: 1/16 P0071: 1/14 P0083: 1/12 P0100: 1/10 P0125: 1/8 P0167: 1/6 P0250: 1/4 P0500: 1/2 P1000: all blocks filled
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DLRessources?')
		return Conversions.str_to_scalar_enum(response, enums.FilledBlocks)

	def set_dl_resources(self, filled_blocks: enums.FilledBlocks) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DLRessources \n
		Snippet: driver.configure.connection.tmode.rmc.set_dl_resources(filled_blocks = enums.FilledBlocks.P0031) \n
		Selects the percentage of DL RMC transport blocks that are filled with information bits. The percentages are rounded,
		indicated in one-tenth of a percent and correspond to values 1/N, indicating that out of N transport blocks, only one is
		fully filled with data. (N – 1) blocks are empty. Example: P0125 = 125 ‰ = 0.125 = 1/8. Each 8th block is filled. \n
			:param filled_blocks: P0031 | P0033 | P0036 | P0038 | P0042 | P0045 | P0050 | P0056 | P0062 | P0071 | P0083 | P0100 | P0125 | P0167 | P0250 | P0500 | P1000 P0031: 1/32 P0033: 1/30 P0036: 1/28 P0038: 1/26 P0042: 1/24 P0045: 1/22 P0050: 1/20 P0056: 1/18 P0062: 1/16 P0071: 1/14 P0083: 1/12 P0100: 1/10 P0125: 1/8 P0167: 1/6 P0250: 1/4 P0500: 1/2 P1000: all blocks filled
		"""
		param = Conversions.enum_scalar_to_str(filled_blocks, enums.FilledBlocks)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DLRessources {param}')

	def get_ucrc(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:UCRC \n
		Snippet: value: bool = driver.configure.connection.tmode.rmc.get_ucrc() \n
		Enables or disables the uplink cyclic redundancy check (CRC) for loop mode 2. This setting is only relevant when an RMC
		with symmetric DL/UL data rate is used. The setting is separate for normal signaling and reduce signaling mode.
		First enable or disable reduced signaling mode (see 'Cell Setup') and afterwards configure the 'Loop Mode 2 Sym. UL CRC'. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:UCRC?')
		return Conversions.str_to_bool(response)

	def set_ucrc(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:UCRC \n
		Snippet: driver.configure.connection.tmode.rmc.set_ucrc(enable = False) \n
		Enables or disables the uplink cyclic redundancy check (CRC) for loop mode 2. This setting is only relevant when an RMC
		with symmetric DL/UL data rate is used. The setting is separate for normal signaling and reduce signaling mode.
		First enable or disable reduced signaling mode (see 'Cell Setup') and afterwards configure the 'Loop Mode 2 Sym. UL CRC'. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:UCRC {param}')

	# noinspection PyTypeChecker
	def get_rlc_mode(self) -> enums.RlcMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:RLCMode \n
		Snippet: value: enums.RlcMode = driver.configure.connection.tmode.rmc.get_rlc_mode() \n
		Selects the RLC mode for RMC transmission with loop mode 1. \n
			:return: mode: TRANsparent | ACKNowledge
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:RLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.RlcMode)

	def set_rlc_mode(self, mode: enums.RlcMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:RLCMode \n
		Snippet: driver.configure.connection.tmode.rmc.set_rlc_mode(mode = enums.RlcMode.ACKNowledge) \n
		Selects the RLC mode for RMC transmission with loop mode 1. \n
			:param mode: TRANsparent | ACKNowledge
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RlcMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:RLCMode {param}')

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Downlink: enums.RefChannelDataRate: R12K2 | R64K | R144k | R384k R12K2: 12.2 kbps R64K: 64 kbps R144k: 144 kbps R384k: 384 kbps
			- Uplink: enums.RefChannelDataRate: R12K2 | R64K | R144k | R384k | R768k R12K2: 12.2 kbps R64K: 64 kbps R144k: 144 kbps R384k: 384 kbps R768k: 768 kbps"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Downlink', enums.RefChannelDataRate),
			ArgStruct.scalar_enum('Uplink', enums.RefChannelDataRate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Downlink: enums.RefChannelDataRate = None
			self.Uplink: enums.RefChannelDataRate = None

	# noinspection PyTypeChecker
	def get_drate(self) -> DrateStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DRATe \n
		Snippet: value: DrateStruct = driver.configure.connection.tmode.rmc.get_drate() \n
		Selects the information bit rate of the downlink and uplink reference channel. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DRATe?', self.__class__.DrateStruct())

	def set_drate(self, value: DrateStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:DRATe \n
		Snippet: driver.configure.connection.tmode.rmc.set_drate(value = DrateStruct()) \n
		Selects the information bit rate of the downlink and uplink reference channel. \n
			:param value: see the help for DrateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:DRATe', value)

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.UtranTestMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:TMODe \n
		Snippet: value: enums.UtranTestMode = driver.configure.connection.tmode.rmc.get_tmode() \n
		Selects the test mode that the UE enters after connecting to the UTRAN. \n
			:return: type_py: OFF | MODE1 | MODE2 OFF: no loop MODE1: loop mode 1 MODE2: loop mode 2
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.UtranTestMode)

	def set_tmode(self, type_py: enums.UtranTestMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:RMC:TMODe \n
		Snippet: driver.configure.connection.tmode.rmc.set_tmode(type_py = enums.UtranTestMode.MODE1) \n
		Selects the test mode that the UE enters after connecting to the UTRAN. \n
			:param type_py: OFF | MODE1 | MODE2 OFF: no loop MODE1: loop mode 1 MODE2: loop mode 2
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.UtranTestMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:RMC:TMODe {param}')
