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
	def fetch(self) -> enums.CswitchedState:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:CSWitched:STATe \n
		Snippet: value: enums.CswitchedState = driver.cswitched.state.fetch() \n
		Queries the CS connection state, see also 'CS Connection States'. Use method RsCmwWcdmaSig.Call.Cswitched.
		action to initiate a transition between different connection states. The CS state changes to ON when the signaling
		generator is started (see method RsCmwWcdmaSig.Source.Cell.State.value) . To make sure that a WCDMA cell signal is
		available, query the cell state. It must be ON, ADJ (see method RsCmwWcdmaSig.Source.Cell.State.all) . \n
			:return: cs_state: ON | REGister | ALERting | CONNecting | PAGing | RELeasing | SIGNaling | IHPReparate | IHANdover | OHANdover | OFF | CESTablished | IRPReparate | IREDirection | OREDirection ON: signal is on REGister: registered ALERting: alerting CONNecting: call setup in progress PAGing: paging in progress RELeasing: disconnect in progress SIGNaling: signaling in progress IHPReparate: preparation for incoming handover IHANdover: incoming handover in progress OHANdover: outgoing handover in progress OFF: signal is off CESTablished: call established IRPReparate: preparation for incoming redirection IREDirection: incoming redirection in progress OREDirection: outgoing redirection in progress"""
		response = self._core.io.query_str(f'FETCh:WCDMa:SIGNaling<Instance>:CSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.CswitchedState)
