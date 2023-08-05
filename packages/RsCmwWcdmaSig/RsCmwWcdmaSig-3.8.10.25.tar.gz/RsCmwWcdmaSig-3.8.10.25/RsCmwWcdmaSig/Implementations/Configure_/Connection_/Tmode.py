from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmode:
	"""Tmode commands group definition. 15 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tmode", core, parent)

	@property
	def btfd(self):
		"""btfd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btfd'):
			from .Tmode_.Btfd import Btfd
			self._btfd = Btfd(self._core, self._base)
		return self._btfd

	@property
	def rmc(self):
		"""rmc commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_rmc'):
			from .Tmode_.Rmc import Rmc
			self._rmc = Rmc(self._core, self._base)
		return self._rmc

	@property
	def hspa(self):
		"""hspa commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_hspa'):
			from .Tmode_.Hspa import Hspa
			self._hspa = Hspa(self._core, self._base)
		return self._hspa

	def get_ktlre_config(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:KTLReconfig \n
		Snippet: value: bool = driver.configure.connection.tmode.get_ktlre_config() \n
		Specifies whether the test loop is kept closed when the operating band or the carrier frequency is reconfigured during an
		established test mode connection with test loop. \n
			:return: enable: OFF | ON ON: keep test loop closed OFF: open test loop, perform reconfiguration, close test loop
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:KTLReconfig?')
		return Conversions.str_to_bool(response)

	def set_ktlre_config(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:KTLReconfig \n
		Snippet: driver.configure.connection.tmode.set_ktlre_config(enable = False) \n
		Specifies whether the test loop is kept closed when the operating band or the carrier frequency is reconfigured during an
		established test mode connection with test loop. \n
			:param enable: OFF | ON ON: keep test loop closed OFF: open test loop, perform reconfiguration, close test loop
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:KTLReconfig {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.TestModeType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:TYPE \n
		Snippet: value: enums.TestModeType = driver.configure.connection.tmode.get_type_py() \n
		Selects the test mode connection type. \n
			:return: type_py: RMC | HSPA | RHSPa | FACH | BTFD RMC: RMC in CS or PS domain HSPA: HSPA in PS domain RHSPa: RMC plus HSPA FACH: test using CELL_FACH state in CS domain BTFD: test using blind transport format detection
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TestModeType)

	def set_type_py(self, type_py: enums.TestModeType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:TYPE \n
		Snippet: driver.configure.connection.tmode.set_type_py(type_py = enums.TestModeType.BTFD) \n
		Selects the test mode connection type. \n
			:param type_py: RMC | HSPA | RHSPa | FACH | BTFD RMC: RMC in CS or PS domain HSPA: HSPA in PS domain RHSPa: RMC plus HSPA FACH: test using CELL_FACH state in CS domain BTFD: test using blind transport format detection
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TestModeType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:TYPE {param}')

	def clone(self) -> 'Tmode':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tmode(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
