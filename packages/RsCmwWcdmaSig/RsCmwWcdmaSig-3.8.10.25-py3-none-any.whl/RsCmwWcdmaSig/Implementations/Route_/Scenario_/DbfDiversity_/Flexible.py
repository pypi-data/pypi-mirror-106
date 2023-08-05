from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flexible:
	"""Flexible commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flexible", core, parent)

	# noinspection PyTypeChecker
	class ExternalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bb_Board_1: enums.BasebandBoard: First signaling unit
			- Bb_Board_2: enums.BasebandBoard: Second signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the first output path of the carrier one
			- Tx_Converter: enums.TxConverter: TX module for the first output path of the carrier one. Select different modules for each of the paths.
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path of the carrier one
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path of the carrier one
			- Tx_3_Connector: enums.TxConnector: RF connector for the first output path of the carrier two
			- Tx_3_Converter: enums.TxConverter: TX module for the first output path of the carrier two
			- Tx_4_Connector: enums.TxConnector: RF connector for the second output path of the carrier two
			- Tx_4_Converter: enums.TxConverter: TX module for the second output path of the carrier two
			- Iq_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the first output path of the carrier one
			- Iq_2_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the second output path of the carrier one
			- Iq_3_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the first output path of the carrier two
			- Iq_4_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the second output path of the carrier two"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board_1', enums.BasebandBoard),
			ArgStruct.scalar_enum('Bb_Board_2', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_4_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Iq_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_4_Connector', enums.TxConnector)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board_1: enums.BasebandBoard = None
			self.Bb_Board_2: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None
			self.Tx_4_Connector: enums.TxConnector = None
			self.Tx_4_Converter: enums.TxConverter = None
			self.Iq_Connector: enums.TxConnector = None
			self.Iq_2_Connector: enums.TxConnector = None
			self.Iq_3_Connector: enums.TxConnector = None
			self.Iq_4_Connector: enums.TxConnector = None

	# noinspection PyTypeChecker
	def get_external(self) -> ExternalStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DBFDiversity:FLEXible[:EXTernal] \n
		Snippet: value: ExternalStruct = driver.route.scenario.dbfDiversity.flexible.get_external() \n
		Activates the 'Dual Carrier / Dual Band RX Diversity Fading: External' scenario and selects the signal paths.
		For possible connector and converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ExternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DBFDiversity:FLEXible:EXTernal?', self.__class__.ExternalStruct())

	def set_external(self, value: ExternalStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DBFDiversity:FLEXible[:EXTernal] \n
		Snippet: driver.route.scenario.dbfDiversity.flexible.set_external(value = ExternalStruct()) \n
		Activates the 'Dual Carrier / Dual Band RX Diversity Fading: External' scenario and selects the signal paths.
		For possible connector and converter values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for ExternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DBFDiversity:FLEXible:EXTernal', value)

	# noinspection PyTypeChecker
	class InternalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bb_Board_1: enums.BasebandBoard: First signaling unit
			- Bb_Board_2: enums.BasebandBoard: Second signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the first output path of the carrier one
			- Tx_Converter: enums.TxConverter: TX module for the first output path of the carrier one. Select different modules for each of the paths.
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path of the carrier one
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path of the carrier one
			- Tx_3_Connector: enums.TxConnector: RF connector for the first output path of the carrier two
			- Tx_3_Converter: enums.TxConverter: TX module for the first output path of the carrier two
			- Tx_4_Connector: enums.TxConnector: RF connector for the second output path of the carrier two
			- Tx_4_Converter: enums.TxConverter: TX module for the second output path of the carrier two
			- Fader_1: enums.Fader: Internal fader used for the second output path of carrier one.
			- Fader_2: enums.Fader: Internal fader used for the second output path of carrier two. Select different boards for the two carriers."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board_1', enums.BasebandBoard),
			ArgStruct.scalar_enum('Bb_Board_2', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_4_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Fader_1', enums.Fader),
			ArgStruct.scalar_enum('Fader_2', enums.Fader)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board_1: enums.BasebandBoard = None
			self.Bb_Board_2: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None
			self.Tx_4_Connector: enums.TxConnector = None
			self.Tx_4_Converter: enums.TxConverter = None
			self.Fader_1: enums.Fader = None
			self.Fader_2: enums.Fader = None

	# noinspection PyTypeChecker
	def get_internal(self) -> InternalStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DBFDiversity:FLEXible:INTernal \n
		Snippet: value: InternalStruct = driver.route.scenario.dbfDiversity.flexible.get_internal() \n
		Activates the 'Dual Carrier / Dual Band RX Diversity Fading: Internal' scenario and selects the signal paths.
		For possible connector and converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for InternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DBFDiversity:FLEXible:INTernal?', self.__class__.InternalStruct())

	def set_internal(self, value: InternalStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DBFDiversity:FLEXible:INTernal \n
		Snippet: driver.route.scenario.dbfDiversity.flexible.set_internal(value = InternalStruct()) \n
		Activates the 'Dual Carrier / Dual Band RX Diversity Fading: Internal' scenario and selects the signal paths.
		For possible connector and converter values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for InternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DBFDiversity:FLEXible:INTernal', value)
