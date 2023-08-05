from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	def set_action(self, ps_action: enums.PswitchedAction) -> None:
		"""SCPI: CALL:WCDMa:SIGNaling<instance>:PSWitched:ACTion \n
		Snippet: driver.call.pswitched.set_action(ps_action = enums.PswitchedAction.ACONnect) \n
		Controls the PS connection state. As a prerequisite for setup of a test mode connection in the PS domain, a test mode
		connection must be set up in the CS domain, see method RsCmwWcdmaSig.Call.Cswitched.action. \n
			:param ps_action: CONNect | DISConnect | HANDover | ACONnect CONNect: initiate the setup of a mobile terminated HSDPA or HSPA test mode connection DISConnect: release the test mode connection HANDover: execute the handover ACONnect: add PS connection to established CS connection (only for test mode connection type RMC + HSPA)
		"""
		param = Conversions.enum_scalar_to_str(ps_action, enums.PswitchedAction)
		self._core.io.write_with_opc(f'CALL:WCDMa:SIGNaling<Instance>:PSWitched:ACTion {param}')
