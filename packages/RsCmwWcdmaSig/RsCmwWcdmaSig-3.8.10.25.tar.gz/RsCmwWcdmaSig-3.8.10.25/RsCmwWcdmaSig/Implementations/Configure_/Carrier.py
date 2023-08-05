from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	# noinspection PyTypeChecker
	def get_band(self) -> enums.OperationBand:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CARRier<carrier>:BAND \n
		Snippet: value: enums.OperationBand = driver.configure.carrier.get_band() \n
		Selects the operating band (OB) . In single-band scenarios, all carriers use the same band. If you change it for one
		carrier, it is also changed for the other carriers. \n
			:return: operation_band: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OB32 | OBS1 | ... | OBS3 | OBL1 | UDEFined OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OB32: operating band XXXII (restricted to dual band scenarios) OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L UDEFined: user defined
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CARRier<Carrier>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.OperationBand)

	def set_band(self, operation_band: enums.OperationBand) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CARRier<carrier>:BAND \n
		Snippet: driver.configure.carrier.set_band(operation_band = enums.OperationBand.OB1) \n
		Selects the operating band (OB) . In single-band scenarios, all carriers use the same band. If you change it for one
		carrier, it is also changed for the other carriers. \n
			:param operation_band: OB1 | ... | OB14 | OB19 | ... | OB22 | OB25 | OB26 | OB32 | OBS1 | ... | OBS3 | OBL1 | UDEFined OB1, ..., OB14: operating band I to XIV OB19, ..., OB22: operating band XIX to XXII OB25, OB26: operating band XXV, XXVI OB32: operating band XXXII (restricted to dual band scenarios) OBS1: operating band S OBS2: operating band S 170 MHz OBS3: operating band S 190 MHz OBL1: operating band L UDEFined: user defined
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(operation_band, enums.OperationBand)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CARRier<Carrier>:BAND {param}')
