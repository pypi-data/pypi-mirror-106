from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UefDormancy:
	"""UefDormancy commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uefDormancy", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:ENABle \n
		Snippet: value: bool = driver.configure.connection.packet.inactivity.dch.uefDormancy.get_enable() \n
		Enables or disables the UE-initiated UE fast dormancy for the UE RRC state CELL_DCH. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:ENABle \n
		Snippet: driver.configure.connection.packet.inactivity.dch.uefDormancy.set_enable(enable = False) \n
		Enables or disables the UE-initiated UE fast dormancy for the UE RRC state CELL_DCH. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:ENABle {param}')

	def get_timer(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:TIMer \n
		Snippet: value: int = driver.configure.connection.packet.inactivity.dch.uefDormancy.get_timer() \n
		Sets the T323 timeout value for UE fast dormancy. \n
			:return: t_323: Range: 0 s to 120 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:TIMer?')
		return Conversions.str_to_int(response)

	def set_timer(self, t_323: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:TIMer \n
		Snippet: driver.configure.connection.packet.inactivity.dch.uefDormancy.set_timer(t_323 = 1) \n
		Sets the T323 timeout value for UE fast dormancy. \n
			:param t_323: Range: 0 s to 120 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(t_323)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:TIMer {param}')

	# noinspection PyTypeChecker
	def get_dstate(self) -> enums.DestinationState:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:DSTate \n
		Snippet: value: enums.DestinationState = driver.configure.connection.packet.inactivity.dch.uefDormancy.get_dstate() \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:return: dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:DSTate?')
		return Conversions.str_to_scalar_enum(response, enums.DestinationState)

	def set_dstate(self, dest_state: enums.DestinationState) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:DSTate \n
		Snippet: driver.configure.connection.packet.inactivity.dch.uefDormancy.set_dstate(dest_state = enums.DestinationState.CPCH) \n
		Specifies the destination state of the UE for automatic RRC transitions.
			INTRO_CMD_HELP: The origination RRC state is indicated in the remote command name as follows: \n
			- ...:DCH:NETWork:... for state CELL_DCH (network-initiated RRC transition)
			- ...:DCH:UEFDormacy:... for state CELL_DCH (UE-initiated RRC transition)
			- ...:FACH:... for state CELL_FACH \n
			:param dest_state: IDLE | FACH | CPCH | UPCH Idle, CELL_FACH, CELL_PCH, URA_PCH
		"""
		param = Conversions.enum_scalar_to_str(dest_state, enums.DestinationState)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:INACtivity:DCH:UEFDormancy:DSTate {param}')
