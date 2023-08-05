from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 145 total commands, 14 Sub-groups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .Cell_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def rcause(self):
		"""rcause commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rcause'):
			from .Cell_.Rcause import Rcause
			self._rcause = Rcause(self._core, self._base)
		return self._rcause

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_timeout'):
			from .Cell_.Timeout import Timeout
			self._timeout = Timeout(self._core, self._base)
		return self._timeout

	@property
	def request(self):
		"""request commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_request'):
			from .Cell_.Request import Request
			self._request = Request(self._core, self._base)
		return self._request

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_security'):
			from .Cell_.Security import Security
			self._security = Security(self._core, self._base)
		return self._security

	@property
	def ueIdentity(self):
		"""ueIdentity commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ueIdentity'):
			from .Cell_.UeIdentity import UeIdentity
			self._ueIdentity = UeIdentity(self._core, self._base)
		return self._ueIdentity

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mnc'):
			from .Cell_.Mnc import Mnc
			self._mnc = Mnc(self._core, self._base)
		return self._mnc

	@property
	def reSelection(self):
		"""reSelection commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_reSelection'):
			from .Cell_.ReSelection import ReSelection
			self._reSelection = ReSelection(self._core, self._base)
		return self._reSelection

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_time'):
			from .Cell_.Time import Time
			self._time = Time(self._core, self._base)
		return self._time

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sync'):
			from .Cell_.Sync import Sync
			self._sync = Sync(self._core, self._base)
		return self._sync

	@property
	def hsdpa(self):
		"""hsdpa commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_hsdpa'):
			from .Cell_.Hsdpa import Hsdpa
			self._hsdpa = Hsdpa(self._core, self._base)
		return self._hsdpa

	@property
	def hsupa(self):
		"""hsupa commands group. 6 Sub-classes, 7 commands."""
		if not hasattr(self, '_hsupa'):
			from .Cell_.Hsupa import Hsupa
			self._hsupa = Hsupa(self._core, self._base)
		return self._hsupa

	@property
	def horder(self):
		"""horder commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_horder'):
			from .Cell_.Horder import Horder
			self._horder = Horder(self._core, self._base)
		return self._horder

	@property
	def cpc(self):
		"""cpc commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpc'):
			from .Cell_.Cpc import Cpc
			self._cpc = Cpc(self._core, self._base)
		return self._cpc

	# noinspection PyTypeChecker
	def get_mr_version(self) -> enums.MaxRelVersion:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MRVersion \n
		Snippet: value: enums.MaxRelVersion = driver.configure.cell.get_mr_version() \n
		Specifies the maximum release version as a cell limitation. Automatic setting respects the installed R&S CMW options and
		the UE capabilities. \n
			:return: max_rel_version: AUTO | R99 | R5 | R6 | R7 | R8 | R9 | R10 | R11
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:MRVersion?')
		return Conversions.str_to_scalar_enum(response, enums.MaxRelVersion)

	def set_mr_version(self, max_rel_version: enums.MaxRelVersion) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MRVersion \n
		Snippet: driver.configure.cell.set_mr_version(max_rel_version = enums.MaxRelVersion.AUTO) \n
		Specifies the maximum release version as a cell limitation. Automatic setting respects the installed R&S CMW options and
		the UE capabilities. \n
			:param max_rel_version: AUTO | R99 | R5 | R6 | R7 | R8 | R9 | R10 | R11
		"""
		param = Conversions.enum_scalar_to_str(max_rel_version, enums.MaxRelVersion)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:MRVersion {param}')

	def get_rsignaling(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RSIGnaling \n
		Snippet: value: bool = driver.configure.cell.get_rsignaling() \n
		Enables or disables the reduced signaling mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:RSIGnaling?')
		return Conversions.str_to_bool(response)

	def set_rsignaling(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RSIGnaling \n
		Snippet: driver.configure.cell.set_rsignaling(enable = False) \n
		Enables or disables the reduced signaling mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:RSIGnaling {param}')

	def get_psdomain(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:PSDomain \n
		Snippet: value: bool = driver.configure.cell.get_psdomain() \n
		Enables or disables the support of packet switched connections by the emulated UTRAN cell. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:PSDomain?')
		return Conversions.str_to_bool(response)

	def set_psdomain(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:PSDomain \n
		Snippet: driver.configure.cell.set_psdomain(enable = False) \n
		Enables or disables the support of packet switched connections by the emulated UTRAN cell. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:PSDomain {param}')

	def get_identity(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:IDENtity \n
		Snippet: value: float = driver.configure.cell.get_identity() \n
		Specifies the cell identity (28-digit binary number) . \n
			:return: value: Range: #B0 to #B1111111111111111111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:IDENtity?')
		return Conversions.str_to_float(response)

	def set_identity(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:IDENtity \n
		Snippet: driver.configure.cell.set_identity(value = 1.0) \n
		Specifies the cell identity (28-digit binary number) . \n
			:param value: Range: #B0 to #B1111111111111111111111111111
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:IDENtity {param}')

	def get_id_node(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:IDNode \n
		Snippet: value: float = driver.configure.cell.get_id_node() \n
		Specifies the NodeB identity (16-digit binary number) . \n
			:return: value: Range: #B0 to #B1111111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:IDNode?')
		return Conversions.str_to_float(response)

	def set_id_node(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:IDNode \n
		Snippet: driver.configure.cell.set_id_node(value = 1.0) \n
		Specifies the NodeB identity (16-digit binary number) . \n
			:param value: Range: #B0 to #B1111111111111111
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:IDNode {param}')

	def get_rnc(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RNC \n
		Snippet: value: float = driver.configure.cell.get_rnc() \n
		Specifies the radio network controller (RNC) identity (12-digit binary number) . \n
			:return: value: Range: #B0 to #B111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:RNC?')
		return Conversions.str_to_float(response)

	def set_rnc(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RNC \n
		Snippet: driver.configure.cell.set_rnc(value = 1.0) \n
		Specifies the radio network controller (RNC) identity (12-digit binary number) . \n
			:param value: Range: #B0 to #B111111111111
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:RNC {param}')

	def get_ura(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:URA \n
		Snippet: value: float = driver.configure.cell.get_ura() \n
		Specifies the UTRAN registration area (URA) identity (16-digit binary number) . \n
			:return: value: Range: #B0 to #B1111111111111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:URA?')
		return Conversions.str_to_float(response)

	def set_ura(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:URA \n
		Snippet: driver.configure.cell.set_ura(value = 1.0) \n
		Specifies the UTRAN registration area (URA) identity (16-digit binary number) . \n
			:param value: Range: #B0 to #B1111111111111111
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:URA {param}')

	def get_rac(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RAC \n
		Snippet: value: float = driver.configure.cell.get_rac() \n
		Specifies the routing area code for PS services (8-digit binary number) . \n
			:return: value: Range: #B0 to #B11111111
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:RAC?')
		return Conversions.str_to_float(response)

	def set_rac(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:RAC \n
		Snippet: driver.configure.cell.set_rac(value = 1.0) \n
		Specifies the routing area code for PS services (8-digit binary number) . \n
			:param value: Range: #B0 to #B11111111
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:RAC {param}')

	def get_lac(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:LAC \n
		Snippet: value: float = driver.configure.cell.get_lac() \n
		Specifies the location area code for CS services. \n
			:return: value: Range: #H1 to #HFFFD
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:LAC?')
		return Conversions.str_to_float(response)

	def set_lac(self, value: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:LAC \n
		Snippet: driver.configure.cell.set_lac(value = 1.0) \n
		Specifies the location area code for CS services. \n
			:param value: Range: #H1 to #HFFFD
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:LAC {param}')

	# noinspection PyTypeChecker
	def get_nt_operation(self) -> enums.NtOperMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:NTOPeration \n
		Snippet: value: enums.NtOperMode = driver.configure.cell.get_nt_operation() \n
		Selects the network operation mode indicating whether a Gs interface is present in the network (mode I) or not (mode II) . \n
			:return: mode: M1 | M2 M1: mode I, Gs interface present M2: mode II, Gs interface not present
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:NTOPeration?')
		return Conversions.str_to_scalar_enum(response, enums.NtOperMode)

	def set_nt_operation(self, mode: enums.NtOperMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:NTOPeration \n
		Snippet: driver.configure.cell.set_nt_operation(mode = enums.NtOperMode.M1) \n
		Selects the network operation mode indicating whether a Gs interface is present in the network (mode I) or not (mode II) . \n
			:param mode: M1 | M2 M1: mode I, Gs interface present M2: mode II, Gs interface not present
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NtOperMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:NTOPeration {param}')

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MCC \n
		Snippet: value: int = driver.configure.cell.get_mcc() \n
		Specifies the three-digit mobile country code (MCC) . Leading zeros can be omitted. \n
			:return: value: Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, value: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:MCC \n
		Snippet: driver.configure.cell.set_mcc(value = 1) \n
		Specifies the three-digit mobile country code (MCC) . Leading zeros can be omitted. \n
			:param value: Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:MCC {param}')

	def get_bindicator(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:BINDicator \n
		Snippet: value: bool = driver.configure.cell.get_bindicator() \n
		Specifies whether the band indicator has to be broadcast as part of the system information or not. \n
			:return: enable: OFF | ON ON: broadcast band indicator OFF: do not broadcast band indicator
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:BINDicator?')
		return Conversions.str_to_bool(response)

	def set_bindicator(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:BINDicator \n
		Snippet: driver.configure.cell.set_bindicator(enable = False) \n
		Specifies whether the band indicator has to be broadcast as part of the system information or not. \n
			:param enable: OFF | ON ON: broadcast band indicator OFF: do not broadcast band indicator
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:BINDicator {param}')

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
