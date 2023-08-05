from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gfactor:
	"""Gfactor commands group definition. 12 total commands, 3 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gfactor", core, parent)

	@property
	def pdata(self):
		"""pdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdata'):
			from .Gfactor_.Pdata import Pdata
			self._pdata = Pdata(self._core, self._base)
		return self._pdata

	@property
	def rmc(self):
		"""rmc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmc'):
			from .Gfactor_.Rmc import Rmc
			self._rmc = Rmc(self._core, self._base)
		return self._rmc

	@property
	def hsupa(self):
		"""hsupa commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_hsupa'):
			from .Gfactor_.Hsupa import Hsupa
			self._hsupa = Hsupa(self._core, self._base)
		return self._hsupa

	# noinspection PyTypeChecker
	class VideoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Beta_C: int: Range: 1 to 15
			- Beta_D: int: Range: 1 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_int('Beta_C'),
			ArgStruct.scalar_int('Beta_D')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Beta_C: int = None
			self.Beta_D: int = None

	def get_video(self) -> VideoStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:VIDeo \n
		Snippet: value: VideoStruct = driver.configure.uplink.gfactor.get_video() \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for video connections. \n
			:return: structure: for return value, see the help for VideoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:VIDeo?', self.__class__.VideoStruct())

	def set_video(self, value: VideoStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:VIDeo \n
		Snippet: driver.configure.uplink.gfactor.set_video(value = VideoStruct()) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for video connections. \n
			:param value: see the help for VideoStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:VIDeo', value)

	# noinspection PyTypeChecker
	class VoiceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Beta_C: int: Range: 1 to 15
			- Beta_D: int: Range: 1 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_int('Beta_C'),
			ArgStruct.scalar_int('Beta_D')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Beta_C: int = None
			self.Beta_D: int = None

	def get_voice(self) -> VoiceStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:VOICe \n
		Snippet: value: VoiceStruct = driver.configure.uplink.gfactor.get_voice() \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for voice connections. \n
			:return: structure: for return value, see the help for VoiceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:VOICe?', self.__class__.VoiceStruct())

	def set_voice(self, value: VoiceStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:VOICe \n
		Snippet: driver.configure.uplink.gfactor.set_voice(value = VoiceStruct()) \n
		Specifies the UE gain factors βc (DPCCH) and βd (DPDCH) for voice connections. \n
			:param value: see the help for VoiceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:VOICe', value)

	# noinspection PyTypeChecker
	class HsdpaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Beta_C: int: Range: 1 to 15
			- Beta_D: int: Range: 1 to 15
			- Delta_Ack: int: Range: 0 to 8
			- Delta_Nack: int: Range: 0 to 8
			- Delta_Cqi: int: Range: 0 to 8"""
		__meta_args_list = [
			ArgStruct.scalar_int('Beta_C'),
			ArgStruct.scalar_int('Beta_D'),
			ArgStruct.scalar_int('Delta_Ack'),
			ArgStruct.scalar_int('Delta_Nack'),
			ArgStruct.scalar_int('Delta_Cqi')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Beta_C: int = None
			self.Beta_D: int = None
			self.Delta_Ack: int = None
			self.Delta_Nack: int = None
			self.Delta_Cqi: int = None

	def get_hsdpa(self) -> HsdpaStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSDPa \n
		Snippet: value: HsdpaStruct = driver.configure.uplink.gfactor.get_hsdpa() \n
		Specifies the UE gain factors and power offsets for HSDPA connections. \n
			:return: structure: for return value, see the help for HsdpaStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSDPa?', self.__class__.HsdpaStruct())

	def set_hsdpa(self, value: HsdpaStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSDPa \n
		Snippet: driver.configure.uplink.gfactor.set_hsdpa(value = HsdpaStruct()) \n
		Specifies the UE gain factors and power offsets for HSDPA connections. \n
			:param value: see the help for HsdpaStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSDPa', value)

	def clone(self) -> 'Gfactor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gfactor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
