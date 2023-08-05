from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conformance:
	"""Conformance commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("conformance", core, parent)

	def get_mode(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:CONFormance:MODE \n
		Snippet: value: bool = driver.configure.cell.hsdpa.cqi.conformance.get_mode() \n
		Enables or disables 64QAM modulation in CQI conformance test mode. \n
			:return: disable_qam_64: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:CONFormance:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, disable_qam_64: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:CONFormance:MODE \n
		Snippet: driver.configure.cell.hsdpa.cqi.conformance.set_mode(disable_qam_64 = False) \n
		Enables or disables 64QAM modulation in CQI conformance test mode. \n
			:param disable_qam_64: OFF | ON
		"""
		param = Conversions.bool_to_str(disable_qam_64)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:CONFormance:MODE {param}')
