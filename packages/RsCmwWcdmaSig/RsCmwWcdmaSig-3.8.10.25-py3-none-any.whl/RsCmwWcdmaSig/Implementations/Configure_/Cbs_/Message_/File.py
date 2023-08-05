from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	# noinspection PyTypeChecker
	class InfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Message_Encoding: str: Encoding of the CB message (UTF16)
			- Message_Text: str: Message text
			- Message_Length: int: The number of characters in the message Range: 0 to 600"""
		__meta_args_list = [
			ArgStruct.scalar_str('Message_Encoding'),
			ArgStruct.scalar_str('Message_Text'),
			ArgStruct.scalar_int('Message_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Message_Encoding: str = None
			self.Message_Text: str = None
			self.Message_Length: int = None

	def get_info(self) -> InfoStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.cbs.message.file.get_info() \n
		Display information of the outgoing CB message file referenced by method RsCmwWcdmaSig.Configure.Cbs.Message.File.value. \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:FILE \n
		Snippet: value: str = driver.configure.cbs.message.file.get_value() \n
		Selects a CB message file. To view details of the message use method RsCmwWcdmaSig.Configure.Cbs.Message.File.info. The
		message files are stored in the directory D:/Rohde-Schwarz/CMW/Data/cbs/WCDMA/. \n
			:return: file: File to be used for CB message
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:FILE?')
		return trim_str_response(response)

	def set_value(self, file: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:MESSage:FILE \n
		Snippet: driver.configure.cbs.message.file.set_value(file = '1') \n
		Selects a CB message file. To view details of the message use method RsCmwWcdmaSig.Configure.Cbs.Message.File.info. The
		message files are stored in the directory D:/Rohde-Schwarz/CMW/Data/cbs/WCDMA/. \n
			:param file: File to be used for CB message
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:MESSage:FILE {param}')
