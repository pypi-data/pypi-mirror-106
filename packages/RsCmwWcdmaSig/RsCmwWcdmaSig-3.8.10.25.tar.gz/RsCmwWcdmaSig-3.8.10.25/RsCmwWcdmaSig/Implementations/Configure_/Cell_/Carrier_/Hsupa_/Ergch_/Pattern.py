from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

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
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:PATTern:LENGth \n
		Snippet: value: int = driver.configure.cell.carrier.hsupa.ergch.pattern.get_length() \n
		Specifies the length of the user-defined relative grant pattern. \n
			:return: length: Range: 1 to 8 (for 10 ms TTI: 1 to 4)
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:PATTern:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:PATTern:LENGth \n
		Snippet: driver.configure.cell.carrier.hsupa.ergch.pattern.set_length(length = 1) \n
		Specifies the length of the user-defined relative grant pattern. \n
			:param length: Range: 1 to 8 (for 10 ms TTI: 1 to 4)
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:PATTern:LENGth {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:PATTern \n
		Snippet: value: str = driver.configure.cell.carrier.hsupa.ergch.pattern.get_value() \n
		Specifies the bits of the user-defined relative grant pattern. Bits exceeding the configured pattern length are ignored,
		see method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Ergch.Pattern.length. \n
			:return: pattern: String containing exactly 8 bits 0 = DOWN, 1 = UP, - = DTX
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:PATTern?')
		return trim_str_response(response)

	def set_value(self, pattern: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:PATTern \n
		Snippet: driver.configure.cell.carrier.hsupa.ergch.pattern.set_value(pattern = '1') \n
		Specifies the bits of the user-defined relative grant pattern. Bits exceeding the configured pattern length are ignored,
		see method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Ergch.Pattern.length. \n
			:param pattern: String containing exactly 8 bits 0 = DOWN, 1 = UP, - = DTX
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.value_to_quoted_str(pattern)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:PATTern {param}')

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
