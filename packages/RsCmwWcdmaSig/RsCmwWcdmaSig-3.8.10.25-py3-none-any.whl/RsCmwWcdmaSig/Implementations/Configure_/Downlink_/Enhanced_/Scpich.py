from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scpich:
	"""Scpich commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scpich", core, parent)

	def get_phase(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:SCPich:PHASe \n
		Snippet: value: int = driver.configure.downlink.enhanced.scpich.get_phase() \n
		Defines the phase of the S-CPICH in degrees, relative to the P-CPICH phase. \n
			:return: phase: Range: -315 deg to 0 deg, Unit: deg
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:SCPich:PHASe?')
		return Conversions.str_to_int(response)

	def set_phase(self, phase: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:SCPich:PHASe \n
		Snippet: driver.configure.downlink.enhanced.scpich.set_phase(phase = 1) \n
		Defines the phase of the S-CPICH in degrees, relative to the P-CPICH phase. \n
			:param phase: Range: -315 deg to 0 deg, Unit: deg
		"""
		param = Conversions.decimal_value_to_str(phase)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:SCPich:PHASe {param}')

	def get_sscode(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:SCPich:SSCode \n
		Snippet: value: int or bool = driver.configure.downlink.enhanced.scpich.get_sscode() \n
		Defines index k used for calculation of a secondary scrambling code number for the S-CPICH (see also 'Scrambling Codes') .
		If the secondary scrambling code is deactivated, the primary scrambling code is used (see method RsCmwWcdmaSig.Configure.
		Cell.Carrier.scode) . \n
			:return: sec_scramb_code: Range: 1 to 15 Additional parameters: OFF | ON (disables | enables the secondary scrambling code)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:SCPich:SSCode?')
		return Conversions.str_to_int_or_bool(response)

	def set_sscode(self, sec_scramb_code: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:ENHanced:SCPich:SSCode \n
		Snippet: driver.configure.downlink.enhanced.scpich.set_sscode(sec_scramb_code = 1) \n
		Defines index k used for calculation of a secondary scrambling code number for the S-CPICH (see also 'Scrambling Codes') .
		If the secondary scrambling code is deactivated, the primary scrambling code is used (see method RsCmwWcdmaSig.Configure.
		Cell.Carrier.scode) . \n
			:param sec_scramb_code: Range: 1 to 15 Additional parameters: OFF | ON (disables | enables the secondary scrambling code)
		"""
		param = Conversions.decimal_or_bool_value_to_str(sec_scramb_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:ENHanced:SCPich:SSCode {param}')
