from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 43 total commands, 6 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	@property
	def voice(self):
		"""voice commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_voice'):
			from .Connection_.Voice import Voice
			self._voice = Voice(self._core, self._base)
		return self._voice

	@property
	def tmode(self):
		"""tmode commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_tmode'):
			from .Connection_.Tmode import Tmode
			self._tmode = Tmode(self._core, self._base)
		return self._tmode

	@property
	def packet(self):
		"""packet commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_packet'):
			from .Connection_.Packet import Packet
			self._packet = Packet(self._core, self._base)
		return self._packet

	@property
	def srbSingle(self):
		"""srbSingle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srbSingle'):
			from .Connection_.SrbSingle import SrbSingle
			self._srbSingle = SrbSingle(self._core, self._base)
		return self._srbSingle

	@property
	def video(self):
		"""video commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_video'):
			from .Connection_.Video import Video
			self._video = Video(self._core, self._base)
		return self._video

	@property
	def cswitched(self):
		"""cswitched commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cswitched'):
			from .Connection_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	# noinspection PyTypeChecker
	class SrbSataStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Downlink: enums.SrbDataRate: R1K7 | R2K5 | R3K4 | R13K6 In kbit/s: 1.7, 2.5, 3.4, 13.6
			- Uplink: enums.SrbDataRate: R1K7 | R2K5 | R3K4 | R13K6 In kbit/s: 1.7, 2.5, 3.4, 13.6"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Downlink', enums.SrbDataRate),
			ArgStruct.scalar_enum('Uplink', enums.SrbDataRate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Downlink: enums.SrbDataRate = None
			self.Uplink: enums.SrbDataRate = None

	# noinspection PyTypeChecker
	def get_srb_sata(self) -> SrbSataStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:SRBData \n
		Snippet: value: SrbSataStruct = driver.configure.connection.get_srb_sata() \n
		Selects the SRB data rate for downlink and uplink. \n
			:return: structure: for return value, see the help for SrbSataStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:SRBData?', self.__class__.SrbSataStruct())

	def set_srb_sata(self, value: SrbSataStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:SRBData \n
		Snippet: driver.configure.connection.set_srb_sata(value = SrbSataStruct()) \n
		Selects the SRB data rate for downlink and uplink. \n
			:param value: see the help for SrbSataStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:SRBData', value)

	# noinspection PyTypeChecker
	def get_ue_terminate(self) -> enums.TerminatingType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:UETerminate \n
		Snippet: value: enums.TerminatingType = driver.configure.connection.get_ue_terminate() \n
		Selects the connection type to be used for UE terminating connections initiated by the instrument. \n
			:return: type_py: VOICe | VIDeo | SRB | TEST
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:UETerminate?')
		return Conversions.str_to_scalar_enum(response, enums.TerminatingType)

	def set_ue_terminate(self, type_py: enums.TerminatingType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:UETerminate \n
		Snippet: driver.configure.connection.set_ue_terminate(type_py = enums.TerminatingType.RMC) \n
		Selects the connection type to be used for UE terminating connections initiated by the instrument. \n
			:param type_py: VOICe | VIDeo | SRB | TEST
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TerminatingType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:UETerminate {param}')

	def get_cid(self) -> str:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:CID \n
		Snippet: value: str = driver.configure.connection.get_cid() \n
		Sets the calling party number of the R&S CMW to be displayed at the UE. Allowed characters are 0 to 9, *, #, a, b, c. \n
			:return: caller_id: 1 to 20-digit ID
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:CID?')
		return trim_str_response(response)

	def set_cid(self, caller_id: str) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:CID \n
		Snippet: driver.configure.connection.set_cid(caller_id = '1') \n
		Sets the calling party number of the R&S CMW to be displayed at the UE. Allowed characters are 0 to 9, *, #, a, b, c. \n
			:param caller_id: 1 to 20-digit ID
		"""
		param = Conversions.value_to_quoted_str(caller_id)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:CID {param}')

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
