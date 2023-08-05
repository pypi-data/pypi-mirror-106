from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upch:
	"""Upch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("upch", core, parent)

	def get_timer(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:UPCH:TIMer \n
		Snippet: value: int = driver.configure.connection.packet.inactivity.upch.get_timer() \n
		Sets the timeout value for network-initiated automatic RRC state transition
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:CPCH:... for origination state CELL_PCH
			- ...:FACH:... for origination state CELL_FACH
			- ...:UPCH:... for origination state URA_PCH \n
			:return: inactivity_time: Range: 1 s to 120 s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:UPCH:TIMer?')
		return Conversions.str_to_int(response)

	def set_timer(self, inactivity_time: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:UPCH:TIMer \n
		Snippet: driver.configure.connection.packet.inactivity.upch.set_timer(inactivity_time = 1) \n
		Sets the timeout value for network-initiated automatic RRC state transition
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:CPCH:... for origination state CELL_PCH
			- ...:FACH:... for origination state CELL_FACH
			- ...:UPCH:... for origination state URA_PCH \n
			:param inactivity_time: Range: 1 s to 120 s
		"""
		param = Conversions.decimal_value_to_str(inactivity_time)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:UPCH:TIMer {param}')
