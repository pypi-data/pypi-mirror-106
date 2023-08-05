from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqIn:
	"""IqIn commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqIn", core, parent)

	# noinspection PyTypeChecker
	class CarrierStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Pep: float: Peak envelope power of the incoming baseband signal Range: -60 dBFS to 0 dBFS, Unit: dBFS
			- Level: float: Average level of the incoming baseband signal (without noise) Range: depends on crest factor and level of outgoing baseband signal , Unit: dBFS"""
		__meta_args_list = [
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pep: float = None
			self.Level: float = None

	def get_carrier(self) -> CarrierStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IQIN:CARRier<carrier> \n
		Snippet: value: CarrierStruct = driver.configure.iqIn.get_carrier() \n
		Specifies properties of the baseband signal at the I/Q input. \n
			:return: structure: for return value, see the help for CarrierStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:IQIN:CARRier<Carrier>?', self.__class__.CarrierStruct())

	def set_carrier(self, value: CarrierStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:IQIN:CARRier<carrier> \n
		Snippet: driver.configure.iqIn.set_carrier(value = CarrierStruct()) \n
		Specifies properties of the baseband signal at the I/Q input. \n
			:param value: see the help for CarrierStruct structure arguments.
		Global Repeated Capabilities: repcap.Carrier"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:IQIN:CARRier<Carrier>', value)
