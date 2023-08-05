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
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HORDer:SEND \n
		Snippet: driver.configure.cell.cpc.horder.send.set() \n
		Tells the UE to enable/disable discontinuous downlink reception and/or discontinuous uplink DPCCH transmission and
		queries the frame number, subframe number and acknowledgment related to the HS-SCCH order type 0 execution.
		See also 'Continuous Packet Connectivity (CPC) '. \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HORDer:SEND')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HORDer:SEND \n
		Snippet: driver.configure.cell.cpc.horder.send.set_with_opc() \n
		Tells the UE to enable/disable discontinuous downlink reception and/or discontinuous uplink DPCCH transmission and
		queries the frame number, subframe number and acknowledgment related to the HS-SCCH order type 0 execution.
		See also 'Continuous Packet Connectivity (CPC) '. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HORDer:SEND')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frame_Number: int: Information about frame from which the UE has applied the HS-SCCH order
			- Sfn: int: Information about subframe from which the UE has applied the HS-SCCH order
			- Ack: enums.AckNack: ACK | NACK | DTX ACK: positive acknowledgment NACK: negative acknowledgment DTX: no acknowledgment"""
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
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:HORDer:SEND \n
		Snippet: value: GetStruct = driver.configure.cell.cpc.horder.send.get() \n
		Tells the UE to enable/disable discontinuous downlink reception and/or discontinuous uplink DPCCH transmission and
		queries the frame number, subframe number and acknowledgment related to the HS-SCCH order type 0 execution.
		See also 'Continuous Packet Connectivity (CPC) '. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:HORDer:SEND?', self.__class__.GetStruct())
