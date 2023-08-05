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
			- Band: enums.GsmBand: G04 | G085 | G09 | G18 | G19 GSM 400, GSM 850, GSM 900, GSM 1800, GSM 1900
			- Channel: int: Channel number used for the broadcast control channel (BCCH) Range: 0 to 1023, depending on GSM band, see table below
			- Measurement: bool: Optional setting parameter. OFF | ON Enables or disables the UE measurement
			- Bsic: int: Optional setting parameter. Base station identity code Range: 0 to 63"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Band', enums.GsmBand),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_bool('Measurement'),
			ArgStruct.scalar_int('Bsic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Band: enums.GsmBand = None
			self.Channel: int = None
			self.Measurement: bool = None
			self.Bsic: int = None

	def set(self, structure: CellStruct, cell=repcap.Cell.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:GSM:CELL<n> \n
		Snippet: driver.configure.ncell.gsm.cell.set(value = [PROPERTY_STRUCT_NAME](), cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for GSM. \n
			:param structure: for set value, see the help for CellStruct structure arguments.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')"""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:GSM:CELL{cell_cmd_val}', structure)

	def get(self, cell=repcap.Cell.Default) -> CellStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:NCELl:GSM:CELL<n> \n
		Snippet: value: CellStruct = driver.configure.ncell.gsm.cell.get(cell = repcap.Cell.Default) \n
		Configures an entry of the neighbor cell list for GSM. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		cell_cmd_val = self._base.get_repcap_cmd_value(cell, repcap.Cell)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:NCELl:GSM:CELL{cell_cmd_val}?', self.__class__.CellStruct())
