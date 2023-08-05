from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	def get_mtext(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:SMS:INComing:INFO:MTEXt \n
		Snippet: value: str = driver.sense.sms.incoming.info.get_mtext() \n
		Returns the text of the last SMS message received from the UE. Only 7-bit ASCII text is supported. \n
			:return: message_text: Message text as string
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:SMS:INComing:INFO:MTEXt?')
		return trim_str_response(response)

	def get_mlength(self) -> int:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:SMS:INComing:INFO:MLENgth \n
		Snippet: value: int = driver.sense.sms.incoming.info.get_mlength() \n
		Returns the length of the last SMS message received from the UE. \n
			:return: message_length: Number of characters of the message Range: 0 to 160
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:SMS:INComing:INFO:MLENgth?')
		return Conversions.str_to_int(response)
