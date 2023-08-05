from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrbSingle:
	"""SrbSingle commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("srbSingle", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.SrbSingleType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:SRBSingle:TYPE \n
		Snippet: value: enums.SrbSingleType = driver.configure.connection.srbSingle.get_type_py() \n
		Selects the radio resource control state to which the UE is commanded when an 'SRB only' connection is set up. \n
			:return: type_py: CDCH | CFACh CDCH: CELL_DCH CFACh: CELL_FACH
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:SRBSingle:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SrbSingleType)

	def set_type_py(self, type_py: enums.SrbSingleType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:SRBSingle:TYPE \n
		Snippet: driver.configure.connection.srbSingle.set_type_py(type_py = enums.SrbSingleType.CDCH) \n
		Selects the radio resource control state to which the UE is commanded when an 'SRB only' connection is set up. \n
			:param type_py: CDCH | CFACh CDCH: CELL_DCH CFACh: CELL_FACH
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.SrbSingleType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:SRBSingle:TYPE {param}')
