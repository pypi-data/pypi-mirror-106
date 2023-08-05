from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsdpa:
	"""Hsdpa commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsdpa", core, parent)

	# noinspection PyTypeChecker
	class RwindowStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Mode: enums.AutoManualMode: AUTO | MANual Automatic calculation | manual configuration of the window size
			- Receiving_Window: int: Manually configured window size applicable to Mode = MANual The value is rounded to the nearest of the following values: 1 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 768 | 1024 | 1536 | 2047 | 2560 | 3072 | 3584 | 4095 Range: 1 to 4095"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.AutoManualMode),
			ArgStruct.scalar_int('Receiving_Window')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.AutoManualMode = None
			self.Receiving_Window: int = None

	# noinspection PyTypeChecker
	def get_rwindow(self) -> RwindowStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:HSDPa:RWINdow \n
		Snippet: value: RwindowStruct = driver.configure.connection.packet.hsdpa.get_rwindow() \n
		Specifies the size of the receiver window in the UE. \n
			:return: structure: for return value, see the help for RwindowStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:HSDPa:RWINdow?', self.__class__.RwindowStruct())

	def set_rwindow(self, value: RwindowStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:HSDPa:RWINdow \n
		Snippet: driver.configure.connection.packet.hsdpa.set_rwindow(value = RwindowStruct()) \n
		Specifies the size of the receiver window in the UE. \n
			:param value: see the help for RwindowStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:HSDPa:RWINdow', value)

	# noinspection PyTypeChecker
	class TimerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Mode: enums.AutoManualMode: AUTO | MANual Automatic calculation | manual configuration of the timeout value
			- T_1_Release_Timer: float: Manually configured value applicable to Mode = MANual The value is rounded to the nearest of the following values in s: 0.01 | 0.02 | 0.03 … 0.1 | 0.12 | 0.14 | 0.16 | 0.2 | 0.3 | 0.4 Range: 0.01 s to 0.4 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.AutoManualMode),
			ArgStruct.scalar_float('T_1_Release_Timer')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.AutoManualMode = None
			self.T_1_Release_Timer: float = None

	# noinspection PyTypeChecker
	def get_timer(self) -> TimerStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:HSDPa:TIMer \n
		Snippet: value: TimerStruct = driver.configure.connection.packet.hsdpa.get_timer() \n
		Specifies the timeout value of the reordering release timer T1. \n
			:return: structure: for return value, see the help for TimerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:HSDPa:TIMer?', self.__class__.TimerStruct())

	def set_timer(self, value: TimerStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:HSDPa:TIMer \n
		Snippet: driver.configure.connection.packet.hsdpa.set_timer(value = TimerStruct()) \n
		Specifies the timeout value of the reordering release timer T1. \n
			:param value: see the help for TimerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:HSDPa:TIMer', value)
