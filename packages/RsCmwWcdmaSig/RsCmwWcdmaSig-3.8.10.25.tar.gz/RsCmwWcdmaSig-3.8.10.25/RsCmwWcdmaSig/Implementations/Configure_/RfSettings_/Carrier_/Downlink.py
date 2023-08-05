from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("downlink", core, parent)

	def set(self, band: enums.OperationBand, channel: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:DL \n
		Snippet: driver.configure.rfSettings.carrier.downlink.set(band = enums.OperationBand.OB1, channel = 1) \n
		Selects the operating band and the DL channel number. The channel number must be valid for the operating band, for
		dependencies see 'Operating Bands'. The related UL channel number is calculated and set automatically. For scenarios with
		multi-carrier, the channel numbers of the other carriers are calculated and set as well. \n
			:param band: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OB32 | OBS1 | ... | OBS3 | OBL1 | UDEFined OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OB32: operating band XXXII (restricted to dual band scenarios) OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L UDEFined: user defined
			:param channel: Range: depends on operating band
		Global Repeated Capabilities: repcap.Carrier
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('band', band, DataType.Enum), ArgSingle('channel', channel, DataType.Integer))
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:DL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Band: enums.OperationBand: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OB32 | OBS1 | ... | OBS3 | OBL1 | UDEFined OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OB32: operating band XXXII (restricted to dual band scenarios) OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L UDEFined: user defined
			- Channel: int: Range: depends on operating band
			- Frequency: float: A query returns band, channel number and corresponding carrier center frequency Range: depends on operating band"""
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
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:CARRier<carrier>:DL \n
		Snippet: value: GetStruct = driver.configure.rfSettings.carrier.downlink.get() \n
		Selects the operating band and the DL channel number. The channel number must be valid for the operating band, for
		dependencies see 'Operating Bands'. The related UL channel number is calculated and set automatically. For scenarios with
		multi-carrier, the channel numbers of the other carriers are calculated and set as well. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:CARRier<Carrier>:DL?', self.__class__.GetStruct())
