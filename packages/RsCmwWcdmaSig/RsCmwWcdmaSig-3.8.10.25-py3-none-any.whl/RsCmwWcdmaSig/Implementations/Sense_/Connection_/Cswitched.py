from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	def get_attempt(self) -> int:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:CONNection:CSWitched:ATTempt \n
		Snippet: value: int = driver.sense.connection.cswitched.get_attempt() \n
		Queries the counters of connection attempt / reject. \n
			:return: counter: Range: 0 to 2^32
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:ATTempt?')
		return Conversions.str_to_int(response)

	def get_reject(self) -> int:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:CONNection:CSWitched:REJect \n
		Snippet: value: int = driver.sense.connection.cswitched.get_reject() \n
		Queries the counters of connection attempt / reject. \n
			:return: counter: Range: 0 to 2^32
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:REJect?')
		return Conversions.str_to_int(response)
