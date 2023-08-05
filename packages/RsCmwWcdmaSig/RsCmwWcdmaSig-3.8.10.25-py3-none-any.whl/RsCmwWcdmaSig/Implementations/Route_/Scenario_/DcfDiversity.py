from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcfDiversity:
	"""DcfDiversity commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dcfDiversity", core, parent)

	@property
	def flexible(self):
		"""flexible commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_flexible'):
			from .DcfDiversity_.Flexible import Flexible
			self._flexible = Flexible(self._core, self._base)
		return self._flexible

	# noinspection PyTypeChecker
	class ExternalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the first output path
			- Tx_Converter: enums.TxConverter: TX module for the first output path. Select different modules for the two paths.
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path
			- Iq_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the first output path. Select different connectors for the two paths.
			- Iq_2_Connector: enums.TxConnector: DIG IQ OUT connector for external fading of the second output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Iq_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_2_Connector', enums.TxConnector)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Iq_Connector: enums.TxConnector = None
			self.Iq_2_Connector: enums.TxConnector = None

	# noinspection PyTypeChecker
	def get_external(self) -> ExternalStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DCFDiversity[:EXTernal] \n
		Snippet: value: ExternalStruct = driver.route.scenario.dcfDiversity.get_external() \n
		Activates the 'Dual Carrier RX Diversity Fading: External' scenario and selects the signal paths. For possible connector
		and converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ExternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DCFDiversity:EXTernal?', self.__class__.ExternalStruct())

	def set_external(self, value: ExternalStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DCFDiversity[:EXTernal] \n
		Snippet: driver.route.scenario.dcfDiversity.set_external(value = ExternalStruct()) \n
		Activates the 'Dual Carrier RX Diversity Fading: External' scenario and selects the signal paths. For possible connector
		and converter values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for ExternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DCFDiversity:EXTernal', value)

	# noinspection PyTypeChecker
	class InternalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the first output path
			- Tx_Converter: enums.TxConverter: TX module for the first output path. Select different modules for the two paths.
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path. Select different modules for the two paths.
			- Fader: enums.Fader: Internal fader"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Fader', enums.Fader)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None
			self.Fader: enums.Fader = None

	# noinspection PyTypeChecker
	def get_internal(self) -> InternalStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DCFDiversity:INTernal \n
		Snippet: value: InternalStruct = driver.route.scenario.dcfDiversity.get_internal() \n
		Activates the 'Dual Carrier RX Diversity Fading: Internal' scenario and selects the signal paths. For possible parameter
		values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for InternalStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DCFDiversity:INTernal?', self.__class__.InternalStruct())

	def set_internal(self, value: InternalStruct) -> None:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario:DCFDiversity:INTernal \n
		Snippet: driver.route.scenario.dcfDiversity.set_internal(value = InternalStruct()) \n
		Activates the 'Dual Carrier RX Diversity Fading: Internal' scenario and selects the signal paths. For possible parameter
		values, see 'Values for Signal Path Selection'. \n
			:param value: see the help for InternalStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario:DCFDiversity:INTernal', value)

	def clone(self) -> 'DcfDiversity':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DcfDiversity(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
