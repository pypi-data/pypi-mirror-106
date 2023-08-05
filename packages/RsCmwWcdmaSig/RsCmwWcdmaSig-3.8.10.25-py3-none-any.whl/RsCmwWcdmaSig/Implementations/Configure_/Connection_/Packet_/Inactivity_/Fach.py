from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fach:
	"""Fach commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fach", core, parent)

	def get_timer(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:FACH:TIMer \n
		Snippet: value: int = driver.configure.connection.packet.inactivity.fach.get_timer() \n
		Sets the timeout value for network-initiated automatic RRC state transition
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:CPCH:... for origination state CELL_PCH
			- ...:FACH:... for origination state CELL_FACH
			- ...:UPCH:... for origination state URA_PCH \n
			:return: inactivity_time: Range: 1 s to 120 s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:FACH:TIMer?')
		return Conversions.str_to_int(response)

	def set_timer(self, inactivity_time: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:FACH:TIMer \n
		Snippet: driver.configure.connection.packet.inactivity.fach.set_timer(inactivity_time = 1) \n
		Sets the timeout value for network-initiated automatic RRC state transition
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:CPCH:... for origination state CELL_PCH
			- ...:FACH:... for origination state CELL_FACH
			- ...:UPCH:... for origination state URA_PCH \n
			:param inactivity_time: Range: 1 s to 120 s
		"""
		param = Conversions.decimal_value_to_str(inactivity_time)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:FACH:TIMer {param}')

	# noinspection PyTypeChecker
	def get_dstate(self) -> enums.DestinationState:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:FACH:DSTate \n
		Snippet: value: enums.DestinationState = driver.configure.connection.packet.inactivity.fach.get_dstate() \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:return: dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:FACH:DSTate?')
		return Conversions.str_to_scalar_enum(response, enums.DestinationState)

	def set_dstate(self, dest_state: enums.DestinationState) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:FACH:DSTate \n
		Snippet: driver.configure.connection.packet.inactivity.fach.set_dstate(dest_state = enums.DestinationState.CPCH) \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:param dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		param = Conversions.enum_scalar_to_str(dest_state, enums.DestinationState)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:FACH:DSTate {param}')
