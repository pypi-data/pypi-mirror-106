from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsignaling:
	"""Rsignaling commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rsignaling", core, parent)

	def set_action(self, rs_action: bool) -> None:
		"""SCPI: CALL:WCDMa:SIGNaling<instance>:RSIGnaling:ACTion \n
		Snippet: driver.call.rsignaling.set_action(rs_action = False) \n
		Switches the reduced signaling connection on or off, i.e. activates or deactivates the dedicated (and shared) downlink
		channels. As a prerequisite for switching on the connection, the cell signal has to be switched on, see method
		RsCmwWcdmaSig.Source.Cell.State.value. \n
			:param rs_action: ON | OFF ON: Switch on the reduced signaling connection OFF: Switch off the reduced signaling connection
		"""
		param = Conversions.bool_to_str(rs_action)
		self._core.io.write_with_opc(f'CALL:WCDMa:SIGNaling<Instance>:RSIGnaling:ACTion {param}')
