from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ctch:
	"""Ctch commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ctch", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:ENABle \n
		Snippet: value: bool = driver.configure.cbs.ctch.get_enable() \n
		Enables CBS generally. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:ENABle \n
		Snippet: driver.configure.cbs.ctch.set_enable(enable = False) \n
		Enables CBS generally. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:ENABle {param}')

	def get_period(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:PERiod \n
		Snippet: value: int = driver.configure.cbs.ctch.get_period() \n
		Specifies the periodicity of CTCH allocation within S-CCPCH. \n
			:return: period: Duration of period (N) Range: 1 to 256, Unit: frames
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:PERiod?')
		return Conversions.str_to_int(response)

	def set_period(self, period: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:PERiod \n
		Snippet: driver.configure.cbs.ctch.set_period(period = 1) \n
		Specifies the periodicity of CTCH allocation within S-CCPCH. \n
			:param period: Duration of period (N) Range: 1 to 256, Unit: frames
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:PERiod {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:FOFFset \n
		Snippet: value: int = driver.configure.cbs.ctch.get_foffset() \n
		Offset (K) used for CTCH allocation within CTCH allocation period N, see method RsCmwWcdmaSig.Configure.Cbs.Ctch.period. \n
			:return: frame_offset: The S-CCPCH TTI number, with the first CTCH allocated for cell broadcast. Range: 0 to N-1, Unit: frames
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, frame_offset: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:FOFFset \n
		Snippet: driver.configure.cbs.ctch.set_foffset(frame_offset = 1) \n
		Offset (K) used for CTCH allocation within CTCH allocation period N, see method RsCmwWcdmaSig.Configure.Cbs.Ctch.period. \n
			:param frame_offset: The S-CCPCH TTI number, with the first CTCH allocated for cell broadcast. Range: 0 to N-1, Unit: frames
		"""
		param = Conversions.decimal_value_to_str(frame_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_fmp_length(self) -> enums.TtiExtended:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:FMPLength \n
		Snippet: value: enums.TtiExtended = driver.configure.cbs.ctch.get_fmp_length() \n
		No command help available \n
			:return: tti: No help available
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:FMPLength?')
		return Conversions.str_to_scalar_enum(response, enums.TtiExtended)

	def set_fmp_length(self, tti: enums.TtiExtended) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:CTCH:FMPLength \n
		Snippet: driver.configure.cbs.ctch.set_fmp_length(tti = enums.TtiExtended.M10) \n
		No command help available \n
			:param tti: No help available
		"""
		param = Conversions.enum_scalar_to_str(tti, enums.TtiExtended)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:CTCH:FMPLength {param}')
