from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 33 total commands, 10 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scell'):
			from .Scenario_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcarrier'):
			from .Scenario_.Dcarrier import Dcarrier
			self._dcarrier = Dcarrier(self._core, self._base)
		return self._dcarrier

	@property
	def scFading(self):
		"""scFading commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scFading'):
			from .Scenario_.ScFading import ScFading
			self._scFading = ScFading(self._core, self._base)
		return self._scFading

	@property
	def scfDiversity(self):
		"""scfDiversity commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scfDiversity'):
			from .Scenario_.ScfDiversity import ScfDiversity
			self._scfDiversity = ScfDiversity(self._core, self._base)
		return self._scfDiversity

	@property
	def dcFading(self):
		"""dcFading commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcFading'):
			from .Scenario_.DcFading import DcFading
			self._dcFading = DcFading(self._core, self._base)
		return self._dcFading

	@property
	def dcfDiversity(self):
		"""dcfDiversity commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dcfDiversity'):
			from .Scenario_.DcfDiversity import DcfDiversity
			self._dcfDiversity = DcfDiversity(self._core, self._base)
		return self._dcfDiversity

	@property
	def dbFading(self):
		"""dbFading commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dbFading'):
			from .Scenario_.DbFading import DbFading
			self._dbFading = DbFading(self._core, self._base)
		return self._dbFading

	@property
	def dbfDiversity(self):
		"""dbfDiversity commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dbfDiversity'):
			from .Scenario_.DbfDiversity import DbfDiversity
			self._dbfDiversity = DbfDiversity(self._core, self._base)
		return self._dbfDiversity

	@property
	def dchspa(self):
		"""dchspa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dchspa'):
			from .Scenario_.Dchspa import Dchspa
			self._dchspa = Dchspa(self._core, self._base)
		return self._dchspa

	@property
	def tchspa(self):
		"""tchspa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tchspa'):
			from .Scenario_.Tchspa import Tchspa
			self._tchspa = Tchspa(self._core, self._base)
		return self._tchspa

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SCELl | DCARrier | SCFading | DCFading | SCFDiversity | DCFDiversity | DBFading | DBFDiversity | DCHSpa | TCHSpa SCEL: 'Standard Cell' DCARrier: 'Dual Carrier' SCFading: 'Standard Cell Fading' DCFading: 'Dual Carrier Fading' SCFDiversity:'Standard Cell RX Diversity Fading' DCFDiversity: 'Dual Carrier RX Diversity Fading' DBFading: 'Dual Carrier / Dual Band Fading' DBFDiversity: 'Dual Carrier / Dual Band RX Diversity Fading' DCHSpa: 'Dual Carrier HSPA' TCHSpa: '3C HSPA'
			- Fader: enums.SourceInt: EXTernal | INTernal Only returned for internal fading scenarios, e.g. SCF, DCF Indicates whether internal or external fading is active."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_enum('Fader', enums.SourceInt)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Fader: enums.SourceInt = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:WCDMa:SIGNaling<instance>:SCENario \n
		Snippet: value: ValueStruct = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:WCDMa:SIGNaling<Instance>:SCENario?', self.__class__.ValueStruct())

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
