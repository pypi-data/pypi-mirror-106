from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gsm:
	"""Gsm commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gsm", core, parent)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rssi: bool: OFF | ON
			- Bsic: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Rssi'),
			ArgStruct.scalar_bool('Bsic')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rssi: bool = None
			self.Bsic: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:GSM:ENABle \n
		Snippet: value: EnableStruct = driver.configure.ueReport.ncell.gsm.get_enable() \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message related to GSM neighbor cell. BSIC measurement requires activated RSSI measurement. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:GSM:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:GSM:ENABle \n
		Snippet: driver.configure.ueReport.ncell.gsm.set_enable(value = EnableStruct()) \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message related to GSM neighbor cell. BSIC measurement requires activated RSSI measurement. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:GSM:ENABle', value)
