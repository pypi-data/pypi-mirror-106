from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	def set(self, band: enums.OperationBand, channel: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:UL \n
		Snippet: driver.configure.rfSettings.carrier.uplink.set(band = enums.OperationBand.OB1, channel = 1) \n
		No command help available \n
			:param band: No help available
			:param channel: No help available
		Global Repeated Capabilities: repcap.Carrier
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum), ArgSingle('channel', channel, DataType.Integer))
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:UL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperationBand: No parameter help available
			- Channel: int: No parameter help available
			- Frequency: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperationBand),
			ArgStruct.scalar_int('Channel'),
			ArgStruct.scalar_float('Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperationBand = None
			self.Channel: int = None
			self.Frequency: float = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:UL \n
		Snippet: value: GetStruct = driver.configure.rfSettings.carrier.uplink.get() \n
		No command help available \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:UL?', self.__class__.GetStruct())
