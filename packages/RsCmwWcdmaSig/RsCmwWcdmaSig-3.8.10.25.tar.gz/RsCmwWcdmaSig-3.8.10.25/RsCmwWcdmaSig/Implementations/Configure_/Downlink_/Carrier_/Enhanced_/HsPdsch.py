from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsPdsch:
	"""HsPdsch commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsPdsch", core, parent)

	# noinspection PyTypeChecker
	def get_us_frames(self) -> enums.UnscheduledTransType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSPDsch:USFRames \n
		Snippet: value: enums.UnscheduledTransType = driver.configure.downlink.carrier.enhanced.hsPdsch.get_us_frames() \n
		Defines the transmission in unscheduled HS-DSCH subframes. \n
			:return: type_py: DUMMy | DTX DUMMy: maintain the HS-DSCH power by sending dummy data DTX: switch off the output power
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSPDsch:USFRames?')
		return Conversions.str_to_scalar_enum(response, enums.UnscheduledTransType)

	def set_us_frames(self, type_py: enums.UnscheduledTransType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSPDsch:USFRames \n
		Snippet: driver.configure.downlink.carrier.enhanced.hsPdsch.set_us_frames(type_py = enums.UnscheduledTransType.DTX) \n
		Defines the transmission in unscheduled HS-DSCH subframes. \n
			:param type_py: DUMMy | DTX DUMMy: maintain the HS-DSCH power by sending dummy data DTX: switch off the output power
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(type_py, enums.UnscheduledTransType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSPDsch:USFRames {param}')

	# noinspection PyTypeChecker
	class PoffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Control: enums.AutoManualMode: AUTO | MANual AUTO: The correct value Γ is calculated automatically. MANual: The value Γ is set manually via the parameter PwrOffsetManual.
			- Pwr_Offset_Manual: float: Range: -6 dB to 13 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Control', enums.AutoManualMode),
			ArgStruct.scalar_float('Pwr_Offset_Manual')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Control: enums.AutoManualMode = None
			self.Pwr_Offset_Manual: float = None

	# noinspection PyTypeChecker
	def get_poffset(self) -> PoffsetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSPDsch:POFFset \n
		Snippet: value: PoffsetStruct = driver.configure.downlink.carrier.enhanced.hsPdsch.get_poffset() \n
		Selects whether the measurement power offset Γ is set manually or calculated automatically. Optionally a second parameter
		can be sent to modify the manual power offset value. It is not relevant for automatic calculation. \n
			:return: structure: for return value, see the help for PoffsetStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSPDsch:POFFset?', self.__class__.PoffsetStruct())

	def set_poffset(self, value: PoffsetStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSPDsch:POFFset \n
		Snippet: driver.configure.downlink.carrier.enhanced.hsPdsch.set_poffset(value = PoffsetStruct()) \n
		Selects whether the measurement power offset Γ is set manually or calculated automatically. Optionally a second parameter
		can be sent to modify the manual power offset value. It is not relevant for automatic calculation. \n
			:param value: see the help for PoffsetStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSPDsch:POFFset', value)
