from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IhMobility:
	"""IhMobility commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ihMobility", core, parent)

	# noinspection PyTypeChecker
	def get_handover(self) -> enums.Handover:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IHMobility:HANDover \n
		Snippet: value: enums.Handover = driver.configure.ihMobility.get_handover() \n
		Selects the connection type to be used for an inter-RAT incoming handover in the WCDMA signaling as a handover
		destination. \n
			:return: handover: VOICe | PACKet | TM CS voice, PS data end-to-end or test mode connection.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:IHMobility:HANDover?')
		return Conversions.str_to_scalar_enum(response, enums.Handover)

	def set_handover(self, handover: enums.Handover) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IHMobility:HANDover \n
		Snippet: driver.configure.ihMobility.set_handover(handover = enums.Handover.PACKet) \n
		Selects the connection type to be used for an inter-RAT incoming handover in the WCDMA signaling as a handover
		destination. \n
			:param handover: VOICe | PACKet | TM CS voice, PS data end-to-end or test mode connection.
		"""
		param = Conversions.enum_scalar_to_str(handover, enums.Handover)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:IHMobility:HANDover {param}')

	# noinspection PyTypeChecker
	def get_mtcs(self) -> enums.CsFallbackConnectionType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IHMobility:MTCS \n
		Snippet: value: enums.CsFallbackConnectionType = driver.configure.ihMobility.get_mtcs() \n
		Selects the connection type to be used for an inter-RAT incoming mobile terminated CS fallback. \n
			:return: type_py: VOICe | TMRMc Voice or test mode RMC connection
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:IHMobility:MTCS?')
		return Conversions.str_to_scalar_enum(response, enums.CsFallbackConnectionType)

	def set_mtcs(self, type_py: enums.CsFallbackConnectionType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IHMobility:MTCS \n
		Snippet: driver.configure.ihMobility.set_mtcs(type_py = enums.CsFallbackConnectionType.TMRMc) \n
		Selects the connection type to be used for an inter-RAT incoming mobile terminated CS fallback. \n
			:param type_py: VOICe | TMRMc Voice or test mode RMC connection
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.CsFallbackConnectionType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:IHMobility:MTCS {param}')
