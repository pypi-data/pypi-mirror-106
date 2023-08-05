from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 48 total commands, 7 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def uepClass(self):
		"""uepClass commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_uepClass'):
			from .Uplink_.UepClass import UepClass
			self._uepClass = UepClass(self._core, self._base)
		return self._uepClass

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_carrier'):
			from .Uplink_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def olpControl(self):
		"""olpControl commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_olpControl'):
			from .Uplink_.OlpControl import OlpControl
			self._olpControl = OlpControl(self._core, self._base)
		return self._olpControl

	@property
	def prach(self):
		"""prach commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_prach'):
			from .Uplink_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	@property
	def gfactor(self):
		"""gfactor commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_gfactor'):
			from .Uplink_.Gfactor import Gfactor
			self._gfactor = Gfactor(self._core, self._base)
		return self._gfactor

	@property
	def tpc(self):
		"""tpc commands group. 5 Sub-classes, 3 commands."""
		if not hasattr(self, '_tpc'):
			from .Uplink_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	@property
	def tpcset(self):
		"""tpcset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpcset'):
			from .Uplink_.Tpcset import Tpcset
			self._tpcset = Tpcset(self._core, self._base)
		return self._tpcset

	def get_mue_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:MUEPower \n
		Snippet: value: float = driver.configure.uplink.get_mue_power() \n
		Sets the maximum allowed output power of the UE transmitter (averaged over the transmit slot) . \n
			:return: max_ue_power: Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:MUEPower?')
		return Conversions.str_to_float(response)

	def set_mue_power(self, max_ue_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:MUEPower \n
		Snippet: driver.configure.uplink.set_mue_power(max_ue_power = 1.0) \n
		Sets the maximum allowed output power of the UE transmitter (averaged over the transmit slot) . \n
			:param max_ue_power: Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(max_ue_power)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:MUEPower {param}')

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
