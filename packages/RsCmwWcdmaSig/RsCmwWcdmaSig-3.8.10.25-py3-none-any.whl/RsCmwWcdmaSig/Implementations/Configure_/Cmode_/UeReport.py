from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReport:
	"""UeReport commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueReport", core, parent)

	# noinspection PyTypeChecker
	class ActivationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fdd: enums.CmodeActivation: RAB | MEASurement
			- Gsm_Rssi: enums.CmodeActivation: RAB | MEASurement
			- Gsm_Bsic: enums.CmodeActivation: RAB | MEASurement
			- Gsm_Bsic_Reconf: enums.CmodeActivation: RAB | MEASurement
			- Eutra: enums.CmodeActivation: RAB | MEASurement"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Fdd', enums.CmodeActivation),
			ArgStruct.scalar_enum('Gsm_Rssi', enums.CmodeActivation),
			ArgStruct.scalar_enum('Gsm_Bsic', enums.CmodeActivation),
			ArgStruct.scalar_enum('Gsm_Bsic_Reconf', enums.CmodeActivation),
			ArgStruct.scalar_enum('Eutra', enums.CmodeActivation)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fdd: enums.CmodeActivation = None
			self.Gsm_Rssi: enums.CmodeActivation = None
			self.Gsm_Bsic: enums.CmodeActivation = None
			self.Gsm_Bsic_Reconf: enums.CmodeActivation = None
			self.Eutra: enums.CmodeActivation = None

	# noinspection PyTypeChecker
	def get_activation(self) -> ActivationStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:UEReport:ACTivation \n
		Snippet: value: ActivationStruct = driver.configure.cmode.ueReport.get_activation() \n
		Selects whether the compressed mode pattern has to be activated for the whole duration of the connection (RAB setup) or
		for the duration of a specified UE report measurement only. \n
			:return: structure: for return value, see the help for ActivationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:UEReport:ACTivation?', self.__class__.ActivationStruct())

	def set_activation(self, value: ActivationStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:UEReport:ACTivation \n
		Snippet: driver.configure.cmode.ueReport.set_activation(value = ActivationStruct()) \n
		Selects whether the compressed mode pattern has to be activated for the whole duration of the connection (RAB setup) or
		for the duration of a specified UE report measurement only. \n
			:param value: see the help for ActivationStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:UEReport:ACTivation', value)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fdd: bool: OFF | ON
			- Gsm_Rssi: bool: OFF | ON
			- Gsm_Bsic: bool: OFF | ON
			- Gsm_Bsic_Reconf: bool: OFF | ON
			- Eutra: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Fdd'),
			ArgStruct.scalar_bool('Gsm_Rssi'),
			ArgStruct.scalar_bool('Gsm_Bsic'),
			ArgStruct.scalar_bool('Gsm_Bsic_Reconf'),
			ArgStruct.scalar_bool('Eutra')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fdd: bool = None
			self.Gsm_Rssi: bool = None
			self.Gsm_Bsic: bool = None
			self.Gsm_Bsic_Reconf: bool = None
			self.Eutra: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:UEReport:ENABle \n
		Snippet: value: EnableStruct = driver.configure.cmode.ueReport.get_enable() \n
		Enables the transmission gap patterns for different measurement purposes. All selected patterns are used in parallel. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:UEReport:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:UEReport:ENABle \n
		Snippet: driver.configure.cmode.ueReport.set_enable(value = EnableStruct()) \n
		Enables the transmission gap patterns for different measurement purposes. All selected patterns are used in parallel. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:UEReport:ENABle', value)
