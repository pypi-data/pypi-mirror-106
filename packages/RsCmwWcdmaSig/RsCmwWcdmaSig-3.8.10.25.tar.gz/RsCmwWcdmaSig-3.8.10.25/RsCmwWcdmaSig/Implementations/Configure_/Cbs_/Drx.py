from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drx:
	"""Drx commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drx", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:ENABle \n
		Snippet: value: bool = driver.configure.cbs.drx.get_enable() \n
		Enables DRX for CBS. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:ENABle \n
		Snippet: driver.configure.cbs.drx.set_enable(enable = False) \n
		Enables DRX for CBS. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:ENABle {param}')

	def get_period(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:PERiod \n
		Snippet: value: int or bool = driver.configure.cbs.drx.get_period() \n
		Specifies the periodicity of DRX the UE can use for the processing of the CB message. \n
			:return: period: Duration of period (P) Range: 1 to 256, Unit: TTIs Additional OFF | ON disables | enables the DRX period
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:PERiod?')
		return Conversions.str_to_int_or_bool(response)

	def set_period(self, period: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:PERiod \n
		Snippet: driver.configure.cbs.drx.set_period(period = 1) \n
		Specifies the periodicity of DRX the UE can use for the processing of the CB message. \n
			:param period: Duration of period (P) Range: 1 to 256, Unit: TTIs Additional OFF | ON disables | enables the DRX period
		"""
		param = Conversions.decimal_or_bool_value_to_str(period)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:PERiod {param}')

	def get_length(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:LENGth \n
		Snippet: value: int = driver.configure.cbs.drx.get_length() \n
		Specifies the length of DRX (L) that the UE can use for the processing of particular CB message. P denotes the period of
		scheduling message, see method RsCmwWcdmaSig.Configure.Cbs.Drx.period. Define value matching with the position of the
		specific CB message within the CBS scheduling period. \n
			:return: length_of_period: Range: 1 TTI to P-1 TTIs, Unit: TTI
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, length_of_period: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:LENGth \n
		Snippet: driver.configure.cbs.drx.set_length(length_of_period = 1) \n
		Specifies the length of DRX (L) that the UE can use for the processing of particular CB message. P denotes the period of
		scheduling message, see method RsCmwWcdmaSig.Configure.Cbs.Drx.period. Define value matching with the position of the
		specific CB message within the CBS scheduling period. \n
			:param length_of_period: Range: 1 TTI to P-1 TTIs, Unit: TTI
		"""
		param = Conversions.decimal_value_to_str(length_of_period)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:LENGth {param}')

	def get_offset(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:OFFSet \n
		Snippet: value: int = driver.configure.cbs.drx.get_offset() \n
		Offset (O) within period of scheduling message (P) . This offset is used for the transmission of a scheduling message.
		See also: method RsCmwWcdmaSig.Configure.Cbs.Drx.period. \n
			:return: offset: Range: 1 TTI to P-1 TTIs, Unit: TTI
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, offset: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:OFFSet \n
		Snippet: driver.configure.cbs.drx.set_offset(offset = 1) \n
		Offset (O) within period of scheduling message (P) . This offset is used for the transmission of a scheduling message.
		See also: method RsCmwWcdmaSig.Configure.Cbs.Drx.period. \n
			:param offset: Range: 1 TTI to P-1 TTIs, Unit: TTI
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:OFFSet {param}')

	def get_fempty(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:FEMPty \n
		Snippet: value: bool = driver.configure.cbs.drx.get_fempty() \n
		Specifies the handling of unused CTCH TTIs allocated for CBS. \n
			:return: enable: OFF | ON OFF: no action for unused CTCH ON: fill unused CTCH with scheduling message
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:FEMPty?')
		return Conversions.str_to_bool(response)

	def set_fempty(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CBS:DRX:FEMPty \n
		Snippet: driver.configure.cbs.drx.set_fempty(enable = False) \n
		Specifies the handling of unused CTCH TTIs allocated for CBS. \n
			:param enable: OFF | ON OFF: no action for unused CTCH ON: fill unused CTCH with scheduling message
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CBS:DRX:FEMPty {param}')
