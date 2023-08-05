from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeIdentity:
	"""UeIdentity commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueIdentity", core, parent)

	def get_filter_py(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:FILTer \n
		Snippet: value: bool = driver.configure.cell.ueIdentity.get_filter_py() \n
		If enabled, the R&S CMW allows only the default IMSI to execute location update and attach. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:FILTer?')
		return Conversions.str_to_bool(response)

	def set_filter_py(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:FILTer \n
		Snippet: driver.configure.cell.ueIdentity.set_filter_py(enable = False) \n
		If enabled, the R&S CMW allows only the default IMSI to execute location update and attach. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:FILTer {param}')

	def get_imsi(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:IMSI \n
		Snippet: value: str = driver.configure.cell.ueIdentity.get_imsi() \n
		Specifies the default IMSI that the instrument can use before the UE is registered. \n
			:return: value: String value, containing 15 digits.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:IMSI?')
		return trim_str_response(response)

	def set_imsi(self, value: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:IMSI \n
		Snippet: driver.configure.cell.ueIdentity.set_imsi(value = '1') \n
		Specifies the default IMSI that the instrument can use before the UE is registered. \n
			:param value: String value, containing 15 digits.
		"""
		param = Conversions.value_to_quoted_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:IMSI {param}')

	# noinspection PyTypeChecker
	def get_use(self) -> enums.Enable:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:USE \n
		Snippet: value: enums.Enable = driver.configure.cell.ueIdentity.get_use() \n
		Specifies whether the default IMSI is used. The default IMSI is defined via method RsCmwWcdmaSig.Configure.Cell.
		UeIdentity.imsi. You can only enable the default IMSI but not disable it. Instead it is disabled automatically when
		registration is performed with a different IMSI. \n
			:return: enable: ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:USE?')
		return Conversions.str_to_scalar_enum(response, enums.Enable)

	def set_use(self, enable: enums.Enable) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:UEIDentity:USE \n
		Snippet: driver.configure.cell.ueIdentity.set_use(enable = enums.Enable.ON) \n
		Specifies whether the default IMSI is used. The default IMSI is defined via method RsCmwWcdmaSig.Configure.Cell.
		UeIdentity.imsi. You can only enable the default IMSI but not disable it. Instead it is disabled automatically when
		registration is performed with a different IMSI. \n
			:param enable: ON
		"""
		param = Conversions.enum_scalar_to_str(enable, enums.Enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:UEIDentity:USE {param}')
