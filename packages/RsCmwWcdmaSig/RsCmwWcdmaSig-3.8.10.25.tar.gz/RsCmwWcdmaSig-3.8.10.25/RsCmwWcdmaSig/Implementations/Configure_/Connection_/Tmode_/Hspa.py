from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hspa:
	"""Hspa commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hspa", core, parent)

	# noinspection PyTypeChecker
	def get_procedure(self) -> enums.Procedure:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:PROCedure \n
		Snippet: value: enums.Procedure = driver.configure.connection.tmode.hspa.get_procedure() \n
		Selects whether an HSPA test mode connection is set up automatically when a test mode connection is established, or can
		be set up manually later on. \n
			:return: procedure: CSPS | CSOPs CSPS: Establish both an RMC connection in the CS domain and an HSPA test mode connection in the PS domain. CSOPs: Establish only an RMC connection in the CS domain. You can trigger an HSPA connection setup manually later on if desired.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:PROCedure?')
		return Conversions.str_to_scalar_enum(response, enums.Procedure)

	def set_procedure(self, procedure: enums.Procedure) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:PROCedure \n
		Snippet: driver.configure.connection.tmode.hspa.set_procedure(procedure = enums.Procedure.CSOPs) \n
		Selects whether an HSPA test mode connection is set up automatically when a test mode connection is established, or can
		be set up manually later on. \n
			:param procedure: CSPS | CSOPs CSPS: Establish both an RMC connection in the CS domain and an HSPA test mode connection in the PS domain. CSOPs: Establish only an RMC connection in the CS domain. You can trigger an HSPA connection setup manually later on if desired.
		"""
		param = Conversions.enum_scalar_to_str(procedure, enums.Procedure)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:PROCedure {param}')

	# noinspection PyTypeChecker
	def get_direction(self) -> enums.HspaTestModeDirection:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:DIRection \n
		Snippet: value: enums.HspaTestModeDirection = driver.configure.connection.tmode.hspa.get_direction() \n
		Selects the HSPA test mode direction. \n
			:return: direction: HSDPa | HSPA HSDPa: HSDPA only HSPA: HSDPA + HSUPA
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.HspaTestModeDirection)

	def set_direction(self, direction: enums.HspaTestModeDirection) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:DIRection \n
		Snippet: driver.configure.connection.tmode.hspa.set_direction(direction = enums.HspaTestModeDirection.HSDPa) \n
		Selects the HSPA test mode direction. \n
			:param direction: HSDPa | HSPA HSDPa: HSDPA only HSPA: HSDPA + HSUPA
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.HspaTestModeDirection)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:DIRection {param}')

	# noinspection PyTypeChecker
	def get_data(self) -> enums.BitPattern:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:DATA \n
		Snippet: value: enums.BitPattern = driver.configure.connection.tmode.hspa.get_data() \n
		Selects the bit pattern to be transmitted as user information on the HS-DSCH. Besides 'All 0', 'All 1' and 'Alternating
		0101...', pseudo-random bit sequences of variable length are available. \n
			:return: pattern: ALL0 | ALL1 | ALTernating | PRBS9 | PRBS11 | PRBS13 | PRBS15
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.BitPattern)

	def set_data(self, pattern: enums.BitPattern) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:DATA \n
		Snippet: driver.configure.connection.tmode.hspa.set_data(pattern = enums.BitPattern.ALL0) \n
		Selects the bit pattern to be transmitted as user information on the HS-DSCH. Besides 'All 0', 'All 1' and 'Alternating
		0101...', pseudo-random bit sequences of variable length are available. \n
			:param pattern: ALL0 | ALL1 | ALTernating | PRBS9 | PRBS11 | PRBS13 | PRBS15
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.BitPattern)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:DATA {param}')

	def get_einsertion(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:EINSertion \n
		Snippet: value: float or bool = driver.configure.connection.tmode.hspa.get_einsertion() \n
		Configures the rate of HS-DSCH data to be sent with an incorrect CRC value. \n
			:return: error_insertion: Range: 10 % to 90 %, Unit: % Additional parameters: OFF | ON (disables the error insertion | enables the error insertion using the previous value)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:EINSertion?')
		return Conversions.str_to_float_or_bool(response)

	def set_einsertion(self, error_insertion: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:EINSertion \n
		Snippet: driver.configure.connection.tmode.hspa.set_einsertion(error_insertion = 1.0) \n
		Configures the rate of HS-DSCH data to be sent with an incorrect CRC value. \n
			:param error_insertion: Range: 10 % to 90 %, Unit: % Additional parameters: OFF | ON (disables the error insertion | enables the error insertion using the previous value)
		"""
		param = Conversions.decimal_or_bool_value_to_str(error_insertion)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:EINSertion {param}')

	def get_usdu(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:USDU \n
		Snippet: value: int = driver.configure.connection.tmode.hspa.get_usdu() \n
		Specifies the HSUPA UL RLC SDU size as an integer multiple of the HSDPA DL RLC SDU size of 2936 bits. Beside the value of
		72 bits, the command accepts a continuous range of values, but sets the nearest multiple of 2936: 72 | 2936 | 5872 | 8808
		| 11744 | 14680 | 17616 | 20552 | 23488 | 26424 | 29360 \n
			:return: size: Range: 72 bits, 2936 bits to 29360 bits , Unit: bit
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:USDU?')
		return Conversions.str_to_int(response)

	def set_usdu(self, size: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:HSPA:USDU \n
		Snippet: driver.configure.connection.tmode.hspa.set_usdu(size = 1) \n
		Specifies the HSUPA UL RLC SDU size as an integer multiple of the HSDPA DL RLC SDU size of 2936 bits. Beside the value of
		72 bits, the command accepts a continuous range of values, but sets the nearest multiple of 2936: 72 | 2936 | 5872 | 8808
		| 11744 | 14680 | 17616 | 20552 | 23488 | 26424 | 29360 \n
			:param size: Range: 72 bits, 2936 bits to 29360 bits , Unit: bit
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:HSPA:USDU {param}')
