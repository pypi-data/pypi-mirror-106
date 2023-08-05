from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.PswitchedState:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:PSWitched:STATe \n
		Snippet: value: enums.PswitchedState = driver.pswitched.state.fetch() \n
		Queries the PS connection state, see also 'PS Connection States'. \n
			:return: ps_state: OFF | ON | ATTached | CESTablished | RELeasing | CONNecting | SIGNaling | IHPReparate | IHANdover | OHANdover | IRPReparate | IREDirection | OREDirection OFF: signal is off ON: signal is on ATTached: attached CESTablished: connection established RELeasing: disconnect in progress CONNecting: connection setup in progress SIGNaling: signaling in progress IHPReparate: preparation for incoming handover IHANdover incoming handover in progress OHANdover outgoing handover in progress IRPReparate: preparation for incoming redirection IREDirection: incoming redirection in progress OREDirection: outgoing redirection in progress"""
		response = self._core.io.query_str(f'FETCh:WCDMa:SIGNaling<Instance>:PSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PswitchedState)
