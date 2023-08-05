from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tchspa:
	"""Tchspa commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tchspa", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bb_Board_1: enums.BasebandBoard: First signaling unit
			- Bb_Board_2: enums.BasebandBoard: Second signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the first input path
			- Rx_Converter: enums.RxConverter: RX module for the first input path
			- Rx_2_Connector: enums.RxConnector: RF connector for the second input path
			- Rx_2_Converter: enums.RxConverter: RX module for the second input path.
			- Tx_Connector: enums.TxConnector: RF connector for the first output path
			- Tx_Converter: enums.TxConverter: TX module for the first output path
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path. Select different modules for the path one and two.
			- Tx_3_Connector: enums.TxConnector: RF connector for the third output path
			- Tx_3_Converter: enums.TxConverter: TX module for the third output path. Select different modules for the three paths or use the path one."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board_1', enums.BasebandBoard),
			ArgStruct.scalar_enum('Bb_Board_2', enums.BasebandBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_2_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_2_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board_1: enums.BasebandBoard = None
			self.Bb_Board_2: enums.BasebandBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Rx_2_Connector: enums.RxConnector = None
			self.Rx_2_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:TCHSpa:FLEXible \n
		Snippet: value: FlexibleStruct = driver.route.scenario.tchspa.get_flexible() \n
		Activates the scenario '3C HSPA' and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:TCHSpa:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:TCHSpa:FLEXible \n
		Snippet: driver.route.scenario.tchspa.set_flexible(value = FlexibleStruct()) \n
		Activates the scenario '3C HSPA' and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:TCHSpa:FLEXible', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the first input path
			- Rx_Converter: enums.RxConverter: RX module for the first input path
			- Rx_2_Connector: enums.RxConnector: RF connector for the second input path
			- Rx_2_Converter: enums.RxConverter: RX module for the second input path.
			- Tx_Connector: enums.TxConnector: RF connector for the first output path
			- Tx_Converter: enums.TxConverter: TX module for the first output path
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path. Select different modules for the path one and two.
			- Tx_3_Connector: enums.TxConnector: RF connector for the third output path
			- Tx_3_Converter: enums.TxConverter: TX module for the third output path. Select different modules for the three paths or use the path one."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_2_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_2_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_3_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_3_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Rx_2_Connector: enums.RxConnector = None
			self.Rx_2_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Tx_3_Connector: enums.TxConnector = None
			self.Tx_3_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:TCHSpa \n
		Snippet: value: ValueStruct = driver.route.scenario.tchspa.get_value() \n
		Activates the scenario '3C HSPA' and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:TCHSpa?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:TCHSpa \n
		Snippet: driver.route.scenario.tchspa.set_value(value = ValueStruct()) \n
		Activates the scenario '3C HSPA' and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:TCHSpa', value)
