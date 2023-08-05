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
	def fetch(self) -> enums.ReducedSignState:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:RSIGnaling:STATe \n
		Snippet: value: enums.ReducedSignState = driver.rsignaling.state.fetch() \n
		Queries the reduced signaling connection state, see also 'Connection States for Reduced Signaling'. \n
			:return: rsig_state: OFF | PROCessing | ON OFF: reduced signaling Off ON: reduced signaling On PROCessing: switching channels On/Off"""
		response = self._core.io.query_str(f'FETCh:WCDMa:SIGNaling<Instance>:RSIGnaling:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.ReducedSignState)
