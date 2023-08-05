from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UepClass:
	"""UepClass commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uepClass", core, parent)

	def get_reported(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:UEPClass:REPorted \n
		Snippet: value: bool = driver.configure.uplink.uepClass.get_reported() \n
		Enable or disable usage of the UE power class value reported by the UE. When disabled, the power class value must be set
		manually, see method RsCmwWcdmaSig.Configure.Uplink.UepClass.manual. The manually set value is also used if no reported
		value is available. \n
			:return: use_reported: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:UEPClass:REPorted?')
		return Conversions.str_to_bool(response)

	def set_reported(self, use_reported: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:UEPClass:REPorted \n
		Snippet: driver.configure.uplink.uepClass.set_reported(use_reported = False) \n
		Enable or disable usage of the UE power class value reported by the UE. When disabled, the power class value must be set
		manually, see method RsCmwWcdmaSig.Configure.Uplink.UepClass.manual. The manually set value is also used if no reported
		value is available. \n
			:param use_reported: OFF | ON
		"""
		param = Conversions.bool_to_str(use_reported)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:UEPClass:REPorted {param}')

	# noinspection PyTypeChecker
	def get_manual(self) -> enums.UePowerClass:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:UEPClass:MANual \n
		Snippet: value: enums.UePowerClass = driver.configure.uplink.uepClass.get_manual() \n
		Configures the UE power class value to be used by the R&S CMW if no reported value is available or usage of the reported
		value is disabled, see method RsCmwWcdmaSig.Configure.Uplink.UepClass.reported. \n
			:return: ue_power_class: PC1 | PC2 | PC3 | PC3B | PC4 Power class 1, 2, 3, 3bis, 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:UEPClass:MANual?')
		return Conversions.str_to_scalar_enum(response, enums.UePowerClass)

	def set_manual(self, ue_power_class: enums.UePowerClass) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:UEPClass:MANual \n
		Snippet: driver.configure.uplink.uepClass.set_manual(ue_power_class = enums.UePowerClass.PC1) \n
		Configures the UE power class value to be used by the R&S CMW if no reported value is available or usage of the reported
		value is disabled, see method RsCmwWcdmaSig.Configure.Uplink.UepClass.reported. \n
			:param ue_power_class: PC1 | PC2 | PC3 | PC3B | PC4 Power class 1, 2, 3, 3bis, 4
		"""
		param = Conversions.enum_scalar_to_str(ue_power_class, enums.UePowerClass)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:UEPClass:MANual {param}')
