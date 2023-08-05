from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Single:
	"""Single commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("single", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.TransGapTypeExtended:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:SINGle:TYPE \n
		Snippet: value: enums.TransGapTypeExtended = driver.configure.cmode.single.get_type_py() \n
		Selects the single transmission gap patterns for a definite measurement purpose. \n
			:return: type_py: RFA | RFB | A | B | C | D | E | F RFA: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table 5.7.5) RFB: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table 5.7.8) A: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table C.5.2, set 1) B: for GSM neighbor cell measurements (see 3GPP TS 34.121, table C.5.2, set 2) C: to search for the BSIC and decode it (see 3GPP TS 25.133, table 8.7, pattern 2) D: to track and decode the BSIC after an initial BSIC identification (see 3GPP TS 25.133, table 8.8, pattern 2) E: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table C.5.1 set 1) F:
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:SINGle:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TransGapTypeExtended)

	def set_type_py(self, type_py: enums.TransGapTypeExtended) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:SINGle:TYPE \n
		Snippet: driver.configure.cmode.single.set_type_py(type_py = enums.TransGapTypeExtended.A) \n
		Selects the single transmission gap patterns for a definite measurement purpose. \n
			:param type_py: RFA | RFB | A | B | C | D | E | F RFA: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table 5.7.5) RFB: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table 5.7.8) A: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table C.5.2, set 1) B: for GSM neighbor cell measurements (see 3GPP TS 34.121, table C.5.2, set 2) C: to search for the BSIC and decode it (see 3GPP TS 25.133, table 8.7, pattern 2) D: to track and decode the BSIC after an initial BSIC identification (see 3GPP TS 25.133, table 8.8, pattern 2) E: for WCDMA neighbor cell measurements (see 3GPP TS 34.121, table C.5.1 set 1) F:
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TransGapTypeExtended)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:SINGle:TYPE {param}')

	# noinspection PyTypeChecker
	def get_activation(self) -> enums.CmodeActivation:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:SINGle:ACTivation \n
		Snippet: value: enums.CmodeActivation = driver.configure.cmode.single.get_activation() \n
		Selects whether the compressed mode has to be activated for the whole duration of the connection (RAB setup) or for the
		duration of a UE report measurement only. \n
			:return: activation: RAB | MEASurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CMODe:SINGle:ACTivation?')
		return Conversions.str_to_scalar_enum(response, enums.CmodeActivation)

	def set_activation(self, activation: enums.CmodeActivation) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:SINGle:ACTivation \n
		Snippet: driver.configure.cmode.single.set_activation(activation = enums.CmodeActivation.MEASurement) \n
		Selects whether the compressed mode has to be activated for the whole duration of the connection (RAB setup) or for the
		duration of a UE report measurement only. \n
			:param activation: RAB | MEASurement
		"""
		param = Conversions.enum_scalar_to_str(activation, enums.CmodeActivation)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:SINGle:ACTivation {param}')
