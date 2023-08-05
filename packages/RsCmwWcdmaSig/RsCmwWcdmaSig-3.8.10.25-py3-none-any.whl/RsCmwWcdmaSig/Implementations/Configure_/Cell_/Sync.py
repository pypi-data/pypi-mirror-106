from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sync", core, parent)

	# noinspection PyTypeChecker
	def get_zone(self) -> enums.Zone:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SYNC:ZONE \n
		Snippet: value: enums.Zone = driver.configure.cell.sync.get_zone() \n
		Selects the synchronization zone for the signaling application. \n
			:return: zone: NONE | Z1 NONE: no synchronization Z1: synchronization to zone 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SYNC:ZONE?')
		return Conversions.str_to_scalar_enum(response, enums.Zone)

	def set_zone(self, zone: enums.Zone) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SYNC:ZONE \n
		Snippet: driver.configure.cell.sync.set_zone(zone = enums.Zone.NONE) \n
		Selects the synchronization zone for the signaling application. \n
			:param zone: NONE | Z1 NONE: no synchronization Z1: synchronization to zone 1
		"""
		param = Conversions.enum_scalar_to_str(zone, enums.Zone)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SYNC:ZONE {param}')

	def get_offset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SYNC:OFFSet \n
		Snippet: value: float = driver.configure.cell.sync.get_offset() \n
		Configures the timing offset relative to the time zone. \n
			:return: offset: Range: -38399 chips / -99997E-5 s to 0 chips / 0 s, Unit: s
		"""
		response = self._core.io.query_str_with_opc('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SYNC:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SYNC:OFFSet \n
		Snippet: driver.configure.cell.sync.set_offset(offset = 1.0) \n
		Configures the timing offset relative to the time zone. \n
			:param offset: Range: -38399 chips / -99997E-5 s to 0 chips / 0 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SYNC:OFFSet {param}')
