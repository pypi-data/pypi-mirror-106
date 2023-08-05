from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpedch:
	"""Mpedch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mpedch", core, parent)

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Current_Etfci_1: float: Monitored 'Current E-TFCI' value of the carrier one Range: 0 to 127
			- Target_Etfci_1: float: Calculated 'Target E-TFCI' value of the carrier one Range: 0 to 127
			- Current_Etfci_2: float: Monitored 'Current E-TFCI' value of the carrier two Range: 0 to 127
			- Target_Etfci_2: float: Calculated 'Target E-TFCI' value of the carrier two Range: 0 to 127"""
		__meta_args_list = [
			ArgStruct.scalar_float('Current_Etfci_1'),
			ArgStruct.scalar_float('Target_Etfci_1'),
			ArgStruct.scalar_float('Current_Etfci_2'),
			ArgStruct.scalar_float('Target_Etfci_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Current_Etfci_1: float = None
			self.Target_Etfci_1: float = None
			self.Current_Etfci_2: float = None
			self.Target_Etfci_2: float = None

	def get_state(self) -> StateStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:MPEDch:STATe \n
		Snippet: value: StateStruct = driver.configure.uplink.tpc.mpedch.get_state() \n
		Queries the E-TFCI information for the TPC setup 'Max. Power E-DCH'. \n
			:return: structure: for return value, see the help for StateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:MPEDch:STATe?', self.__class__.StateStruct())
