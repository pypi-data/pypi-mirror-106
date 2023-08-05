from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	def get_ms_frames(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:BLER:MSFRames \n
		Snippet: value: int = driver.configure.hcqi.bler.get_ms_frames() \n
		Defines the number of HSDPA subframes for the second measurement stage to be measured per measurement cycle (statistics
		cycle) . \n
			:return: meas_sub_frames: Range: 100 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:HCQI:BLER:MSFRames?')
		return Conversions.str_to_int(response)

	def set_ms_frames(self, meas_sub_frames: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:HCQI:BLER:MSFRames \n
		Snippet: driver.configure.hcqi.bler.set_ms_frames(meas_sub_frames = 1) \n
		Defines the number of HSDPA subframes for the second measurement stage to be measured per measurement cycle (statistics
		cycle) . \n
			:param meas_sub_frames: Range: 100 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(meas_sub_frames)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:HCQI:BLER:MSFRames {param}')
