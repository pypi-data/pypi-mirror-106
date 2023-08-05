from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ergch:
	"""Ergch commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ergch", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_pattern'):
			from .Ergch_.Pattern import Pattern
			self._pattern = Pattern(self._core, self._base)
		return self._pattern

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ErgchIndicatorMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:MODE \n
		Snippet: value: enums.ErgchIndicatorMode = driver.configure.cell.carrier.hsupa.ergch.get_mode() \n
		Specifies the relative grant sequence transmitted via the E-RGCH. For definition of a user-defined pattern, see method
		RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Ergch.Pattern.value. \n
			:return: mode: ALTernating | HARQ | UP | DOWN | DTX | CONTinuous | SINGle ALTernating: alternating UP, DOWN - per TTI HARQ: alternating UP, DOWN - per HARQ cycle UP: all UP DOWN: all DOWN DTX: all DTX CONTinuous: continuous user-defined pattern SINGle: single user-defined pattern
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ErgchIndicatorMode)

	def set_mode(self, mode: enums.ErgchIndicatorMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:MODE \n
		Snippet: driver.configure.cell.carrier.hsupa.ergch.set_mode(mode = enums.ErgchIndicatorMode.ALTernating) \n
		Specifies the relative grant sequence transmitted via the E-RGCH. For definition of a user-defined pattern, see method
		RsCmwWcdmaSig.Configure.Cell.Carrier.Hsupa.Ergch.Pattern.value. \n
			:param mode: ALTernating | HARQ | UP | DOWN | DTX | CONTinuous | SINGle ALTernating: alternating UP, DOWN - per TTI HARQ: alternating UP, DOWN - per HARQ cycle UP: all UP DOWN: all DOWN DTX: all DTX CONTinuous: continuous user-defined pattern SINGle: single user-defined pattern
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(mode, enums.ErgchIndicatorMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:MODE {param}')

	def get_signature(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:SIGNature \n
		Snippet: value: int = driver.configure.cell.carrier.hsupa.ergch.get_signature() \n
		Specifies the E-RGCH signature. \n
			:return: signature: Range: 0 to 39
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:SIGNature?')
		return Conversions.str_to_int(response)

	def set_signature(self, signature: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ERGCh:SIGNature \n
		Snippet: driver.configure.cell.carrier.hsupa.ergch.set_signature(signature = 1) \n
		Specifies the E-RGCH signature. \n
			:param signature: Range: 0 to 39
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(signature)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ERGCh:SIGNature {param}')

	def clone(self) -> 'Ergch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ergch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
