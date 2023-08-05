from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable: bool: OFF | ON Enables or disables the entry
			- Band: enums.OperationBand: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OBS1 | ... | OBS3 | OBL1 OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OB32: operating band XXXII (restricted to dual band scenarios) OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L
			- Channel: int: Downlink channel number Range: depends on operating band
			- Scrambling_Code: str: Primary scrambling code Range: #H0 to #H1FF
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the UE measurement"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.OperationBand),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_raw_str('Scrambling_Code'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.OperationBand = None
			self.Channel: int = None
			self.Scrambling_Code: str = None
			self.Measurement: bool = None

	def set(self, structure: CellStruct, cell=repcap.Cell.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:WCDMa:CELL<n> \n
		Snippet: driver.configure.ncell.wcdma.cell.set(value = [PROPERTY_STRUCT_NAME](), cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for WCDMA. For channel number ranges depending on operating bands see
		'Operating Bands'. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')"""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:WCDMa:CELL{cell_cmd_val}', structure)

	def get(self, cell=repcap.Cell.Default) -> CellStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:WCDMa:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.wcdma.cell.get(cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for WCDMA. For channel number ranges depending on operating bands see
		'Operating Bands'. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:WCDMa:CELL{cell_cmd_val}?', self.__class__.CellStruct())
