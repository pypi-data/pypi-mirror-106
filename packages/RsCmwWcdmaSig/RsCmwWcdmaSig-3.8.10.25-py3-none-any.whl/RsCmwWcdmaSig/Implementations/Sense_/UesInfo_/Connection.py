from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	def get_packet(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:CONNection:PACKet \n
		Snippet: value: str = driver.sense.uesInfo.connection.get_packet() \n
		Queries the type of an established PS connection. NAV indicates that no PS connection has been established. \n
			:return: packet_connect: Connection type as string
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:CONNection:PACKet?')
		return trim_str_response(response)

	def get_circuit(self) -> str:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UESinfo:CONNection:CIRCuit \n
		Snippet: value: str = driver.sense.uesInfo.connection.get_circuit() \n
		Queries the type of an established CS connection. NAV indicates that no CS connection has been established. \n
			:return: circuit_connect: Connection type as string
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UESinfo:CONNection:CIRCuit?')
		return trim_str_response(response)
