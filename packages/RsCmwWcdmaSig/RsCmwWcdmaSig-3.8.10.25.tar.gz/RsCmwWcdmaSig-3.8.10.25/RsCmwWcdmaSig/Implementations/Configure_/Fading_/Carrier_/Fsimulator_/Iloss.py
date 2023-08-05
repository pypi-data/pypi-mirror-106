from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iloss:
	"""Iloss commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iloss", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.InsertLossMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ILOSs:MODE \n
		Snippet: value: enums.InsertLossMode = driver.configure.fading.carrier.fsimulator.iloss.get_mode() \n
		Sets the insertion loss mode. \n
			:return: insert_loss_mode: NORMal | USER NORMal: the insertion loss is determined by the fading profile USER: the insertion loss can be adjusted manually
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ILOSs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InsertLossMode)

	def set_mode(self, insert_loss_mode: enums.InsertLossMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ILOSs:MODE \n
		Snippet: driver.configure.fading.carrier.fsimulator.iloss.set_mode(insert_loss_mode = enums.InsertLossMode.NORMal) \n
		Sets the insertion loss mode. \n
			:param insert_loss_mode: NORMal | USER NORMal: the insertion loss is determined by the fading profile USER: the insertion loss can be adjusted manually
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(insert_loss_mode, enums.InsertLossMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ILOSs:MODE {param}')

	def get_loss(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ILOSs:LOSS \n
		Snippet: value: float = driver.configure.fading.carrier.fsimulator.iloss.get_loss() \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see method RsCmwWcdmaSig.
		Configure.Fading.Carrier.Fsimulator.Iloss.mode) . \n
			:return: insertion_loss: Range: 0 dB to 18 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ILOSs:LOSS?')
		return Conversions.str_to_float(response)

	def set_loss(self, insertion_loss: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ILOSs:LOSS \n
		Snippet: driver.configure.fading.carrier.fsimulator.iloss.set_loss(insertion_loss = 1.0) \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see method RsCmwWcdmaSig.
		Configure.Fading.Carrier.Fsimulator.Iloss.mode) . \n
			:param insertion_loss: Range: 0 dB to 18 dB, Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(insertion_loss)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ILOSs:LOSS {param}')
