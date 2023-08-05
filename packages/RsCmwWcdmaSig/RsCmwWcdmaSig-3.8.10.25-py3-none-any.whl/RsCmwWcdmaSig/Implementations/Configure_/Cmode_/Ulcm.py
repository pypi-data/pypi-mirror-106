from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulcm:
	"""Ulcm commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ulcm", core, parent)

	@property
	def activation(self):
		"""activation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_activation'):
			from .Ulcm_.Activation import Activation
			self._activation = Activation(self._core, self._base)
		return self._activation

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.TransGapType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:ULCM:TYPE \n
		Snippet: value: enums.TransGapType = driver.configure.cmode.ulcm.get_type_py() \n
		Selects the transmission gap patterns for the UL compressed mode TX test. \n
			:return: type_py: AR | AF | B AR: pattern A (rising TPC) defined in 3GPP TS 34.121, table 5.7.6 AF: pattern A (falling TPC) defined in 3GPP TS 34.121, table 5.7.7 B: pattern B defined in 3GPP TS 34.121, table 5.7.8
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:ULCM:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TransGapType)

	def set_type_py(self, type_py: enums.TransGapType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:ULCM:TYPE \n
		Snippet: driver.configure.cmode.ulcm.set_type_py(type_py = enums.TransGapType.AF) \n
		Selects the transmission gap patterns for the UL compressed mode TX test. \n
			:param type_py: AR | AF | B AR: pattern A (rising TPC) defined in 3GPP TS 34.121, table 5.7.6 AF: pattern A (falling TPC) defined in 3GPP TS 34.121, table 5.7.7 B: pattern B defined in 3GPP TS 34.121, table 5.7.8
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TransGapType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:ULCM:TYPE {param}')

	def clone(self) -> 'Ulcm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ulcm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
