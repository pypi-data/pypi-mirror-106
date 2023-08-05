from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Udtx:
	"""Udtx commands group definition. 7 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udtx", core, parent)

	@property
	def cycle(self):
		"""cycle commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cycle'):
			from .Udtx_.Cycle import Cycle
			self._cycle = Cycle(self._core, self._base)
		return self._cycle

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:ENABle \n
		Snippet: value: bool = driver.configure.cell.cpc.udtx.get_enable() \n
		Defines the settings for the discontinuous transmission in the uplink, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: enable: OFF | ON enables/disables UL DTX
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:ENABle \n
		Snippet: driver.configure.cell.cpc.udtx.set_enable(enable = False) \n
		Defines the settings for the discontinuous transmission in the uplink, see 'Continuous Packet Connectivity (CPC) '. \n
			:param enable: OFF | ON enables/disables UL DTX
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:ENABle {param}')

	def get_lp_length(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:LPLength \n
		Snippet: value: int = driver.configure.cell.cpc.udtx.get_lp_length() \n
		Defines the long preamble length that the UE uses during UL DTX cycle 2 to aid synchronization, see 'Continuous Packet
		Connectivity (CPC) '. \n
			:return: length: Only the following values are allowed (in slots) : 2 | 4 | 15 If you enter another value, the nearest allowed value is set instead. Range: 2 slots to 15 slots, Unit: slot
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:LPLength?')
		return Conversions.str_to_int(response)

	def set_lp_length(self, length: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:LPLength \n
		Snippet: driver.configure.cell.cpc.udtx.set_lp_length(length = 1) \n
		Defines the long preamble length that the UE uses during UL DTX cycle 2 to aid synchronization, see 'Continuous Packet
		Connectivity (CPC) '. \n
			:param length: Only the following values are allowed (in slots) : 2 | 4 | 15 If you enter another value, the nearest allowed value is set instead. Range: 2 slots to 15 slots, Unit: slot
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:LPLength {param}')

	def get_cqi_timer(self) -> int or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CQITimer \n
		Snippet: value: int or bool = driver.configure.cell.cpc.udtx.get_cqi_timer() \n
		Number of subframes after an HS-DSCH reception during which the CQI reports have higher priority than the DTX pattern and
		are transmitted according to the regular CQI pattern, see 'Continuous Packet Connectivity (CPC) '. \n
			:return: timer: 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | ON | OFF If you enter another value, the nearest allowed value is set instead. Range: 0 Subframe to 512 Subframe, Unit: subframe Additional OFF | ON disables | enables the CQI DTX timer
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CQITimer?')
		return Conversions.str_to_int_or_bool(response)

	def set_cqi_timer(self, timer: int or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CPC:UDTX:CQITimer \n
		Snippet: driver.configure.cell.cpc.udtx.set_cqi_timer(timer = 1) \n
		Number of subframes after an HS-DSCH reception during which the CQI reports have higher priority than the DTX pattern and
		are transmitted according to the regular CQI pattern, see 'Continuous Packet Connectivity (CPC) '. \n
			:param timer: 0 | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | ON | OFF If you enter another value, the nearest allowed value is set instead. Range: 0 Subframe to 512 Subframe, Unit: subframe Additional OFF | ON disables | enables the CQI DTX timer
		"""
		param = Conversions.decimal_or_bool_value_to_str(timer)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CPC:UDTX:CQITimer {param}')

	def clone(self) -> 'Udtx':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Udtx(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
