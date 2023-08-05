from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 6 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pattern", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Pattern_.Execute import Execute
			self._execute = Execute(self._core, self._base)
		return self._execute

	def get_length(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:LENGth \n
		Snippet: value: int = driver.configure.cell.carrier.hsupa.eagch.pattern.get_length() \n
		Specifies the length of the absolute grant pattern. \n
			:return: length: Range: 1 to 8 (for 10 ms TTI: 1 to 4)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:LENGth \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.set_length(length = 1) \n
		Specifies the length of the absolute grant pattern. \n
			:param length: Range: 1 to 8 (for 10 ms TTI: 1 to 4)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:LENGth {param}')

	def get_index(self) -> List[int or bool]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:INDex \n
		Snippet: value: List[int or bool] = driver.configure.cell.carrier.hsupa.eagch.pattern.get_index() \n
		Specifies the absolute grant indices of the absolute grant pattern. A query returns all eight defined indices. A setting
		configures the first n indices (n = 1 to 8) . Only the first m indices are considered for transmission, with m specified
		via method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:return: index: Comma-separated list of up to eight values Range: 0 to 31 Additional OFF | ON disables | enables the transmission of index value, OFF results in an unscheduled TTI
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:INDex?')
		return Conversions.str_to_int_or_bool_list(response)

	def set_index(self, index: List[int or bool]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:INDex \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.set_index(index = [1, True, 2, False, 3]) \n
		Specifies the absolute grant indices of the absolute grant pattern. A query returns all eight defined indices. A setting
		configures the first n indices (n = 1 to 8) . Only the first m indices are considered for transmission, with m specified
		via method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:param index: Comma-separated list of up to eight values Range: 0 to 31 Additional OFF | ON disables | enables the transmission of index value, OFF results in an unscheduled TTI
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.list_to_csv_str(index)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:INDex {param}')

	def get_scope(self) -> List[bool]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:SCOPe \n
		Snippet: value: List[bool] = driver.configure.cell.carrier.hsupa.eagch.pattern.get_scope() \n
		Specifies the absolute grant scopes of the absolute grant pattern. A query returns all eight defined scopes. A setting
		configures the first n scopes (n = 1 to 8) . Only the first m scopes are considered for transmission, with m specified
		via method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:return: scope: OFF | ON Comma-separated list of up to eight values OFF: absolute grant applies to all HARQ processes ON: absolute grant applies to one HARQ process only
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:SCOPe?')
		return Conversions.str_to_bool_list(response)

	def set_scope(self, scope: List[bool]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:SCOPe \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.set_scope(scope = [True, False, True]) \n
		Specifies the absolute grant scopes of the absolute grant pattern. A query returns all eight defined scopes. A setting
		configures the first n scopes (n = 1 to 8) . Only the first m scopes are considered for transmission, with m specified
		via method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:param scope: OFF | ON Comma-separated list of up to eight values OFF: absolute grant applies to all HARQ processes ON: absolute grant applies to one HARQ process only
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.list_to_csv_str(scope)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:SCOPe {param}')

	def get_type_py(self) -> List[bool]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:TYPE \n
		Snippet: value: List[bool] = driver.configure.cell.carrier.hsupa.eagch.pattern.get_type_py() \n
		Specifies the ID types of the absolute grant pattern. A query returns all eight defined types. A setting configures the
		first n types (n = 1 to 8) . Only the first m types are considered for transmission, with m specified via method
		RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:return: type_py: OFF | ON Comma-separated list of up to eight values OFF: use primary UE-ID ON: use secondary UE-ID
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:TYPE?')
		return Conversions.str_to_bool_list(response)

	def set_type_py(self, type_py: List[bool]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:TYPE \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.set_type_py(type_py = [True, False, True]) \n
		Specifies the ID types of the absolute grant pattern. A query returns all eight defined types. A setting configures the
		first n types (n = 1 to 8) . Only the first m types are considered for transmission, with m specified via method
		RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Eagch.Pattern.length. \n
			:param type_py: OFF | ON Comma-separated list of up to eight values OFF: use primary UE-ID ON: use secondary UE-ID
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.list_to_csv_str(type_py)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:TYPE {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepetitionB:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:REPetition \n
		Snippet: value: enums.RepetitionB = driver.configure.cell.carrier.hsupa.eagch.pattern.get_repetition() \n
		Specifies whether the absolute grant pattern has to be transmitted only once, continuously or serving grant (SG)
		initialized. Select 'SG Initialized' only for E-RGCH measurements. \n
			:return: repetition: ONCE | CONTinuous | SGINit
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepetitionB)

	def set_repetition(self, repetition: enums.RepetitionB) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:REPetition \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.set_repetition(repetition = enums.RepetitionB.CONTinuous) \n
		Specifies whether the absolute grant pattern has to be transmitted only once, continuously or serving grant (SG)
		initialized. Select 'SG Initialized' only for E-RGCH measurements. \n
			:param repetition: ONCE | CONTinuous | SGINit
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepetitionB)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:REPetition {param}')

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
