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
	def fetch(self) -> enums.ResourceState:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:UEReport:STATe \n
		Snippet: value: enums.ResourceState = driver.ueReport.state.fetch() \n
		Queries the state of UE measurement reporting. \n
			:return: state: RDY | PENDing RDY: Any requested reports have been received. PENDing: The instrument is waiting for reports from the UE."""
		response = self._core.io.query_str(f'FETCh:WCDMa:SIGNaling<Instance>:UEReport:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)
