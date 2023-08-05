from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmode:
	"""Cmode commands group definition. 7 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmode", core, parent)

	@property
	def ulcm(self):
		"""ulcm commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulcm'):
			from .Cmode_.Ulcm import Ulcm
			self._ulcm = Ulcm(self._core, self._base)
		return self._ulcm

	@property
	def single(self):
		"""single commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_single'):
			from .Cmode_.Single import Single
			self._single = Single(self._core, self._base)
		return self._single

	@property
	def ueReport(self):
		"""ueReport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ueReport'):
			from .Cmode_.UeReport import UeReport
			self._ueReport = UeReport(self._core, self._base)
		return self._ueReport

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.CmodePatternSelection:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:PATTern \n
		Snippet: value: enums.CmodePatternSelection = driver.configure.cmode.get_pattern() \n
		Selects the transmission gap patterns for compressed mode. \n
			:return: selection: NONE | UEReport | SINGle | ULCM NONE: compressed mode disabled UEReport: several patterns for different measurement purposes used in parallel See method RsCmwWcdmaSig.Configure.Cmode.UeReport.enable SINGle: selectable pattern for a definite measurement purpose See method RsCmwWcdmaSig.Configure.Cmode.Single.typePy ULCM: selectable pattern for the UL compressed mode TX test See method RsCmwWcdmaSig.Configure.Cmode.Ulcm.typePy
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.CmodePatternSelection)

	def set_pattern(self, selection: enums.CmodePatternSelection) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:PATTern \n
		Snippet: driver.configure.cmode.set_pattern(selection = enums.CmodePatternSelection.NONE) \n
		Selects the transmission gap patterns for compressed mode. \n
			:param selection: NONE | UEReport | SINGle | ULCM NONE: compressed mode disabled UEReport: several patterns for different measurement purposes used in parallel See method RsCmwWcdmaSig.Configure.Cmode.UeReport.enable SINGle: selectable pattern for a definite measurement purpose See method RsCmwWcdmaSig.Configure.Cmode.Single.typePy ULCM: selectable pattern for the UL compressed mode TX test See method RsCmwWcdmaSig.Configure.Cmode.Ulcm.typePy
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.CmodePatternSelection)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:PATTern {param}')

	def clone(self) -> 'Cmode':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmode(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
