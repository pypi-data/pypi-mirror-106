from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Send:
	"""Send commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("send", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SEND \n
		Snippet: driver.configure.cell.hsupa.horder.send.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SEND')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SEND \n
		Snippet: driver.configure.cell.hsupa.horder.send.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SEND')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frame_Number: int: No parameter help available
			- Sfn: int: No parameter help available
			- Ack: enums.AckNack: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Frame_Number'),
			ArgStruct.scalar_int('Sfn'),
			ArgStruct.scalar_enum('Ack', enums.AckNack)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frame_Number: int = None
			self.Sfn: int = None
			self.Ack: enums.AckNack = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HORDer:SEND \n
		Snippet: value: GetStruct = driver.configure.cell.hsupa.horder.send.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HORDer:SEND?', self.__class__.GetStruct())
