from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 9 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .UserDefined_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .UserDefined_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	def get_ud_separation(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:UDSeparation \n
		Snippet: value: float = driver.configure.rfSettings.userDefined.get_ud_separation() \n
		Specifies the uplink - downlink separation interval for user-defined band. \n
			:return: frequency: Range: -3832.4 Hz to 2012.4 Hz , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:UDSeparation?')
		return Conversions.str_to_float(response)

	def set_ud_separation(self, frequency: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:UDEFined:UDSeparation \n
		Snippet: driver.configure.rfSettings.userDefined.set_ud_separation(frequency = 1.0) \n
		Specifies the uplink - downlink separation interval for user-defined band. \n
			:param frequency: Range: -3832.4 Hz to 2012.4 Hz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:UDEFined:UDSeparation {param}')

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
