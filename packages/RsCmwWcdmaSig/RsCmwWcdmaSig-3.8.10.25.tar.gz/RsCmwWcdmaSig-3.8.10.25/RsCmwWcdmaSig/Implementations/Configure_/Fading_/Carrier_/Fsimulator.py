from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsimulator:
	"""Fsimulator commands group definition. 9 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fsimulator", core, parent)

	@property
	def globale(self):
		"""globale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globale'):
			from .Fsimulator_.Globale import Globale
			self._globale = Globale(self._core, self._base)
		return self._globale

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_restart'):
			from .Fsimulator_.Restart import Restart
			self._restart = Restart(self._core, self._base)
		return self._restart

	@property
	def iloss(self):
		"""iloss commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_iloss'):
			from .Fsimulator_.Iloss import Iloss
			self._iloss = Iloss(self._core, self._base)
		return self._iloss

	@property
	def dshift(self):
		"""dshift commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dshift'):
			from .Fsimulator_.Dshift import Dshift
			self._dshift = Dshift(self._core, self._base)
		return self._dshift

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ENABle \n
		Snippet: value: bool = driver.configure.fading.carrier.fsimulator.get_enable() \n
		Enables/disables the fading simulator. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:ENABle \n
		Snippet: driver.configure.fading.carrier.fsimulator.set_enable(enable = False) \n
		Enables/disables the fading simulator. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:ENABle {param}')

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.FadingStandard:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:STANdard \n
		Snippet: value: enums.FadingStandard = driver.configure.fading.carrier.fsimulator.get_standard() \n
		Selects one of the propagation conditions defined in the annex B.2 of 3GPP TS 25.101. \n
			:return: standard: C1 | C2 | C3 | C4 | C5 | C6 | C8 | PA3 | PB3 | VA3 | VA30 | VA12 | MPRopagation | BDEath | HST C1 to C6: case 1 to case 6 (multipath fading profile) C8: case 8 (for CQI test in multipath fading and HS-SCCH-less demodulation of HS-DSCH) PA3 | PB3: ITU PA3 / PB3 (multipath fading profile) VA3 | VA30 | VA12: ITU VA3 / VA30 / VA120 (multipath fading profile) MPRopagation: moving propagation BDEath: birth-death propagation HST: high-speed train
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.FadingStandard)

	def set_standard(self, standard: enums.FadingStandard) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:FADing:CARRier<carrier>:FSIMulator:STANdard \n
		Snippet: driver.configure.fading.carrier.fsimulator.set_standard(standard = enums.FadingStandard.B261) \n
		Selects one of the propagation conditions defined in the annex B.2 of 3GPP TS 25.101. \n
			:param standard: C1 | C2 | C3 | C4 | C5 | C6 | C8 | PA3 | PB3 | VA3 | VA30 | VA12 | MPRopagation | BDEath | HST C1 to C6: case 1 to case 6 (multipath fading profile) C8: case 8 (for CQI test in multipath fading and HS-SCCH-less demodulation of HS-DSCH) PA3 | PB3: ITU PA3 / PB3 (multipath fading profile) VA3 | VA30 | VA12: ITU VA3 / VA30 / VA120 (multipath fading profile) MPRopagation: moving propagation BDEath: birth-death propagation HST: high-speed train
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(standard, enums.FadingStandard)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:FADing:CARRier<Carrier>:FSIMulator:STANdard {param}')

	def clone(self) -> 'Fsimulator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fsimulator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
