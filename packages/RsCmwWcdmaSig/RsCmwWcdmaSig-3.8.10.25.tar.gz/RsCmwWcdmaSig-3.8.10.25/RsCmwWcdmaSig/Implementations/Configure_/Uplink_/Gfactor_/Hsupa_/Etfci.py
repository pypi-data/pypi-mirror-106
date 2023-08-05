from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Etfci:
	"""Etfci commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("etfci", core, parent)

	def get_poffset(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:POFFset \n
		Snippet: value: List[int] = driver.configure.uplink.gfactor.hsupa.etfci.get_poffset() \n
		Specifies the power offset values of the first n pairs of reference E-TFCIs and power offsets, with n = 1 to 8. \n
			:return: power_offset: Comma-separated list of up to 8 values (30 and 31 reserved for E-TFCI boost) Range: 0 to 31
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:POFFset?')
		return response

	def set_poffset(self, power_offset: List[int]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:POFFset \n
		Snippet: driver.configure.uplink.gfactor.hsupa.etfci.set_poffset(power_offset = [1, 2, 3]) \n
		Specifies the power offset values of the first n pairs of reference E-TFCIs and power offsets, with n = 1 to 8. \n
			:param power_offset: Comma-separated list of up to 8 values (30 and 31 reserved for E-TFCI boost) Range: 0 to 31
		"""
		param = Conversions.list_to_csv_str(power_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:POFFset {param}')

	def get_reference(self) -> List[int]:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:REFerence \n
		Snippet: value: List[int] = driver.configure.uplink.gfactor.hsupa.etfci.get_reference() \n
		Specifies the E-TFCI values of the first n pairs of reference E-TFCIs and power offsets, with n = 1 to 8. \n
			:return: etfci: Comma-separated list of up to 8 values Range: 0 to 127
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:REFerence?')
		return response

	def set_reference(self, etfci: List[int]) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:REFerence \n
		Snippet: driver.configure.uplink.gfactor.hsupa.etfci.set_reference(etfci = [1, 2, 3]) \n
		Specifies the E-TFCI values of the first n pairs of reference E-TFCIs and power offsets, with n = 1 to 8. \n
			:param etfci: Comma-separated list of up to 8 values Range: 0 to 127
		"""
		param = Conversions.list_to_csv_str(etfci)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:REFerence {param}')

	def get_number(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:NUMBer \n
		Snippet: value: int = driver.configure.uplink.gfactor.hsupa.etfci.get_number() \n
		Specifies how many pairs of reference E-TFCIs and assigned power offset values are signaled to the UE. \n
			:return: number: Range: 1 to 8
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:NUMBer \n
		Snippet: driver.configure.uplink.gfactor.hsupa.etfci.set_number(number = 1) \n
		Specifies how many pairs of reference E-TFCIs and assigned power offset values are signaled to the UE. \n
			:param number: Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:NUMBer {param}')

	def get_boost(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:BOOSt \n
		Snippet: value: int or bool = driver.configure.uplink.gfactor.hsupa.etfci.get_boost() \n
		Specifies the E-TFCI threshold beyond which boosting of E-DPCCH is enabled. \n
			:return: value: Range: 0 to 127 Additional ON / OFF enables or disables the E-DPCCH power boosting.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:BOOSt?')
		return Conversions.str_to_int_or_bool(response)

	def set_boost(self, value: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:ETFCi:BOOSt \n
		Snippet: driver.configure.uplink.gfactor.hsupa.etfci.set_boost(value = 1) \n
		Specifies the E-TFCI threshold beyond which boosting of E-DPCCH is enabled. \n
			:param value: Range: 0 to 127 Additional ON / OFF enables or disables the E-DPCCH power boosting.
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:ETFCi:BOOSt {param}')
