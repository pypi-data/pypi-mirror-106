from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rstate:
	"""Rstate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rstate", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.ResultState:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HCQI:RSTate \n
		Snippet: value: enums.ResultState = driver.hcqi.rstate.fetch() \n
		Queries the result of the entire HSDPA CQI measurement including all stages. \n
			:return: result_state: FAIL | PASS | RUN Measurement failed, passed, running."""
		response = self._core.io.query_str(f'FETCh:WCDMa:SIGNaling<Instance>:HCQI:RSTate?')
		return Conversions.str_to_scalar_enum(response, enums.ResultState)
