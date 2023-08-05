from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def tpc(self):
		"""tpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpc'):
			from .Carrier_.Tpc import Tpc
			self._tpc = Tpc(self._core, self._base)
		return self._tpc

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:POFFset \n
		Snippet: value: float = driver.configure.uplink.carrier.get_poffset() \n
		Sets the DPCCH power offset, used by the UE to calculate the initial DPCCH power for random access. The power offset of
		the carrier two is defined as the power offset between the initial DPCCH power level on UL2 and the current DPCCH power
		level of UL1. \n
			:return: power_offset: Range: -164 dB to -6 dB for carrier one; 0 dB to 7 dB for carrier two , Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, power_offset: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:POFFset \n
		Snippet: driver.configure.uplink.carrier.set_poffset(power_offset = 1.0) \n
		Sets the DPCCH power offset, used by the UE to calculate the initial DPCCH power for random access. The power offset of
		the carrier two is defined as the power offset between the initial DPCCH power level on UL2 and the current DPCCH power
		level of UL1. \n
			:param power_offset: Range: -164 dB to -6 dB for carrier one; 0 dB to 7 dB for carrier two , Unit: dB
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(power_offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:POFFset {param}')

	def get_scode(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:SCODe \n
		Snippet: value: float = driver.configure.uplink.carrier.get_scode() \n
		Sets the long code number that the UE has to use to scramble the uplink WCDMA signal. \n
			:return: scrambling_code: Range: #H0 to #HFFFFFF
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:SCODe?')
		return Conversions.str_to_float(response)

	def set_scode(self, scrambling_code: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:CARRier<carrier>:SCODe \n
		Snippet: driver.configure.uplink.carrier.set_scode(scrambling_code = 1.0) \n
		Sets the long code number that the UE has to use to scramble the uplink WCDMA signal. \n
			:param scrambling_code: Range: #H0 to #HFFFFFF
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(scrambling_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:CARRier<Carrier>:SCODe {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
