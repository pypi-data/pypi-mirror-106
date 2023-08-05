from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOut:
	"""IqOut commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqOut", core, parent)

	# noinspection PyTypeChecker
	class CarrierStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sample_Rate: enums.SampleRate: M100 Fixed value, indicating a sample rate of 100 Msps (100 MHz)
			- Pep: float: Peak envelope power of the baseband signal Range: -60 dBFS to 0 dBFS, Unit: dBFS
			- Crest_Factor: float: Crest factor of the baseband signal Range: 0 dB to 60 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sample_Rate', enums.SampleRate),
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Crest_Factor')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Rate: enums.SampleRate = None
			self.Pep: float = None
			self.Crest_Factor: float = None

	# noinspection PyTypeChecker
	def get_carrier(self) -> CarrierStruct:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:IQOut:CARRier<carrier> \n
		Snippet: value: CarrierStruct = driver.sense.iqOut.get_carrier() \n
		Queries properties of the baseband signal at the I/Q output. \n
			:return: structure: for return value, see the help for CarrierStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('SENSe:WCDMa:SIGNaling<Instance>:IQOut:CARRier<Carrier>?', self.__class__.CarrierStruct())
