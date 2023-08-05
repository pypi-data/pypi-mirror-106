from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	def get_lmsent(self) -> enums.SucessState:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:SMS:OUTGoing:INFO:LMSent \n
		Snippet: value: enums.SucessState = driver.sense.sms.outgoing.info.get_lmsent() \n
		Indicates, whether the last message was sent successfully or not. \n
			:return: state: FAILed | SUCCessful
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:SMS:OUTGoing:INFO:LMSent?')
		return Conversions.str_to_scalar_enum(response, enums.SucessState)
