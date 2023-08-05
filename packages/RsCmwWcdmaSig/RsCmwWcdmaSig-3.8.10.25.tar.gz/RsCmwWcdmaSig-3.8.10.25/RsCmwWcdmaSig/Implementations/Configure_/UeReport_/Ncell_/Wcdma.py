from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wcdma:
	"""Wcdma commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("wcdma", core, parent)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rscp: bool: OFF | ON
			- Ecn_0: bool: OFF | ON
			- Rssi: bool: OFF | ON
			- Sfn_Cfn: bool: OFF | ON
			- Pathloss: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Rscp'),
			ArgStruct.scalar_bool('Ecn_0'),
			ArgStruct.scalar_bool('Rssi'),
			ArgStruct.scalar_bool('Sfn_Cfn'),
			ArgStruct.scalar_bool('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rscp: bool = None
			self.Ecn_0: bool = None
			self.Rssi: bool = None
			self.Sfn_Cfn: bool = None
			self.Pathloss: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:WCDMa:ENABle \n
		Snippet: value: EnableStruct = driver.configure.ueReport.ncell.wcdma.get_enable() \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message related to WCDMA neighbor cell. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:WCDMa:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:WCDMa:ENABle \n
		Snippet: driver.configure.ueReport.ncell.wcdma.set_enable(value = EnableStruct()) \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message related to WCDMA neighbor cell. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:WCDMa:ENABle', value)
