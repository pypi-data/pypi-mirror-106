from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Packet:
	"""Packet commands group definition. 15 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("packet", core, parent)

	@property
	def hsdpa(self):
		"""hsdpa commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hsdpa'):
			from .Packet_.Hsdpa import Hsdpa
			self._hsdpa = Hsdpa(self._core, self._base)
		return self._hsdpa

	@property
	def inactivity(self):
		"""inactivity commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_inactivity'):
			from .Packet_.Inactivity import Inactivity
			self._inactivity = Inactivity(self._core, self._base)
		return self._inactivity

	@property
	def rohc(self):
		"""rohc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rohc'):
			from .Packet_.Rohc import Rohc
			self._rohc = Rohc(self._core, self._base)
		return self._rohc

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Downlink: enums.DataRateDownlink: R8 | R16 | R32 | R64 | R128 | R384 | HSDPa R8 to R384: 8 kbps to 384 kbps HSDPa: HSDPA connection
			- Uplink: enums.DataRateUplink: R8 | R16 | R32 | R64 | R128 | R384 | HSUPa R8 to R384: 8 kbps to 384 kbps HSUPa: HSUPA connection"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Downlink', enums.DataRateDownlink),
			ArgStruct.scalar_enum('Uplink', enums.DataRateUplink)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Downlink: enums.DataRateDownlink = None
			self.Uplink: enums.DataRateUplink = None

	# noinspection PyTypeChecker
	def get_drate(self) -> DrateStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:DRATe \n
		Snippet: value: DrateStruct = driver.configure.connection.packet.get_drate() \n
		Specifies data rates for end-to-end data connections in downlink and uplink direction. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:DRATe?', self.__class__.DrateStruct())

	def set_drate(self, value: DrateStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:PACKet:DRATe \n
		Snippet: driver.configure.connection.packet.set_drate(value = DrateStruct()) \n
		Specifies data rates for end-to-end data connections in downlink and uplink direction. \n
			:param value: see the help for DrateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:PACKet:DRATe', value)

	def clone(self) -> 'Packet':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Packet(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
