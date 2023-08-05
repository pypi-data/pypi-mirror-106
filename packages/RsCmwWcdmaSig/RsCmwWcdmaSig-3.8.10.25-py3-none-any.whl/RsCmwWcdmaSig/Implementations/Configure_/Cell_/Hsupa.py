from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsupa:
	"""Hsupa commands group definition. 19 total commands, 6 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsupa", core, parent)

	@property
	def pdu(self):
		"""pdu commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdu'):
			from .Hsupa_.Pdu import Pdu
			self._pdu = Pdu(self._core, self._base)
		return self._pdu

	@property
	def ueCategory(self):
		"""ueCategory commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueCategory'):
			from .Hsupa_.UeCategory import UeCategory
			self._ueCategory = UeCategory(self._core, self._base)
		return self._ueCategory

	@property
	def eagch(self):
		"""eagch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eagch'):
			from .Hsupa_.Eagch import Eagch
			self._eagch = Eagch(self._core, self._base)
		return self._eagch

	@property
	def horder(self):
		"""horder commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_horder'):
			from .Hsupa_.Horder import Horder
			self._horder = Horder(self._core, self._base)
		return self._horder

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_etfci'):
			from .Hsupa_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	@property
	def harq(self):
		"""harq commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_harq'):
			from .Hsupa_.Harq import Harq
			self._harq = Harq(self._core, self._base)
		return self._harq

	# noinspection PyTypeChecker
	def get_tti(self) -> enums.TransTimeInterval:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:TTI \n
		Snippet: value: enums.TransTimeInterval = driver.configure.cell.hsupa.get_tti() \n
		Selects the transmission time interval (TTI) for the E-DCH. The value must be compatible with the UE category (2 ms TTI
		only allowed for category 2, 4 and 6) . \n
			:return: tti: M2 | M10 M2: 2 ms M10: 10 ms
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:TTI?')
		return Conversions.str_to_scalar_enum(response, enums.TransTimeInterval)

	def set_tti(self, tti: enums.TransTimeInterval) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:TTI \n
		Snippet: driver.configure.cell.hsupa.set_tti(tti = enums.TransTimeInterval.M10) \n
		Selects the transmission time interval (TTI) for the E-DCH. The value must be compatible with the UE category (2 ms TTI
		only allowed for category 2, 4 and 6) . \n
			:param tti: M2 | M10 M2: 2 ms M10: 10 ms
		"""
		param = Conversions.enum_scalar_to_str(tti, enums.TransTimeInterval)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:TTI {param}')

	# noinspection PyTypeChecker
	def get_hr_version(self) -> enums.HrVersion:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HRVersion \n
		Snippet: value: enums.HrVersion = driver.configure.cell.hsupa.get_hr_version() \n
		Specifies the HARQ RV configuration value signaled to the UE. \n
			:return: version: RV0 | TABLe RV0: use always redundancy version 0 TABLe: determine the redundancy version using a table as specified in 3GPP TS 25.212
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HRVersion?')
		return Conversions.str_to_scalar_enum(response, enums.HrVersion)

	def set_hr_version(self, version: enums.HrVersion) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HRVersion \n
		Snippet: driver.configure.cell.hsupa.set_hr_version(version = enums.HrVersion.RV0) \n
		Specifies the HARQ RV configuration value signaled to the UE. \n
			:param version: RV0 | TABLe RV0: use always redundancy version 0 TABLe: determine the redundancy version using a table as specified in 3GPP TS 25.212
		"""
		param = Conversions.enum_scalar_to_str(version, enums.HrVersion)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HRVersion {param}')

	def get_hbd_condition(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HBDConition \n
		Snippet: value: float = driver.configure.cell.hsupa.get_hbd_condition() \n
		Specifies the happy bit delay condition value signaled to the UE. \n
			:return: delay: Only the following values are allowed (in ms) : 2 | 10 | 20 | 50 | 100 | 200 | 500 | 1000 If you enter another value, the nearest allowed value is set instead. Range: 2 ms to 1000 ms, Unit: ms
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HBDConition?')
		return Conversions.str_to_float(response)

	def set_hbd_condition(self, delay: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:HBDConition \n
		Snippet: driver.configure.cell.hsupa.set_hbd_condition(delay = 1.0) \n
		Specifies the happy bit delay condition value signaled to the UE. \n
			:param delay: Only the following values are allowed (in ms) : 2 | 10 | 20 | 50 | 100 | 200 | 500 | 1000 If you enter another value, the nearest allowed value is set instead. Range: 2 ms to 1000 ms, Unit: ms
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:HBDConition {param}')

	def get_pl_pl_non_max(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PLPLnonmax \n
		Snippet: value: float = driver.configure.cell.hsupa.get_pl_pl_non_max() \n
		Specifies the 'PLnon-max' value signaled to the UE. \n
			:return: limit: Range: 0.44 to 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PLPLnonmax?')
		return Conversions.str_to_float(response)

	def set_pl_pl_non_max(self, limit: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:PLPLnonmax \n
		Snippet: driver.configure.cell.hsupa.set_pl_pl_non_max(limit = 1.0) \n
		Specifies the 'PLnon-max' value signaled to the UE. \n
			:param limit: Range: 0.44 to 1
		"""
		param = Conversions.decimal_value_to_str(limit)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:PLPLnonmax {param}')

	# noinspection PyTypeChecker
	def get_mccode(self) -> enums.MaxChanCode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:MCCode \n
		Snippet: value: enums.MaxChanCode = driver.configure.cell.hsupa.get_mccode() \n
		Specifies the maximum channelization codes value signaled to the UE. Depending on several other HSUPA parameters, e.g.
		the UE category, only a subset of values is allowed. \n
			:return: code: S64 | S32 | S16 | S8 | S4 | S24 | S22 | S224 S64, S32, S16, S8, S4: one code, SF 64 to SF 4 S24: two codes, SF 4 S22: two codes, SF 2 S224: four codes, two with SF 2 and two with SF 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:MCCode?')
		return Conversions.str_to_scalar_enum(response, enums.MaxChanCode)

	def set_mccode(self, code: enums.MaxChanCode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:MCCode \n
		Snippet: driver.configure.cell.hsupa.set_mccode(code = enums.MaxChanCode.S16) \n
		Specifies the maximum channelization codes value signaled to the UE. Depending on several other HSUPA parameters, e.g.
		the UE category, only a subset of values is allowed. \n
			:param code: S64 | S32 | S16 | S8 | S4 | S24 | S22 | S224 S64, S32, S16, S8, S4: one code, SF 64 to SF 4 S24: two codes, SF 4 S22: two codes, SF 2 S224: four codes, two with SF 2 and two with SF 4
		"""
		param = Conversions.enum_scalar_to_str(code, enums.MaxChanCode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:MCCode {param}')

	# noinspection PyTypeChecker
	class IsGrantStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Grant: int or bool: Serving grant value information element Range: 0 to 38 Additional parameters: OFF | ON (disable | enable transmission of the initial serving grant parameters)
			- Type_Py: enums.ParameterType: PRIMary | SECondary Primary/secondary grant selector information element"""
		__meta_args_list = [
			ArgStruct.scalar_int_ext('Grant'),
			ArgStruct.scalar_enum('Type_Py', enums.ParameterType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Grant: int or bool = None
			self.Type_Py: enums.ParameterType = None

	def get_is_grant(self) -> IsGrantStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:ISGRant \n
		Snippet: value: IsGrantStruct = driver.configure.cell.hsupa.get_is_grant() \n
		Specifies initial serving grant parameters signaled to the UE. If you only want to modify the <Grant>, you can omit the
		<Type> parameter. \n
			:return: structure: for return value, see the help for IsGrantStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:ISGRant?', self.__class__.IsGrantStruct())

	def set_is_grant(self, value: IsGrantStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:ISGRant \n
		Snippet: driver.configure.cell.hsupa.set_is_grant(value = IsGrantStruct()) \n
		Specifies initial serving grant parameters signaled to the UE. If you only want to modify the <Grant>, you can omit the
		<Type> parameter. \n
			:param value: see the help for IsGrantStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:ISGRant', value)

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.HsupaModulation:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:MODulation \n
		Snippet: value: enums.HsupaModulation = driver.configure.cell.hsupa.get_modulation() \n
		Selects the E-DCH modulation scheme to be used during HSUPA connection. \n
			:return: modulation: QPSK | Q16 QPSK, 16-QAM
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.HsupaModulation)

	def set_modulation(self, modulation: enums.HsupaModulation) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSUPa:MODulation \n
		Snippet: driver.configure.cell.hsupa.set_modulation(modulation = enums.HsupaModulation.Q16) \n
		Selects the E-DCH modulation scheme to be used during HSUPA connection. \n
			:param modulation: QPSK | Q16 QPSK, 16-QAM
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.HsupaModulation)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSUPa:MODulation {param}')

	def clone(self) -> 'Hsupa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsupa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
