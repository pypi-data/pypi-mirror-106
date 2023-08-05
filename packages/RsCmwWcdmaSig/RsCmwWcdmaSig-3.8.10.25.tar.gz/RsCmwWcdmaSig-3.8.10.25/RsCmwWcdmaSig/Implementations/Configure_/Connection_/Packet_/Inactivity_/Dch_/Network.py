from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("network", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:ENABle \n
		Snippet: value: bool = driver.configure.connection.packet.inactivity.dch.network.get_enable() \n
		Enables or disables the network-initiated automatic RRC state transitions of the UE for the originating states CELL_DCH,
		CELL_FACH, CELL_PCH and URA_PCH. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:ENABle \n
		Snippet: driver.configure.connection.packet.inactivity.dch.network.set_enable(enable = False) \n
		Enables or disables the network-initiated automatic RRC state transitions of the UE for the originating states CELL_DCH,
		CELL_FACH, CELL_PCH and URA_PCH. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:ENABle {param}')

	def get_timer(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:TIMer \n
		Snippet: value: int = driver.configure.connection.packet.inactivity.dch.network.get_timer() \n
		Sets the timeout value for network-initiated automatic RRC state transition for originating state CELL_DCH. \n
			:return: inactivity_time: Range: 1 s to 120 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:TIMer?')
		return Conversions.str_to_int(response)

	def set_timer(self, inactivity_time: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:TIMer \n
		Snippet: driver.configure.connection.packet.inactivity.dch.network.set_timer(inactivity_time = 1) \n
		Sets the timeout value for network-initiated automatic RRC state transition for originating state CELL_DCH. \n
			:param inactivity_time: Range: 1 s to 120 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(inactivity_time)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:TIMer {param}')

	# noinspection PyTypeChecker
	def get_dstate(self) -> enums.DestinationState:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:DSTate \n
		Snippet: value: enums.DestinationState = driver.configure.connection.packet.inactivity.dch.network.get_dstate() \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:return: dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:DSTate?')
		return Conversions.str_to_scalar_enum(response, enums.DestinationState)

	def set_dstate(self, dest_state: enums.DestinationState) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:NETWork:DSTate \n
		Snippet: driver.configure.connection.packet.inactivity.dch.network.set_dstate(dest_state = enums.DestinationState.CPCH) \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:param dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		param = Conversions.enum_scalar_to_str(dest_state, enums.DestinationState)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:NETWork:DSTate {param}')
