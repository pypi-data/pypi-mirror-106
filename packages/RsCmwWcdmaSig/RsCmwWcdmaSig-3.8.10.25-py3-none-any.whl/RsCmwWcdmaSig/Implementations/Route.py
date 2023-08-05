from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Route:
	"""Route commands group definition. 34 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 10 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Route_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SCELl | DCARrier | SCFading | DCFading | SCFDiversity | DCFDiversity | DBFading | DBFDiversity | DCHSpa | TCHSpa SCEL: 'Standard Cell' DCARrier: 'Dual Carrier' SCFading: 'Standard Cell Fading' DCFading: 'Dual Carrier Fading' SCFDiversity: 'Standard Cell RX Diversity Fading' DCFDiversity: 'Dual Carrier RX Diversity Fading' DBFading: 'Dual Carrier / Dual Band Fading' DBFDiversity: 'Dual Carrier / Dual Band RX Diversity Fading' DCHSpa: 'Dual Carrier HSPA' TCHSpa: '3C HSPA'
			- Master: str: For future use - returned value not relevant
			- Rx_Connector: enums.RxConnector: RF connector for input path 1
			- Rx_Converter: enums.RxConverter: RX module for input path 1
			- Rx_2_Connector: enums.RxConnector: RF connector for input path 2
			- Rx_2_Converter: enums.RxConverter: RX module for input path 2
			- Tx_Connector: enums.TxConnector: RF connector for output path 1
			- Tx_Converter: enums.TxConverter: TX module for output path 1
			- Tx_2_Connector: enums.TxConnector: RF connector for output path 2
			- Tx_2_Converter: enums.TxConverter: TX module for output path 2
			- Tx_3_Connector: enums.TxConnector: RF connector for output path 2
			- Tx_3_Converter: enums.TxConverter: TX module for output path 2
			- Tx_4_Connector: enums.TxConnector: RF connector for output path 3
			- Tx_4_Converter: enums.TxConverter: TX module for output path 4
			- Iq_Connector: enums.TxConnector: DIG IQ OUT connector for output path 1
			- Iq_2_Connector: enums.TxConnector: DIG IQ OUT connector for output path 2
			- Iq_3_Connector: enums.TxConnector: DIG IQ OUT connector for output path 3
			- Iq_4_Connector: enums.TxConnector: DIG IQ OUT connector for output path 4
			- Fader: enums.Fader: I/Q board with I/Q connectors"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Rx_2_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_2_Converter', enums.RxConverter),
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
			ArgStruct.scalar_enum('Iq_4_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Fader', enums.Fader)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Master: str = None
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
			self.Tx_4_Connector: enums.TxConnector = None
			self.Tx_4_Converter: enums.TxConverter = None
			self.Iq_Connector: enums.TxConnector = None
			self.Iq_2_Connector: enums.TxConnector = None
			self.Iq_3_Connector: enums.TxConnector = None
			self.Iq_4_Connector: enums.TxConnector = None
			self.Fader: enums.Fader = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Returns the configured routing settings. The number of returned values depends on the active scenario (6 to 18 values) .
		For possible connector and converter values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Route':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Route(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
