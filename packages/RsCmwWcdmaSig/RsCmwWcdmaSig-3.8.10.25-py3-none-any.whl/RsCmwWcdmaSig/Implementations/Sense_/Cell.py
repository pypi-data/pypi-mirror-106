from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	# noinspection PyTypeChecker
	def get_config(self) -> enums.CellConfig:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:CELL:CONFig \n
		Snippet: value: enums.CellConfig = driver.sense.cell.get_config() \n
		Returns information corresponding to the gray/green icons displayed behind the cell state in the 'Connection Status' area
		of the main view. The icons indicate the type of a PS connection. \n
			:return: config: WCDMa | HSDPa | HSPLus | DCHS | HSPA | HDUPlus | DDUPlus | DHDU | 3CHS | 3DUPlus | 3HDU WCDMa: R99 signal, no HSPA test mode HSDPa: HSDPA HSPLus: HSDPA+ DCHS: dual carrier HSDPA+ HSPA: HSDPA and HSUPA HDUPlus: HSDPA+ and HSUPA DDUPlus: dual carrier HSDPA+ and single carrier HSUPA DHDU: dual carrier HSDPA+ and dual carrier HSUPA 3CHS: three carrier HSDPA+ 3DUPlus: three carrier HSDPA+ and single carrier HSUPA 3HDU: three carrier HSDPA+ and dual carrier HSUPA
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:CELL:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.CellConfig)
