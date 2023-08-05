from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	# noinspection PyTypeChecker
	class InfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: str: Time stamp of sending
			- Reserved: str: For future use
			- Message_Encoding: str: Encoding of the ANSI message (ASCII, binary, Unicode)
			- Message_Text: str: Message text
			- Message_Length: int: The number of characters in the message Range: 0 to 10E+3
			- Message_Segments: int: The segment number Range: 0 to 1000
			- Used_Send_Method: enums.UsedSendMethod: WDEFault The send method used by the UE"""
		__meta_args_list = [
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_str('Reserved'),
			ArgStruct.scalar_str('Message_Encoding'),
			ArgStruct.scalar_str('Message_Text'),
			ArgStruct.scalar_int('Message_Length'),
			ArgStruct.scalar_int('Message_Segments'),
			ArgStruct.scalar_enum('Used_Send_Method', enums.UsedSendMethod)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: str = None
			self.Reserved: str = None
			self.Message_Encoding: str = None
			self.Message_Text: str = None
			self.Message_Length: int = None
			self.Message_Segments: int = None
			self.Used_Send_Method: enums.UsedSendMethod = None

	def get_info(self) -> InfoStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:SMS:INComing:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.sms.incoming.file.get_info() \n
		Display information on the received message file referenced by method RsCmwWcdmaSig.Configure.Sms.Incoming.File.value. \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:SMS:INComing:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:SMS:INComing:FILE \n
		Snippet: value: str = driver.configure.sms.incoming.file.get_value() \n
		Selects a received message file.
		The message files are stored in the directory D:/Rohde-Schwarz/CMW/Data/SMS/WCDMA/Received/. \n
			:return: sms_file: String parameter to specify the received message file.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:SMS:INComing:FILE?')
		return trim_str_response(response)

	def set_value(self, sms_file: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:SMS:INComing:FILE \n
		Snippet: driver.configure.sms.incoming.file.set_value(sms_file = '1') \n
		Selects a received message file.
		The message files are stored in the directory D:/Rohde-Schwarz/CMW/Data/SMS/WCDMA/Received/. \n
			:param sms_file: String parameter to specify the received message file.
		"""
		param = Conversions.value_to_quoted_str(sms_file)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:SMS:INComing:FILE {param}')
