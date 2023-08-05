from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etfci:
	"""Etfci commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etfci", core, parent)

	def get_mset(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ETFCi:MSET \n
		Snippet: value: int or bool = driver.configure.cell.carrier.hsupa.etfci.get_mset() \n
		Specifies the 'E-DCH minimum set E-TFCI' value signaled to the UE. \n
			:return: min_set: Range: 0 to 127 Additional OFF | ON disables | enables the transmission of E-TFCI minimum set
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ETFCi:MSET?')
		return Conversions.str_to_int_or_bool(response)

	def set_mset(self, min_set: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:ETFCi:MSET \n
		Snippet: driver.configure.cell.carrier.hsupa.etfci.set_mset(min_set = 1) \n
		Specifies the 'E-DCH minimum set E-TFCI' value signaled to the UE. \n
			:param min_set: Range: 0 to 127 Additional OFF | ON disables | enables the transmission of E-TFCI minimum set
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_or_bool_value_to_str(min_set)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:ETFCi:MSET {param}')
