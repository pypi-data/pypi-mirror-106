from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	def set_action(self, cs_action: enums.CswitchedAction) -> None:
		"""SCPI: CALL:WCDMa:SIGNaling<instance>:CSWitched:ACTion \n
		Snippet: driver.call.cswitched.set_action(cs_action = enums.CswitchedAction.CONNect) \n
		Controls the CS connection state. As a prerequisite for connection setup the DL signal has to be switched on, see method
		RsCmwWcdmaSig.Source.Cell.State.value. \n
			:param cs_action: CONNect | DISConnect | SSMS | UNRegister | HANDover CONNect: Initiate a CS connection setup DISConnect: Release a CS connection SSMS: Send SMS UNRegister: Unregister the UE completely (CS unregister and PS detach) , i.e. change to state 'On' HANDover: Initiate a handover
		"""
		param = Conversions.enum_scalar_to_str(cs_action, enums.CswitchedAction)
		self._core.io.write_with_opc(f'CALL:WCDMa:SIGNaling<Instance>:CSWitched:ACTion {param}')
