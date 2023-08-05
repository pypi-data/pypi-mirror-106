from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsscch:
	"""Hsscch commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsscch", core, parent)

	# noinspection PyTypeChecker
	def get_us_frames(self) -> enums.UnscheduledTransType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:USFRames \n
		Snippet: value: enums.UnscheduledTransType = driver.configure.downlink.carrier.enhanced.hsscch.get_us_frames() \n
		Defines the transmission in unscheduled HS-SCCH subframes. \n
			:return: type_py: DUMMy | DTX DUMMy: maintain HS-SCCH power and transfer dummy UE ID, see method RsCmwWcdmaSig.Configure.Downlink.Carrier.Hsscch.IdDummy.set DTX: switch off output power in unscheduled subframes
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:USFRames?')
		return Conversions.str_to_scalar_enum(response, enums.UnscheduledTransType)

	def set_us_frames(self, type_py: enums.UnscheduledTransType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:USFRames \n
		Snippet: driver.configure.downlink.carrier.enhanced.hsscch.set_us_frames(type_py = enums.UnscheduledTransType.DTX) \n
		Defines the transmission in unscheduled HS-SCCH subframes. \n
			:param type_py: DUMMy | DTX DUMMy: maintain HS-SCCH power and transfer dummy UE ID, see method RsCmwWcdmaSig.Configure.Downlink.Carrier.Hsscch.IdDummy.set DTX: switch off output power in unscheduled subframes
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(type_py, enums.UnscheduledTransType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:USFRames {param}')

	def get_number(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:NUMBer \n
		Snippet: value: int = driver.configure.downlink.carrier.enhanced.hsscch.get_number() \n
		Configures the number of HS-SCCHs contained in the HS-SCCH set. <Number> = n means that the set contains the HS-SCCHs
		number 1 to n. \n
			:return: number: Range: 1 to 4
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:NUMBer \n
		Snippet: driver.configure.downlink.carrier.enhanced.hsscch.set_number(number = 1) \n
		Configures the number of HS-SCCHs contained in the HS-SCCH set. <Number> = n means that the set contains the HS-SCCHs
		number 1 to n. \n
			:param number: Range: 1 to 4
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:NUMBer {param}')

	# noinspection PyTypeChecker
	def get_selection(self) -> enums.HsScchType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:SELection \n
		Snippet: value: enums.HsScchType = driver.configure.downlink.carrier.enhanced.hsscch.get_selection() \n
		Selects the HS-SCCH that carries the UE ID in scheduled subframes. The number <n> used below is set via method
		RsCmwWcdmaSig.Configure.Downlink.Carrier.Enhanced.Hsscch.number. \n
			:return: type_py: CH1 | CH2 | CH3 | CH4 | RANDom | AUTomatic CH1 to CH4: The UE ID is transferred on the selected HS-SCCH. RANDom: The HS-SCCH for each transmission is selected at random among the channels 1 to n. AUTomatic: For a R5 connection, the UE ID is transferred on the HS-SCCH sequence 1, 2,…, n, 1, 2, and so on. For a R7/R8 connection, the UE ID is transferred on the appropriate HS-SCCH automatically selected depending on the used modulation scheme.
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:SELection?')
		return Conversions.str_to_scalar_enum(response, enums.HsScchType)

	def set_selection(self, type_py: enums.HsScchType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:ENHanced:HSSCch:SELection \n
		Snippet: driver.configure.downlink.carrier.enhanced.hsscch.set_selection(type_py = enums.HsScchType.AUTomatic) \n
		Selects the HS-SCCH that carries the UE ID in scheduled subframes. The number <n> used below is set via method
		RsCmwWcdmaSig.Configure.Downlink.Carrier.Enhanced.Hsscch.number. \n
			:param type_py: CH1 | CH2 | CH3 | CH4 | RANDom | AUTomatic CH1 to CH4: The UE ID is transferred on the selected HS-SCCH. RANDom: The HS-SCCH for each transmission is selected at random among the channels 1 to n. AUTomatic: For a R5 connection, the UE ID is transferred on the HS-SCCH sequence 1, 2,…, n, 1, 2, and so on. For a R7/R8 connection, the UE ID is transferred on the appropriate HS-SCCH automatically selected depending on the used modulation scheme.
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(type_py, enums.HsScchType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:ENHanced:HSSCch:SELection {param}')
