from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdu:
	"""Pdu commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdu", core, parent)

	def get_flexible(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PDU:FLEXible \n
		Snippet: value: int or bool = driver.configure.cell.hsupa.pdu.get_flexible() \n
		Enables and selects the maximum RLC PDU size to be signaled to the UE to configure its flexible UL RLC PDU for dual
		uplink carrier connections. \n
			:return: flexible_max: Range: 16 to 12.04E+3 Additional ON/OFF enables/disables flexible PDU size.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PDU:FLEXible?')
		return Conversions.str_to_int_or_bool(response)

	def set_flexible(self, flexible_max: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PDU:FLEXible \n
		Snippet: driver.configure.cell.hsupa.pdu.set_flexible(flexible_max = 1) \n
		Enables and selects the maximum RLC PDU size to be signaled to the UE to configure its flexible UL RLC PDU for dual
		uplink carrier connections. \n
			:param flexible_max: Range: 16 to 12.04E+3 Additional ON/OFF enables/disables flexible PDU size.
		"""
		param = Conversions.decimal_or_bool_value_to_str(flexible_max)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PDU:FLEXible {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PDU \n
		Snippet: value: int = driver.configure.cell.hsupa.pdu.get_value() \n
		Selects the RLC PDU size to be signaled to the UE to configure its constant UL RLC PDU size. \n
			:return: size: Range: 72 to 5000
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PDU?')
		return Conversions.str_to_int(response)

	def set_value(self, size: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PDU \n
		Snippet: driver.configure.cell.hsupa.pdu.set_value(size = 1) \n
		Selects the RLC PDU size to be signaled to the UE to configure its constant UL RLC PDU size. \n
			:param size: Range: 72 to 5000
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PDU {param}')
