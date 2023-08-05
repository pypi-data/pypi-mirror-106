from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reported:
	"""Reported commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reported", core, parent)

	def set(self, use_reported: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UECategory:REPorted \n
		Snippet: driver.configure.cell.hsdpa.ueCategory.reported.set(use_reported = False) \n
		Enable or disable usage of the UE category value reported by the UE. When disabled, the UE category must be set manually,
		see method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UeCategory.manual. The manually set value is also used if no reported value
		is available. \n
			:param use_reported: OFF | ON
		"""
		param = Conversions.bool_to_str(use_reported)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UECategory:REPorted {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Use_Reported: bool: OFF | ON
			- Ue_Cat_Reported: int: UE category reported by the UE (NAV indicates that none has been reported) Range: 1 to 24"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Use_Reported'),
			ArgStruct.scalar_int('Ue_Cat_Reported')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Use_Reported: bool = None
			self.Ue_Cat_Reported: int = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UECategory:REPorted \n
		Snippet: value: GetStruct = driver.configure.cell.hsdpa.ueCategory.reported.get() \n
		Enable or disable usage of the UE category value reported by the UE. When disabled, the UE category must be set manually,
		see method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UeCategory.manual. The manually set value is also used if no reported value
		is available. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UECategory:REPorted?', self.__class__.GetStruct())
