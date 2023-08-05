from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attempt:
	"""Attempt commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("attempt", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:WCDMa:SIGNaling<instance>:CONNection:CSWitched:ATTempt \n
		Snippet: driver.clean.connection.cswitched.attempt.set() \n
		Sets the counters of connection attempt / reject to zero. \n
		"""
		self._core.io.write(f'CLEan:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:ATTempt')

	def set_with_opc(self) -> None:
		"""SCPI: CLEan:WCDMa:SIGNaling<instance>:CONNection:CSWitched:ATTempt \n
		Snippet: driver.clean.connection.cswitched.attempt.set_with_opc() \n
		Sets the counters of connection attempt / reject to zero. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CLEan:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:ATTempt')
