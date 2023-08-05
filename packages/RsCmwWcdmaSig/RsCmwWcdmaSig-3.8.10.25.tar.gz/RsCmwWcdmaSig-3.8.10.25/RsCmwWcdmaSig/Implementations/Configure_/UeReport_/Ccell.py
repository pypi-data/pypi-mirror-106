from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccell:
	"""Ccell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ccell", core, parent)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cpi_Ch_Rscp: bool: OFF | ON
			- Cpi_Ch_Ec_Io: bool: OFF | ON
			- Tch_Bler: bool: OFF | ON
			- Tx_Power: bool: OFF | ON
			- Rx_Tx_Time_Diff: bool: OFF | ON
			- Pathloss: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Cpi_Ch_Rscp'),
			ArgStruct.scalar_bool('Cpi_Ch_Ec_Io'),
			ArgStruct.scalar_bool('Tch_Bler'),
			ArgStruct.scalar_bool('Tx_Power'),
			ArgStruct.scalar_bool('Rx_Tx_Time_Diff'),
			ArgStruct.scalar_bool('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cpi_Ch_Rscp: bool = None
			self.Cpi_Ch_Ec_Io: bool = None
			self.Tch_Bler: bool = None
			self.Tx_Power: bool = None
			self.Rx_Tx_Time_Diff: bool = None
			self.Pathloss: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:CCELl:ENABle \n
		Snippet: value: EnableStruct = driver.configure.ueReport.ccell.get_enable() \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message for the current cell. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:CCELl:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:CCELl:ENABle \n
		Snippet: driver.configure.ueReport.ccell.set_enable(value = EnableStruct()) \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message for the current cell. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:CCELl:ENABle', value)
