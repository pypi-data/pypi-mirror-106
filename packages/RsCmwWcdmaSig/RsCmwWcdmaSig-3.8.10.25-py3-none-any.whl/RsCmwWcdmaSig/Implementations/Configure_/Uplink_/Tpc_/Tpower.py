from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpower:
	"""Tpower commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpower", core, parent)

	def get_offset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:TPOWer:OFFSet \n
		Snippet: value: float = driver.configure.uplink.tpc.tpower.get_offset() \n
		Specifies the difference between the target power levels of carrier one and two. \n
			:return: offset: Range: -10 dB to +10 dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:TPOWer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:TPOWer:OFFSet \n
		Snippet: driver.configure.uplink.tpc.tpower.set_offset(offset = 1.0) \n
		Specifies the difference between the target power levels of carrier one and two. \n
			:param offset: Range: -10 dB to +10 dB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:TPOWer:OFFSet {param}')

	# noinspection PyTypeChecker
	def get_reference(self) -> enums.ClosedLoopPower:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:TPOWer:REFerence \n
		Snippet: value: enums.ClosedLoopPower = driver.configure.uplink.tpc.tpower.get_reference() \n
		Selects the type of the closed loop target power. \n
			:return: reference: TOTal | DPCH TOTal: maximum total uplink power DPCH: maximum DPCH power
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:TPOWer:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.ClosedLoopPower)

	def set_reference(self, reference: enums.ClosedLoopPower) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:TPOWer:REFerence \n
		Snippet: driver.configure.uplink.tpc.tpower.set_reference(reference = enums.ClosedLoopPower.DPCH) \n
		Selects the type of the closed loop target power. \n
			:param reference: TOTal | DPCH TOTal: maximum total uplink power DPCH: maximum DPCH power
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.ClosedLoopPower)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:TPOWer:REFerence {param}')
