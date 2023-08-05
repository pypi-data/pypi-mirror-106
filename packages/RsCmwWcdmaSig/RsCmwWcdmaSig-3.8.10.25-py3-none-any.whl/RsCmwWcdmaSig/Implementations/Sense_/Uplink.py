from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uplink", core, parent)

	@property
	def olpControl(self):
		"""olpControl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_olpControl'):
			from .Uplink_.OlpControl import OlpControl
			self._olpControl = OlpControl(self._core, self._base)
		return self._olpControl

	def get_ei_power(self) -> float:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UL:EIPower \n
		Snippet: value: float = driver.sense.uplink.get_ei_power() \n
		Queries the expected initial DPCCH power. \n
			:return: exp_dpcchp_ower: Range: -160 dBm to 33 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UL:EIPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
