from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpc:
	"""Tpc commands group definition. 9 total commands, 5 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tpc", core, parent)

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Tpc_.Set import Set
			self._set = Set(self._core, self._base)
		return self._set

	@property
	def tpower(self):
		"""tpower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tpower'):
			from .Tpc_.Tpower import Tpower
			self._tpower = Tpower(self._core, self._base)
		return self._tpower

	@property
	def mpedch(self):
		"""mpedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpedch'):
			from .Tpc_.Mpedch import Mpedch
			self._mpedch = Mpedch(self._core, self._base)
		return self._mpedch

	@property
	def precondition(self):
		"""precondition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_precondition'):
			from .Tpc_.Precondition import Precondition
			self._precondition = Precondition(self._core, self._base)
		return self._precondition

	@property
	def pexecute(self):
		"""pexecute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexecute'):
			from .Tpc_.Pexecute import Pexecute
			self._pexecute = Pexecute(self._core, self._base)
		return self._pexecute

	# noinspection PyTypeChecker
	def get_state(self) -> enums.TpcState:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:STATe \n
		Snippet: value: enums.TpcState = driver.configure.uplink.tpc.get_state() \n
		Queries the current TPC state. \n
			:return: state: IDLE | CONTinous | ALTernating | TPLocked | TPUNlocked | MAXPower | MINPower | TRANsition | SINGle | SEARching | FAILed | MRESource | SCONflict | SCHanged IDLE: no connection established CONTinuous: transmitting continuous pattern ALTernating: transmitting alternating pattern TPLocked: closed loop target power reached TPUNlocked: reaching closed loop target power failed MAXPower: maximum power reached MINPower: minimum power reached TRANsition: transition to a state, e.g. to maximum power SINGle: transmitting a single user-defined pattern Only relevant for 'Max. Power E-DCH' setup: SEARching: setup started, max power not yet reached FAILed: test procedure failed in state 'Searching' MRESource: required resources are blocked/not available SCONflict: settings are inappropriate for the setup SCHanged: relevant settings changed after setup execution
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.TpcState)

	def get_pattern(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PATTern \n
		Snippet: value: str = driver.configure.uplink.tpc.get_pattern() \n
		Sets the 'User Defined Pattern' to be used for 'Single Pattern' and 'Continuous Pattern'. \n
			:return: pattern: String to specify the pattern. Range: up to 60 zeros and ones
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PATTern?')
		return trim_str_response(response)

	def set_pattern(self, pattern: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PATTern \n
		Snippet: driver.configure.uplink.tpc.set_pattern(pattern = '1') \n
		Sets the 'User Defined Pattern' to be used for 'Single Pattern' and 'Continuous Pattern'. \n
			:param pattern: String to specify the pattern. Range: up to 60 zeros and ones
		"""
		param = Conversions.value_to_quoted_str(pattern)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PATTern {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.TpcMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:MODE \n
		Snippet: value: enums.TpcMode = driver.configure.uplink.tpc.get_mode() \n
		Defines the power control algorithm and the TPC step size configured at the UE. \n
			:return: mode: A2S1 | A1S1 | A1S2 A2S1: algorithm 2, step size 1 dB A1S1: algorithm 1, step size 1 dB A1S2: algorithm 1, step size 2 dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TpcMode)

	def set_mode(self, mode: enums.TpcMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:MODE \n
		Snippet: driver.configure.uplink.tpc.set_mode(mode = enums.TpcMode.A1S1) \n
		Defines the power control algorithm and the TPC step size configured at the UE. \n
			:param mode: A2S1 | A1S1 | A1S2 A2S1: algorithm 2, step size 1 dB A1S1: algorithm 1, step size 1 dB A1S2: algorithm 1, step size 2 dB
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TpcMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:MODE {param}')

	def clone(self) -> 'Tpc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tpc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
