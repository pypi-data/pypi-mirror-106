from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Language:
	"""Language commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("language", core, parent)

	def set(self, language: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: driver.configure.cbs.message.language.set(language = 1) \n
		Specifies the language of CB message as defined in 3GPP TS 23.038. \n
			:param language: Bits 0 to 3 of CBS data coding scheme Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(language)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:LANGuage {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Language: int: Bits 0 to 3 of CBS data coding scheme Range: 0 to 15
			- Lng_Indication: str: Language indication"""
		__meta_args_list = [
			ArgStruct.scalar_int('Language'),
			ArgStruct.scalar_str('Lng_Indication')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Language: int = None
			self.Lng_Indication: str = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: value: GetStruct = driver.configure.cbs.message.language.get() \n
		Specifies the language of CB message as defined in 3GPP TS 23.038. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:LANGuage?', self.__class__.GetStruct())
