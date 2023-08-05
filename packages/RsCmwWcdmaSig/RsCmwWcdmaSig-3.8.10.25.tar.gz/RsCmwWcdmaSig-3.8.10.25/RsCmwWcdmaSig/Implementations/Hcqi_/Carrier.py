from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 8 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def bler(self):
		"""bler commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bler'):
			from .Carrier_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dtx'):
			from .Carrier_.Dtx import Dtx
			self._dtx = Dtx(self._core, self._base)
		return self._dtx

	@property
	def msFrames(self):
		"""msFrames commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_msFrames'):
			from .Carrier_.MsFrames import MsFrames
			self._msFrames = MsFrames(self._core, self._base)
		return self._msFrames

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Median_Cqi: int: Middle of the CQI distribution reported in the first measurement stage Range: 0 to 30
			- Meas_Sub_Frames: int: Total number of measured HSDPA subframes in stage one Range: 0 to 1E+6
			- Cqiin_Range: float: Percentage of the CQI values reported within the interval [median CQI - 2, median CQI + 2] Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Median_Cqi'),
			ArgStruct.scalar_int('Meas_Sub_Frames'),
			ArgStruct.scalar_float('Cqiin_Range')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Median_Cqi: int = None
			self.Meas_Sub_Frames: int = None
			self.Cqiin_Range: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:WCDMa:SIGNaling<instance>:HCQI:CARRier<carrier> \n
		Snippet: value: ResultData = driver.hcqi.carrier.fetch() \n
		Returns the results of the first stage of HSDPA CQI measurement per carrier. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:WCDMa:SIGNaling<Instance>:HCQI:CARRier<Carrier>?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:WCDMa:SIGNaling<instance>:HCQI:CARRier<carrier> \n
		Snippet: value: ResultData = driver.hcqi.carrier.read() \n
		Returns the results of the first stage of HSDPA CQI measurement per carrier. \n
		Global Repeated Capabilities: repcap.Carrier
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:WCDMa:SIGNaling<Instance>:HCQI:CARRier<Carrier>?', self.__class__.ResultData())

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
