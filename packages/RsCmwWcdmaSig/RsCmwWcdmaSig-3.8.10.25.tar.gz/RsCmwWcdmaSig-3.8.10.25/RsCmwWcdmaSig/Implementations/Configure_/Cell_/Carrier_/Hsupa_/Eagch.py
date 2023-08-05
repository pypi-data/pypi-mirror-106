from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eagch:
	"""Eagch commands group definition. 7 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eagch", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_pattern'):
			from .Eagch_.Pattern import Pattern
			self._pattern = Pattern(self._core, self._base)
		return self._pattern

	# noinspection PyTypeChecker
	class UeIdStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Primary: float: Range: #H0 to #HFFFF
			- Secondary: float: Range: #H0 to #HFFFF"""
		__meta_args_list = [
			ArgStruct.scalar_float('Primary'),
			ArgStruct.scalar_float('Secondary')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Primary: float = None
			self.Secondary: float = None

	def get_ue_id(self) -> UeIdStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:UEID \n
		Snippet: value: UeIdStruct = driver.configure.cell.carrier.hsupa.eagch.get_ue_id() \n
		Specifies the primary [and secondary] E-RNTI of the UE. \n
			:return: structure: for return value, see the help for UeIdStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:UEID?', self.__class__.UeIdStruct())

	def set_ue_id(self, value: UeIdStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:UEID \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.set_ue_id(value = UeIdStruct()) \n
		Specifies the primary [and secondary] E-RNTI of the UE. \n
			:param value: see the help for UeIdStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:UEID', value)

	def clone(self) -> 'Eagch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eagch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
