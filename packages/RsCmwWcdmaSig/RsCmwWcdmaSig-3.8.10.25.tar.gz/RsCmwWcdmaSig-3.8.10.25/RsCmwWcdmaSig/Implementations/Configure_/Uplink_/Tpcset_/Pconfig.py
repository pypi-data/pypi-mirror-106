from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconfig:
	"""Pconfig commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pconfig", core, parent)

	def get_tsef(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSEF \n
		Snippet: value: int = driver.configure.uplink.tpcset.pconfig.get_tsef() \n
		Defines the number of 0 bits to be sent before the all 1 pattern is started for TPC setup 'TPC Test Step EF'. \n
			:return: length: Range: 100 to 170
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSEF?')
		return Conversions.str_to_int(response)

	def set_tsef(self, length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSEF \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_tsef(length = 1) \n
		Defines the number of 0 bits to be sent before the all 1 pattern is started for TPC setup 'TPC Test Step EF'. \n
			:param length: Range: 100 to 170
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSEF {param}')

	def get_tsgh(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSGH \n
		Snippet: value: int = driver.configure.uplink.tpcset.pconfig.get_tsgh() \n
		Defines the number of 0 bits to be sent before the all 1 pattern is started for TPC setup 'TPC Test Step GH'. \n
			:return: length: Range: 60 to 170
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSGH?')
		return Conversions.str_to_int(response)

	def set_tsgh(self, length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSGH \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_tsgh(length = 1) \n
		Defines the number of 0 bits to be sent before the all 1 pattern is started for TPC setup 'TPC Test Step GH'. \n
			:param length: Range: 60 to 170
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSGH {param}')

	def get_ts_segment(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSSegment \n
		Snippet: value: bool = driver.configure.uplink.tpcset.pconfig.get_ts_segment() \n
		Enables or disables segmentation for test steps E, F, G and H. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSSegment?')
		return Conversions.str_to_bool(response)

	def set_ts_segment(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:TSSegment \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_ts_segment(enable = False) \n
		Enables or disables segmentation for test steps E, F, G and H. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:TSSegment {param}')

	def get_phdown(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:PHDown \n
		Snippet: value: int = driver.configure.uplink.tpcset.pconfig.get_phdown() \n
		Define the number of times the pattern has to be repeated for 'Phase Discontinuity Up/Down'. \n
			:return: repetition: Range: 1 to 13
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:PHDown?')
		return Conversions.str_to_int(response)

	def set_phdown(self, repetition: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:PHDown \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_phdown(repetition = 1) \n
		Define the number of times the pattern has to be repeated for 'Phase Discontinuity Up/Down'. \n
			:param repetition: Range: 1 to 13
		"""
		param = Conversions.decimal_value_to_str(repetition)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:PHDown {param}')

	def get_phup(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:PHUP \n
		Snippet: value: int = driver.configure.uplink.tpcset.pconfig.get_phup() \n
		Define the number of times the pattern has to be repeated for 'Phase Discontinuity Up/Down'. \n
			:return: repetition: Range: 1 to 13
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:PHUP?')
		return Conversions.str_to_int(response)

	def set_phup(self, repetition: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:PHUP \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_phup(repetition = 1) \n
		Define the number of times the pattern has to be repeated for 'Phase Discontinuity Up/Down'. \n
			:param repetition: Range: 1 to 13
		"""
		param = Conversions.decimal_value_to_str(repetition)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:PHUP {param}')

	# noinspection PyTypeChecker
	class DhibStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Config: enums.PatternType: UD | DU UD: pattern for the carrier 1 starts: 11 (up) , carrier 2: 00 (down) DU: carrier 1 starts: 00 (down) , carrier 2: 11 (up)
			- Repetition: int: The number of times the pattern is repeated for each carrier. Range: 1 to 20"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Config', enums.PatternType),
			ArgStruct.scalar_int('Repetition')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Config: enums.PatternType = None
			self.Repetition: int = None

	# noinspection PyTypeChecker
	def get_dhib(self) -> DhibStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:DHIB \n
		Snippet: value: DhibStruct = driver.configure.uplink.tpcset.pconfig.get_dhib() \n
		Defines the beginning of the pattern and the number of times the pattern has to be repeated for 'DC HSPA In-Band
		Emission'. \n
			:return: structure: for return value, see the help for DhibStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:DHIB?', self.__class__.DhibStruct())

	def set_dhib(self, value: DhibStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PCONfig:DHIB \n
		Snippet: driver.configure.uplink.tpcset.pconfig.set_dhib(value = DhibStruct()) \n
		Defines the beginning of the pattern and the number of times the pattern has to be repeated for 'DC HSPA In-Band
		Emission'. \n
			:param value: see the help for DhibStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PCONfig:DHIB', value)
