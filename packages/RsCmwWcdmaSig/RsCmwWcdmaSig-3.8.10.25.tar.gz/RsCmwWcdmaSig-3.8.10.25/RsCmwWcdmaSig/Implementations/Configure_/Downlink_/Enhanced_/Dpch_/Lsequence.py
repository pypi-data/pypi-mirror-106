from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lsequence:
	"""Lsequence commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lsequence", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Lsequence_.Execute import Execute
			self._execute = Execute(self._core, self._base)
		return self._execute

	# noinspection PyTypeChecker
	def get_state(self) -> enums.LevelSeqState:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:LSEQuence:STATe \n
		Snippet: value: enums.LevelSeqState = driver.configure.downlink.enhanced.dpch.lsequence.get_state() \n
		Queries the generator status of DPCH level transitions for 'WCDMA Out-Of-Sync Handling Measurement'. \n
			:return: state: IDLE | RUNNing | FAILed | SCONflict | SCHanged IDLE: test procedure has not started yet RUNNing: test procedure is in progress without errors FAILed: test procedure failed SCONflict: settings are inappropriate for the setup SCHanged: relevant settings changed after setup execution
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:LSEQuence:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.LevelSeqState)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Ab: float: Range: -80 dB to 0 dB
			- Bd: float: Range: -80 dB to 0 dB
			- De: float: Range: -80 dB to 0 dB
			- Ef: float: Range: -80 dB to 0 dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ab'),
			ArgStruct.scalar_float('Bd'),
			ArgStruct.scalar_float('De'),
			ArgStruct.scalar_float('Ef')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ab: float = None
			self.Bd: float = None
			self.De: float = None
			self.Ef: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:LSEQuence \n
		Snippet: value: ValueStruct = driver.configure.downlink.enhanced.dpch.lsequence.get_value() \n
		Specifies the level of out-of-sync power mask between the areas A to F. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:LSEQuence?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:LSEQuence \n
		Snippet: driver.configure.downlink.enhanced.dpch.lsequence.set_value(value = ValueStruct()) \n
		Specifies the level of out-of-sync power mask between the areas A to F. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:LSEQuence', value)

	def clone(self) -> 'Lsequence':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lsequence(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
