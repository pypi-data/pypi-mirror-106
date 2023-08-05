from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btfd:
	"""Btfd commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("btfd", core, parent)

	# noinspection PyTypeChecker
	def get_tformat(self) -> enums.BtfdDataRate:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:BTFD:TFORmat \n
		Snippet: value: enums.BtfdDataRate = driver.configure.connection.tmode.btfd.get_tformat() \n
		Selects the downlink bit rate for BTFD RMCs. \n
			:return: data_rate: R1K95 | R4K75 | R5K15 | R5K9 | R6K7 | R7K4 | R7K95 | R10K2 | R12K2 Data rate in kbit/s: 1.95, 4.75, 5.15, 5.9, 6.7, 7.4, 7.95, 10.2, 12.2
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:BTFD:TFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.BtfdDataRate)

	def set_tformat(self, data_rate: enums.BtfdDataRate) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:TMODe:BTFD:TFORmat \n
		Snippet: driver.configure.connection.tmode.btfd.set_tformat(data_rate = enums.BtfdDataRate.R10K2) \n
		Selects the downlink bit rate for BTFD RMCs. \n
			:param data_rate: R1K95 | R4K75 | R5K15 | R5K9 | R6K7 | R7K4 | R7K95 | R10K2 | R12K2 Data rate in kbit/s: 1.95, 4.75, 5.15, 5.9, 6.7, 7.4, 7.95, 10.2, 12.2
		"""
		param = Conversions.enum_scalar_to_str(data_rate, enums.BtfdDataRate)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:TMODe:BTFD:TFORmat {param}')
