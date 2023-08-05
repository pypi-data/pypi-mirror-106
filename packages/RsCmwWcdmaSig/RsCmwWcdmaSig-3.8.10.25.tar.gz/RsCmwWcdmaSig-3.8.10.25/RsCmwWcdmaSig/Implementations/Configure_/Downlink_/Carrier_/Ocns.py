from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocns:
	"""Ocns commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ocns", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.OcnsChannelType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:OCNS:TYPE \n
		Snippet: value: enums.OcnsChannelType = driver.configure.downlink.carrier.ocns.get_type_py() \n
		Selects the type of OCNS channels to be generated, see 'Orthogonal Channel Noise Simulator (OCNS) '. You can select the
		type manually or use the automatic mode. \n
			:return: type_py: R99 | R5 | R6 | R7 | AUTO
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:OCNS:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.OcnsChannelType)

	def set_type_py(self, type_py: enums.OcnsChannelType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:OCNS:TYPE \n
		Snippet: driver.configure.downlink.carrier.ocns.set_type_py(type_py = enums.OcnsChannelType.AUTO) \n
		Selects the type of OCNS channels to be generated, see 'Orthogonal Channel Noise Simulator (OCNS) '. You can select the
		type manually or use the automatic mode. \n
			:param type_py: R99 | R5 | R6 | R7 | AUTO
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(type_py, enums.OcnsChannelType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:OCNS:TYPE {param}')

	def get_level(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CARRier<carrier>:OCNS:LEVel \n
		Snippet: value: float = driver.configure.downlink.carrier.ocns.get_level() \n
		Queries the total OCNS channel power (relative to the base level of the generator) . If no OCNS channels are present, INV
		is returned. \n
			:return: level: Range: -99 dB to 0 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CARRier<Carrier>:OCNS:LEVel?')
		return Conversions.str_to_float(response)
