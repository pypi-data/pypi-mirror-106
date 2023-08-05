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
			- Band: enums.LteBand: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB15 | OB16 | OB17 | OB18 | OB19 | OB20 | OB21 | OB22 | OB23 | OB24 | OB25 | OB26 | OB27 | OB28 | OB29 | OB30 | OB31 | OB32 | OB33 | OB34 | OB35 | OB36 | OB37 | OB38 | OB39 | OB40 | OB41 | OB42 | OB43 | OB44 | OB45 | OB46 | OB65 | OB66 | OB67 | OB252 | OB255 Operating band 1 to 46, 65 to 67, 252, 255
			- Channel: int: Downlink channel number Range: depends on operating band, see tables below
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the UE measurement"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.LteBand),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_bool('Measurement')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.LteBand = None
			self.Channel: int = None
			self.Measurement: bool = None

	def set(self, structure: CellStruct, cell=repcap.Cell.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:LTE:CELL<n> \n
		Snippet: driver.configure.ncell.lte.cell.set(value = [PROPERTY_STRUCT_NAME](), cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for LTE. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')"""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:LTE:CELL{cell_cmd_val}', structure)

	def get(self, cell=repcap.Cell.Default) -> CellStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:LTE:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.lte.cell.get(cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for LTE. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:LTE:CELL{cell_cmd_val}?', self.__class__.CellStruct())
