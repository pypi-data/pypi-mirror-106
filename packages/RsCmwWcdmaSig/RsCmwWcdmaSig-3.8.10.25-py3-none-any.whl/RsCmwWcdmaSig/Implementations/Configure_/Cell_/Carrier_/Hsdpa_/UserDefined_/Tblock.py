from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tblock:
	"""Tblock commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tblock", core, parent)

	def set(self, index: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:TBLock \n
		Snippet: driver.configure.cell.carrier.hsdpa.userDefined.tblock.set(index = 1) \n
		Specifies the value of the transport format and resource indicator (TFRI) signaled to the UE. A query returns also the
		resulting transport block size. \n
			:param index: Transport block size index (TFRI value) Range: 0 to 62
		Global Repeated Capabilities: repcap.Carrier
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:TBLock {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: int: Transport block size index (TFRI value) Range: 0 to 62
			- Size: int: Used transport block size resulting from the settings Range: 0 bits to 28.8E+3 bits"""
		__meta_args_list = [
			ArgStruct.scalar_int('Index'),
			ArgStruct.scalar_int('Size')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: int = None
			self.Size: int = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:TBLock \n
		Snippet: value: GetStruct = driver.configure.cell.carrier.hsdpa.userDefined.tblock.get() \n
		Specifies the value of the transport format and resource indicator (TFRI) signaled to the UE. A query returns also the
		resulting transport block size. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:TBLock?', self.__class__.GetStruct())
