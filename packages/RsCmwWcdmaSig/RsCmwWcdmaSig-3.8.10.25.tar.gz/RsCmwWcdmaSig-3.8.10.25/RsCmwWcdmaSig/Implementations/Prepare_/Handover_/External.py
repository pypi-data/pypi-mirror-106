from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("external", core, parent)

	# noinspection PyTypeChecker
	def get_destination(self) -> enums.HoverExtDestination:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: value: enums.HoverExtDestination = driver.prepare.handover.external.get_destination() \n
		Selects the target radio access technology for handover to another instrument. \n
			:return: destination: WCDMa | GSM | LTE | EVDO | CDMA
		"""
		response = self._core.io.query_str('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:DESTination?')
		return Conversions.str_to_scalar_enum(response, enums.HoverExtDestination)

	def set_destination(self, destination: enums.HoverExtDestination) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:DESTination \n
		Snippet: driver.prepare.handover.external.set_destination(destination = enums.HoverExtDestination.CDMA) \n
		Selects the target radio access technology for handover to another instrument. \n
			:param destination: WCDMa | GSM | LTE | EVDO | CDMA
		"""
		param = Conversions.enum_scalar_to_str(destination, enums.HoverExtDestination)
		self._core.io.write(f'PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:DESTination {param}')

	# noinspection PyTypeChecker
	class LteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.LteBand: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB15 | OB16 | OB17 | OB18 | OB19 | OB20 | OB21 | OB22 | OB23 | OB24 | OB25 | OB26 | OB27 | OB28 | OB29 | OB30 | OB31 | OB32 | OB33 | OB34 | OB35 | OB36 | OB37 | OB38 | OB39 | OB40 | OB41 | OB42 | OB43 | OB44 | OB45 | OB46 | OB65 | OB66 | OB67 | OB252 | OB255 Operating band 1 to 46, 65 to 67, 252, 255
			- Dl_Channel: int: Downlink channel number Range: The allowed range depends on the LTE band, see table below."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.LteBand),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.LteBand = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_lte(self) -> LteStruct:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: value: LteStruct = driver.prepare.handover.external.get_lte() \n
		No command help available \n
			:return: structure: for return value, see the help for LteStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:LTE?', self.__class__.LteStruct())

	def set_lte(self, value: LteStruct) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:LTE \n
		Snippet: driver.prepare.handover.external.set_lte(value = LteStruct()) \n
		No command help available \n
			:param value: see the help for LteStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:LTE', value)

	# noinspection PyTypeChecker
	class GsmStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.GsmBand: G04 | G085 | G09 | G18 | G19 GSM 400, GSM 850, GSM 900, GSM 1800, GSM 1900
			- Dl_Channel: int: Channel number used for the broadcast control channel (BCCH) Range: The allowed range depends on the operating band, see table below."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.GsmBand),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.GsmBand = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_gsm(self) -> GsmStruct:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: value: GsmStruct = driver.prepare.handover.external.get_gsm() \n
		Configures the destination parameters for handover to a GSM destination at another instrument. \n
			:return: structure: for return value, see the help for GsmStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:GSM?', self.__class__.GsmStruct())

	def set_gsm(self, value: GsmStruct) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:GSM \n
		Snippet: driver.prepare.handover.external.set_gsm(value = GsmStruct()) \n
		Configures the destination parameters for handover to a GSM destination at another instrument. \n
			:param value: see the help for GsmStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:GSM', value)

	# noinspection PyTypeChecker
	class CdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, 'US-Cellular' KCEL: BC 0, 'Korean Cellular' NAPC: BC 1, 'North American PCS' TACS: BC 2, 'TACS Band' JTAC: BC 3, 'JTACS Band' KPCS: BC 4, 'Korean PCS' N45T: BC 5, 'NMT-450' IM2K: BC 6, 'IMT-2000' NA7C: BC 7, 'Upper 700 MHz' B18M: BC 8, '1800 MHz Band' NA9C: BC 9, 'North American 900 MHz' NA8S: BC 10, 'Secondary 800 MHz' PA4M: BC 11, 'European 400 MHz PAMR' PA8M: BC 12, '800 MHz PAMR' IEXT: BC 13, 'IMT-2000 2.5 GHz Extension' USPC: BC 14, 'US PCS 1900 MHz' AWS: BC 15, 'AWS Band' U25B: BC 16, 'US 2.5 GHz Band' U25F: BC 17, 'US 2.5 GHz Forward' PS7C: BC 18, 'Public Safety Band 700 MHz' LO7C: BC 19, 'Lower 700 MHz'
			- Dl_Channel: int: Channel number Range: 0 to 2108, depending on band class, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_cdma(self) -> CdmaStruct:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: value: CdmaStruct = driver.prepare.handover.external.get_cdma() \n
		Configure the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:return: structure: for return value, see the help for CdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:CDMA?', self.__class__.CdmaStruct())

	def set_cdma(self, value: CdmaStruct) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:CDMA \n
		Snippet: driver.prepare.handover.external.set_cdma(value = CdmaStruct()) \n
		Configure the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:param value: see the help for CdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:CDMA', value)

	# noinspection PyTypeChecker
	class EvdoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band_Class: enums.BandClass: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | NA9C | PS7C | LO7C USC: BC 0, 'US-Cellular' KCEL: BC 0, 'Korean Cellular' NAPC: BC 1, 'North American PCS' TACS: BC 2, 'TACS Band' JTAC: BC 3, 'JTACS Band' KPCS: BC 4, 'Korean PCS' N45T: BC 5, 'NMT-450' IM2K: BC 6, 'IMT-2000' NA7C: BC 7, 'Upper 700 MHz' B18M: BC 8, '1800 MHz Band' NA9C: BC 9, 'North American 900 MHz' NA8S: BC 10, 'Secondary 800 MHz' PA4M: BC 11, 'European 400 MHz PAMR' PA8M: BC 12, '800 MHz PAMR' IEXT: BC 13, 'IMT-2000 2.5 GHz Extension' USPC: BC 14, 'US PCS 1900 MHz' AWS: BC 15, 'AWS Band' U25B: BC 16, 'US 2.5 GHz Band' U25F: BC 17, 'US 2.5 GHz Forward' PS7C: BC 18, 'Public Safety Band 700 MHz' LO7C: BC 19, 'Lower 700 MHz'
			- Dl_Channel: int: Channel number Range: 0 to 2108, depending on band class, see table below"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band_Class', enums.BandClass),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band_Class: enums.BandClass = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_evdo(self) -> EvdoStruct:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: value: EvdoStruct = driver.prepare.handover.external.get_evdo() \n
		Configure the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:return: structure: for return value, see the help for EvdoStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:EVDO?', self.__class__.EvdoStruct())

	def set_evdo(self, value: EvdoStruct) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:EVDO \n
		Snippet: driver.prepare.handover.external.set_evdo(value = EvdoStruct()) \n
		Configure the destination parameters for handover to a CDMA2000 or 1xEV-DO destination at another instrument. \n
			:param value: see the help for EvdoStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:EVDO', value)

	# noinspection PyTypeChecker
	class WcdmaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Band: enums.OperationBand: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OBS1 | ... | OBS3 | OBL1 | UDEFined OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L UDEFined: user defined
			- Dl_Channel: int: For channel number ranges depending on operating bands see Table 'Operating bands for uplink signals'."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Band', enums.OperationBand),
			ArgStruct.scalar_int('Dl_Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Band: enums.OperationBand = None
			self.Dl_Channel: int = None

	# noinspection PyTypeChecker
	def get_wcdma(self) -> WcdmaStruct:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: value: WcdmaStruct = driver.prepare.handover.external.get_wcdma() \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:return: structure: for return value, see the help for WcdmaStruct structure arguments.
		"""
		return self._core.io.query_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:WCDMa?', self.__class__.WcdmaStruct())

	def set_wcdma(self, value: WcdmaStruct) -> None:
		"""SCPI: PREPare:WCDMa:SIGNaling<instance>:HANDover:EXTernal:WCDMa \n
		Snippet: driver.prepare.handover.external.set_wcdma(value = WcdmaStruct()) \n
		Configures the destination parameters for handover to a WCDMA destination at another instrument. \n
			:param value: see the help for WcdmaStruct structure arguments.
		"""
		self._core.io.write_struct('PREPare:WCDMa:SIGNaling<Instance>:HANDover:EXTernal:WCDMa', value)
