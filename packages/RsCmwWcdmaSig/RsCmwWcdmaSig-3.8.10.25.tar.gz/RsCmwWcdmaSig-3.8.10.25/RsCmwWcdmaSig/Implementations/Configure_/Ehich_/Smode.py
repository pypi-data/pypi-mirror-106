from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smode:
	"""Smode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smode", core, parent)

	# noinspection PyTypeChecker
	def get_average(self) -> enums.AveragingMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:SMODe:AVERage \n
		Snippet: value: enums.AveragingMode = driver.configure.ehich.smode.get_average() \n
		Specifies calculation algorithm for average statistics. Only remote command is provided. No corresponding manual setting
		is existing in the GUI. The setting is especially useful if 'Repetition' = 'Continuous'. \n
			:return: mode: WINDow | CONTinuous WINDow: average results calculated per statistic cycle ('Measure Frames') CONTinuous: average results calculated since the beginning of the measurement
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:EHICh:SMODe:AVERage?')
		return Conversions.str_to_scalar_enum(response, enums.AveragingMode)

	def set_average(self, mode: enums.AveragingMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:EHICh:SMODe:AVERage \n
		Snippet: driver.configure.ehich.smode.set_average(mode = enums.AveragingMode.CONTinuous) \n
		Specifies calculation algorithm for average statistics. Only remote command is provided. No corresponding manual setting
		is existing in the GUI. The setting is especially useful if 'Repetition' = 'Continuous'. \n
			:param mode: WINDow | CONTinuous WINDow: average results calculated per statistic cycle ('Measure Frames') CONTinuous: average results calculated since the beginning of the measurement
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AveragingMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:EHICh:SMODe:AVERage {param}')
