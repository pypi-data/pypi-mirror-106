from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aich:
	"""Aich commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aich", core, parent)

	# noinspection PyTypeChecker
	def get_acknowledge(self) -> enums.SlopeType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:AICH:ACKNowledge \n
		Snippet: value: enums.SlopeType = driver.configure.downlink.enhanced.aich.get_acknowledge() \n
		Defines how the R&S CMW acknowledges RACH preambles received from the UE. \n
			:return: acknowledge: POSitive | NEGative POSitive: The R&S CMW acknowledges or negatively acknowledges the preambles appropriately. NEGative: The R&S CMW always responds with negative acknowledgements.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:AICH:ACKNowledge?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)

	def set_acknowledge(self, acknowledge: enums.SlopeType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:AICH:ACKNowledge \n
		Snippet: driver.configure.downlink.enhanced.aich.set_acknowledge(acknowledge = enums.SlopeType.NEGative) \n
		Defines how the R&S CMW acknowledges RACH preambles received from the UE. \n
			:param acknowledge: POSitive | NEGative POSitive: The R&S CMW acknowledges or negatively acknowledges the preambles appropriately. NEGative: The R&S CMW always responds with negative acknowledgements.
		"""
		param = Conversions.enum_scalar_to_str(acknowledge, enums.SlopeType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:AICH:ACKNowledge {param}')

	def get_ttiming(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:AICH:TTIMing \n
		Snippet: value: float = driver.configure.downlink.enhanced.aich.get_ttiming() \n
		Defines the minimum allowed time delay between two consecutive RACH preambles. \n
			:return: transm_timing: Minimum time delay Range: 3 slots to 4 slots
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:AICH:TTIMing?')
		return Conversions.str_to_float(response)

	def set_ttiming(self, transm_timing: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:AICH:TTIMing \n
		Snippet: driver.configure.downlink.enhanced.aich.set_ttiming(transm_timing = 1.0) \n
		Defines the minimum allowed time delay between two consecutive RACH preambles. \n
			:param transm_timing: Minimum time delay Range: 3 slots to 4 slots
		"""
		param = Conversions.decimal_value_to_str(transm_timing)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:AICH:TTIMing {param}')
