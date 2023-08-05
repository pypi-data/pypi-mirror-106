from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpch:
	"""Dpch commands group definition. 8 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpch", core, parent)

	@property
	def lsequence(self):
		"""lsequence commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_lsequence'):
			from .Dpch_.Lsequence import Lsequence
			self._lsequence = Lsequence(self._core, self._base)
		return self._lsequence

	# noinspection PyTypeChecker
	def get_rxl_strategy(self) -> enums.PowerStrategy:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:RXLStrategy \n
		Snippet: value: enums.PowerStrategy = driver.configure.downlink.enhanced.dpch.get_rxl_strategy() \n
		Specifies the algorithm for generated power DPCH level in downlink for 'WCDMA Out-Of-Sync Handling Measurement'. \n
			:return: strategy: AF | BF | CE AF: 'Max A off F Max' BF: 'Max B off F Max' CE: 'Max C off E Max'
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:RXLStrategy?')
		return Conversions.str_to_scalar_enum(response, enums.PowerStrategy)

	def set_rxl_strategy(self, strategy: enums.PowerStrategy) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:RXLStrategy \n
		Snippet: driver.configure.downlink.enhanced.dpch.set_rxl_strategy(strategy = enums.PowerStrategy.AF) \n
		Specifies the algorithm for generated power DPCH level in downlink for 'WCDMA Out-Of-Sync Handling Measurement'. \n
			:param strategy: AF | BF | CE AF: 'Max A off F Max' BF: 'Max B off F Max' CE: 'Max C off E Max'
		"""
		param = Conversions.enum_scalar_to_str(strategy, enums.PowerStrategy)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:RXLStrategy {param}')

	# noinspection PyTypeChecker
	def get_phase(self) -> enums.PhaseReference:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:PHASe \n
		Snippet: value: enums.PhaseReference = driver.configure.downlink.enhanced.dpch.get_phase() \n
		Sets the DPCH phase reference. For the S-CPICH phase shift, see method RsCmwWcdmaSig.Configure.Downlink.Enhanced.Scpich.
		phase. \n
			:return: reference: PCPich | SCPich PCPich: P-CPICH set as reference SCPich: S-CPICH set as reference
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.PhaseReference)

	def set_phase(self, reference: enums.PhaseReference) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:PHASe \n
		Snippet: driver.configure.downlink.enhanced.dpch.set_phase(reference = enums.PhaseReference.PCPich) \n
		Sets the DPCH phase reference. For the S-CPICH phase shift, see method RsCmwWcdmaSig.Configure.Downlink.Enhanced.Scpich.
		phase. \n
			:param reference: PCPich | SCPich PCPich: P-CPICH set as reference SCPich: S-CPICH set as reference
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.PhaseReference)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:PHASe {param}')

	def get_sscode(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:SSCode \n
		Snippet: value: int or bool = driver.configure.downlink.enhanced.dpch.get_sscode() \n
		Defines index k used for calculation of a secondary scrambling code number for the DPCH/F-DPCH (see also 'Scrambling
		Codes') . If the secondary scrambling code is deactivated, the primary scrambling code is used (see method RsCmwWcdmaSig.
		Configure.Cell.Carrier.scode) . \n
			:return: sec_scramb_code: Range: 1 to 15 Additional parameters: OFF | ON (disables | enables the secondary scrambling code)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:SSCode?')
		return Conversions.str_to_int_or_bool(response)

	def set_sscode(self, sec_scramb_code: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:SSCode \n
		Snippet: driver.configure.downlink.enhanced.dpch.set_sscode(sec_scramb_code = 1) \n
		Defines index k used for calculation of a secondary scrambling code number for the DPCH/F-DPCH (see also 'Scrambling
		Codes') . If the secondary scrambling code is deactivated, the primary scrambling code is used (see method RsCmwWcdmaSig.
		Configure.Cell.Carrier.scode) . \n
			:param sec_scramb_code: Range: 1 to 15 Additional parameters: OFF | ON (disables | enables the secondary scrambling code)
		"""
		param = Conversions.decimal_or_bool_value_to_str(sec_scramb_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:SSCode {param}')

	def get_toffset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:TOFFset \n
		Snippet: value: float = driver.configure.downlink.enhanced.dpch.get_toffset() \n
		Defines the offset between the DL P-CCPCH timing and the DL DPCH/F-DPCH timing in multiples of 256 chips (1/10 slot) . \n
			:return: timing_offset: Range: 0 to 149
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:TOFFset?')
		return Conversions.str_to_float(response)

	def set_toffset(self, timing_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:TOFFset \n
		Snippet: driver.configure.downlink.enhanced.dpch.set_toffset(timing_offset = 1.0) \n
		Defines the offset between the DL P-CCPCH timing and the DL DPCH/F-DPCH timing in multiples of 256 chips (1/10 slot) . \n
			:param timing_offset: Range: 0 to 149
		"""
		param = Conversions.decimal_value_to_str(timing_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:TOFFset {param}')

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Level_Min: float: Range: -80 dB to 0 dB, Unit: dB
			- Level_Max: float: Range: -80 dB to 0 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Level_Min'),
			ArgStruct.scalar_float('Level_Max')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Level_Min: float = None
			self.Level_Max: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:RANGe \n
		Snippet: value: RangeStruct = driver.configure.downlink.enhanced.dpch.get_range() \n
		Specifies the allowed range for the variation of the DPDCH/F-DPCH power level relative to the base level Ior. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:RANGe?', self.__class__.RangeStruct())

	def set_range(self, value: RangeStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:DPCH:RANGe \n
		Snippet: driver.configure.downlink.enhanced.dpch.set_range(value = RangeStruct()) \n
		Specifies the allowed range for the variation of the DPDCH/F-DPCH power level relative to the base level Ior. \n
			:param value: see the help for RangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:DPCH:RANGe', value)

	def clone(self) -> 'Dpch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
