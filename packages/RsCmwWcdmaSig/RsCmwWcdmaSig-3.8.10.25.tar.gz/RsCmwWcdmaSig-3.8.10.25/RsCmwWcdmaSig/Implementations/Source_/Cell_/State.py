from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Main_State: enums.GeneratorState: OFF | ON | RFHandover OFF: generator switched off ON: generator has been turned on RFHandover: ready to receive a handover from another signaling application
			- Sync_State: enums.SyncState: PENDing | ADJusted PENDing: the generator has been turned on (off) but the signal is not yet (still) available ADJusted: the physical output signal corresponds to the main generator state (signal off for main state OFF, signal on for main state ON)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Main_State', enums.GeneratorState),
			ArgStruct.scalar_enum('Sync_State', enums.SyncState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: enums.GeneratorState = None
			self.Sync_State: enums.SyncState = None

	# noinspection PyTypeChecker
	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:WCDMa:SIGNaling<instance>:CELL:STATe:ALL \n
		Snippet: value: AllStruct = driver.source.cell.state.get_all() \n
		Returns detailed information about the 'WCDMA Signaling' generator state. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:WCDMa:SIGNaling<Instance>:CELL:STATe:ALL?', self.__class__.AllStruct())

	def get_value(self) -> bool:
		"""SCPI: SOURce:WCDMa:SIGNaling<instance>:CELL:STATe \n
		Snippet: value: bool = driver.source.cell.state.get_value() \n
		Turns the generator (the cell) on or off. \n
			:return: main_state: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:WCDMa:SIGNaling<Instance>:CELL:STATe?')
		return Conversions.str_to_bool(response)

	def set_value(self, main_state: bool) -> None:
		"""SCPI: SOURce:WCDMa:SIGNaling<instance>:CELL:STATe \n
		Snippet: driver.source.cell.state.set_value(main_state = False) \n
		Turns the generator (the cell) on or off. \n
			:param main_state: No help available
		"""
		param = Conversions.bool_to_str(main_state)
		self._core.io.write_with_opc(f'SOURce:WCDMa:SIGNaling<Instance>:CELL:STATe {param}')
