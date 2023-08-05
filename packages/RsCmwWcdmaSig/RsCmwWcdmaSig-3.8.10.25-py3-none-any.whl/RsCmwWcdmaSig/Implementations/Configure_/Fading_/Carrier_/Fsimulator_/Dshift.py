from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dshift:
	"""Dshift commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dshift", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.InsertLossMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:DSHift:MODE \n
		Snippet: value: enums.InsertLossMode = driver.configure.fading.carrier.fsimulator.dshift.get_mode() \n
		Sets the Doppler shift mode. \n
			:return: mode: NORMal | USER NORMal: the maximum Doppler frequency is determined by the fading profile USER: the maximum Doppler frequency can be adjusted manually
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:DSHift:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InsertLossMode)

	def set_mode(self, mode: enums.InsertLossMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:DSHift:MODE \n
		Snippet: driver.configure.fading.carrier.fsimulator.dshift.set_mode(mode = enums.InsertLossMode.NORMal) \n
		Sets the Doppler shift mode. \n
			:param mode: NORMal | USER NORMal: the maximum Doppler frequency is determined by the fading profile USER: the maximum Doppler frequency can be adjusted manually
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(mode, enums.InsertLossMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:DSHift:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:DSHift \n
		Snippet: value: float = driver.configure.fading.carrier.fsimulator.dshift.get_value() \n
		Displays the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwWcdmaSig.Configure.Fading.Carrier.Fsimulator.Dshift.mode) . \n
			:return: frequency: Range: 1 Hz to 2000 Hz, Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:DSHift?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:DSHift \n
		Snippet: driver.configure.fading.carrier.fsimulator.dshift.set_value(frequency = 1.0) \n
		Displays the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwWcdmaSig.Configure.Fading.Carrier.Fsimulator.Dshift.mode) . \n
			:param frequency: Range: 1 Hz to 2000 Hz, Unit: Hz
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:DSHift {param}')
