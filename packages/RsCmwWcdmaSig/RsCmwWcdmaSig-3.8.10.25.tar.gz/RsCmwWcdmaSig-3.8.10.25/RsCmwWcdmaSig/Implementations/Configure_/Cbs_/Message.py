from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Message:
	"""Message commands group definition. 14 total commands, 3 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("message", core, parent)

	@property
	def language(self):
		"""language commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_language'):
			from .Message_.Language import Language
			self._language = Language(self._core, self._base)
		return self._language

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .Message_.File import File
			self._file = File(self._core, self._base)
		return self._file

	@property
	def etws(self):
		"""etws commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_etws'):
			from .Message_.Etws import Etws
			self._etws = Etws(self._core, self._base)
		return self._etws

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: value: bool = driver.configure.cbs.message.get_enable() \n
		Enables the particular CB message. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ENABle \n
		Snippet: driver.configure.cbs.message.set_enable(enable = False) \n
		Enables the particular CB message. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ENABle {param}')

	def get_id(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: value: int = driver.configure.cbs.message.get_id() \n
		Identifies source/type of a CB message. Edit this parameter for user-defined settings. Hexadecimal values are displayed
		for information. \n
			:return: idn: Range: 0 to 65.535E+3
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ID?')
		return Conversions.str_to_int(response)

	def set_id(self, idn: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:ID \n
		Snippet: driver.configure.cbs.message.set_id(idn = 1) \n
		Identifies source/type of a CB message. Edit this parameter for user-defined settings. Hexadecimal values are displayed
		for information. \n
			:param idn: Range: 0 to 65.535E+3
		"""
		param = Conversions.decimal_value_to_str(idn)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:ID {param}')

	# noinspection PyTypeChecker
	def get_id_type(self) -> enums.CbsMessageSeverity:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: value: enums.CbsMessageSeverity = driver.configure.cbs.message.get_id_type() \n
		Specifies the severity of the CBS message ID as either decimal or hexadecimal number. \n
			:return: type_py: UDEFined | APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest UDEFined: user defined APResidentia: presidential level alerts (IDs 4370 and 4383) AEXTreme: extreme alerts (IDs 4371 to 4372 and 4384 to 4385) ASEVere: severe alerts (IDs 4373 to 4378 and 4386 to 4391) AAMBer: amber alerts (IDs 4379 and 4392) EARThquake: earthquake warning (ID 4352) TSUNami: tsunami warning (ID 4353) ETWarning: earthquake and tsunami warning (ID 4354) ETWTest: ETWS test message (ID 4355)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:IDTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.CbsMessageSeverity)

	def set_id_type(self, type_py: enums.CbsMessageSeverity) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:IDTYpe \n
		Snippet: driver.configure.cbs.message.set_id_type(type_py = enums.CbsMessageSeverity.AAMBer) \n
		Specifies the severity of the CBS message ID as either decimal or hexadecimal number. \n
			:param type_py: UDEFined | APResidentia | AEXTreme | ASEVere | AAMBer | EARThquake | TSUNami | ETWarning | ETWTest UDEFined: user defined APResidentia: presidential level alerts (IDs 4370 and 4383) AEXTreme: extreme alerts (IDs 4371 to 4372 and 4384 to 4385) ASEVere: severe alerts (IDs 4373 to 4378 and 4386 to 4391) AAMBer: amber alerts (IDs 4379 and 4392) EARThquake: earthquake warning (ID 4352) TSUNami: tsunami warning (ID 4353) ETWarning: earthquake and tsunami warning (ID 4354) ETWTest: ETWS test message (ID 4355)
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.CbsMessageSeverity)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:IDTYpe {param}')

	# noinspection PyTypeChecker
	class SerialStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Geo_Scope: enums.GeoScope: CIMMediate | PLMN | SERVice | CNORmal The geographical area over which the message code is unique. CIMMediate: cell-wide, immediate display PLMN: PLMN wide SERVice: service area wide CNORmal: cell-wide, normal display
			- Message_Code: int: CB message identification Range: 0 to 1023
			- Auto_Incr: bool: OFF | ON OFF: no increase of UpdateNumber upon a CB message change ON: increase UpdateNumber automatically upon a CB message change
			- Update_Number: int: Indication of a content change of the same CB message Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Geo_Scope', enums.GeoScope),
			ArgStruct.scalar_int('Message_Code'),
			ArgStruct.scalar_bool('Auto_Incr'),
			ArgStruct.scalar_int('Update_Number')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Geo_Scope: enums.GeoScope = None
			self.Message_Code: int = None
			self.Auto_Incr: bool = None
			self.Update_Number: int = None

	# noinspection PyTypeChecker
	def get_serial(self) -> SerialStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: value: SerialStruct = driver.configure.cbs.message.get_serial() \n
		Specifies the unique CB message identification. \n
			:return: structure: for return value, see the help for SerialStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:SERial?', self.__class__.SerialStruct())

	def set_serial(self, value: SerialStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:SERial \n
		Snippet: driver.configure.cbs.message.set_serial(value = SerialStruct()) \n
		Specifies the unique CB message identification. \n
			:param value: see the help for SerialStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:SERial', value)

	def get_cgroup(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:CGRoup \n
		Snippet: value: int = driver.configure.cbs.message.get_cgroup() \n
		Queries the coding group to be indicated to the CB message recipient. The coding group is defined in 3GPP TS 23.
		038, section 5 as bits 4 to 7 of CBS data coding scheme. \n
			:return: coding_group: 0: used for internal messages ('Data Source' = 'Use Internal') 1: used for CBS files (only language = 1: UCS2 is supported) Range: 0 to 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:CGRoup?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_category(self) -> enums.Priority:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: value: enums.Priority = driver.configure.cbs.message.get_category() \n
		Indicates the privilege category of a CB message. \n
			:return: category: BACKground | NORMal | HIGH BACKground: to be broadcast, when no CB messages of category high priority or normal are broadcast NORMal: to be broadcast according to the associated repetition period HIGH: to be broadcast at the earliest opportunity
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.Priority)

	def set_category(self, category: enums.Priority) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:CATegory \n
		Snippet: driver.configure.cbs.message.set_category(category = enums.Priority.BACKground) \n
		Indicates the privilege category of a CB message. \n
			:param category: BACKground | NORMal | HIGH BACKground: to be broadcast, when no CB messages of category high priority or normal are broadcast NORMal: to be broadcast according to the associated repetition period HIGH: to be broadcast at the earliest opportunity
		"""
		param = Conversions.enum_scalar_to_str(category, enums.Priority)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:CATegory {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.MessageHandling:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: value: enums.MessageHandling = driver.configure.cbs.message.get_source() \n
		Specifies whether the CB message text is entered manually via method RsCmwWcdmaSig.Configure.Cbs.Message.
		data or an existing CBS file is used. The CBS file is selected via method RsCmwWcdmaSig.Configure.Cbs.Message.File.value. \n
			:return: message_handling: INTernal | FILE INTernal: content entered manually FILE: specified *.cbs file is used
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.MessageHandling)

	def set_source(self, message_handling: enums.MessageHandling) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:SOURce \n
		Snippet: driver.configure.cbs.message.set_source(message_handling = enums.MessageHandling.FILE) \n
		Specifies whether the CB message text is entered manually via method RsCmwWcdmaSig.Configure.Cbs.Message.
		data or an existing CBS file is used. The CBS file is selected via method RsCmwWcdmaSig.Configure.Cbs.Message.File.value. \n
			:param message_handling: INTernal | FILE INTernal: content entered manually FILE: specified *.cbs file is used
		"""
		param = Conversions.enum_scalar_to_str(message_handling, enums.MessageHandling)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:SOURce {param}')

	def get_data(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: value: str = driver.configure.cbs.message.get_data() \n
		Defines the CB message text. \n
			:return: data: Up to 1395 characters
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:DATA?')
		return trim_str_response(response)

	def set_data(self, data: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:DATA \n
		Snippet: driver.configure.cbs.message.set_data(data = '1') \n
		Defines the CB message text. \n
			:param data: Up to 1395 characters
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:DATA {param}')

	def get_period(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: value: float = driver.configure.cbs.message.get_period() \n
		Repetition period to broadcast the CB message again. \n
			:return: interval: Range: 1 s to 4096 s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, interval: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:PERiod \n
		Snippet: driver.configure.cbs.message.set_period(interval = 1.0) \n
		Repetition period to broadcast the CB message again. \n
			:param interval: Range: 1 s to 4096 s
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:PERiod {param}')

	def clone(self) -> 'Message':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Message(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
