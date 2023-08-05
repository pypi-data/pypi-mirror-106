from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncell:
	"""Ncell commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ncell", core, parent)

	@property
	def gsm(self):
		"""gsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gsm'):
			from .Ncell_.Gsm import Gsm
			self._gsm = Gsm(self._core, self._base)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wcdma'):
			from .Ncell_.Wcdma import Wcdma
			self._wcdma = Wcdma(self._core, self._base)
		return self._wcdma

	@property
	def lte(self):
		"""lte commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lte'):
			from .Ncell_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cpi_Ch_Rscp: bool: OFF | ON
			- Cpi_Ch_Ec_Io: bool: OFF | ON
			- Rssi: bool: OFF | ON
			- Sfn_Cfn_Time_Diff: bool: OFF | ON
			- Pathloss: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Cpi_Ch_Rscp'),
			ArgStruct.scalar_bool('Cpi_Ch_Ec_Io'),
			ArgStruct.scalar_bool('Rssi'),
			ArgStruct.scalar_bool('Sfn_Cfn_Time_Diff'),
			ArgStruct.scalar_bool('Pathloss')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cpi_Ch_Rscp: bool = None
			self.Cpi_Ch_Ec_Io: bool = None
			self.Rssi: bool = None
			self.Sfn_Cfn_Time_Diff: bool = None
			self.Pathloss: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:ENABle \n
		Snippet: value: EnableStruct = driver.configure.ueReport.ncell.get_enable() \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message for carrier 2. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UEReport:NCELl:ENABle \n
		Snippet: driver.configure.ueReport.ncell.set_enable(value = EnableStruct()) \n
		Enables or disables the evaluation and display of the individual information elements included in the UE measurement
		report message for carrier 2. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UEReport:NCELl:ENABle', value)

	def clone(self) -> 'Ncell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ncell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
