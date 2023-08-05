from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 32 total commands, 5 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcarrier'):
			from .RfSettings_.Dcarrier import Dcarrier
			self._dcarrier = Dcarrier(self._core, self._base)
		return self._dcarrier

	@property
	def carrier(self):
		"""carrier commands group. 7 Sub-classes, 4 commands."""
		if not hasattr(self, '_carrier'):
			from .RfSettings_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def coPower(self):
		"""coPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coPower'):
			from .RfSettings_.CoPower import CoPower
			self._coPower = CoPower(self._core, self._base)
		return self._coPower

	@property
	def toPower(self):
		"""toPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toPower'):
			from .RfSettings_.ToPower import ToPower
			self._toPower = ToPower(self._core, self._base)
		return self._toPower

	@property
	def userDefined(self):
		"""userDefined commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_userDefined'):
			from .RfSettings_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	# noinspection PyTypeChecker
	class DbdcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON
			- Config: enums.OperBandConfig: UDEFined | C1 | C2 | C3 | C4 | C5 | C6 UDEFined: User defined (custom) - free band selection C1: DL band A I, DL band B VIII C2: DL band A II, DL band B IV C3: DL band A I, DL band B V C4: DL band A I, DL band B XI C5: DL band A II, DL band B V C6: DL band A I, DL band B XXXII UL applies the band of the DL carrier 1, where the assignment of band A or band B is possible. Exception: no UL for operating band XXXII."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Config', enums.OperBandConfig)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Config: enums.OperBandConfig = None

	def get_dbdc(self) -> DbdcStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:DBDC \n
		Snippet: value: DbdcStruct = driver.configure.rfSettings.get_dbdc() \n
		Enables dual band dual carrier HSDPA operation and selects the operating bands for UL and DL. For operating band
		description, see 'Operating Bands'. \n
			:return: structure: for return value, see the help for DbdcStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:DBDC?', self.__class__.DbdcStruct())

	def set_dbdc(self, value: DbdcStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:DBDC \n
		Snippet: driver.configure.rfSettings.set_dbdc(value = DbdcStruct()) \n
		Enables dual band dual carrier HSDPA operation and selects the operating bands for UL and DL. For operating band
		description, see 'Operating Bands'. \n
			:param value: see the help for DbdcStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:DBDC', value)

	# noinspection PyTypeChecker
	def get_enp_mode(self) -> enums.NominalPowerMode:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:ENPMode \n
		Snippet: value: enums.NominalPowerMode = driver.configure.rfSettings.get_enp_mode() \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwWcdmaSig.Configure.RfSettings.envelopePower
			- method RsCmwWcdmaSig.Configure.RfSettings.margin \n
			:return: mode: MANual | ULPC MANual: The expected nominal power and margin are specified manually. ULPC: The expected nominal power is calculated according to the UL power control settings.
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:ENPMode?')
		return Conversions.str_to_scalar_enum(response, enums.NominalPowerMode)

	def set_enp_mode(self, mode: enums.NominalPowerMode) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:ENPMode \n
		Snippet: driver.configure.rfSettings.set_enp_mode(mode = enums.NominalPowerMode.AUToranging) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwWcdmaSig.Configure.RfSettings.envelopePower
			- method RsCmwWcdmaSig.Configure.RfSettings.margin \n
			:param mode: MANual | ULPC MANual: The expected nominal power and margin are specified manually. ULPC: The expected nominal power is calculated according to the UL power control settings.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NominalPowerMode)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:ENPMode {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. \n
			:return: expected_power: The range of the expected nominal power can be calculated as follows: Range (Expected Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, expected_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(expected_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal. \n
			:param expected_power: The range of the expected nominal power can be calculated as follows: Range (Expected Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(expected_power)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:ENPower {param}')

	def get_margin(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:MARGin \n
		Snippet: value: float = driver.configure.rfSettings.get_margin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode. The
		reference level minus the external input attenuation must be within the power range of the selected input connector;
		refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwWcdmaSig.Configure.RfSettings.enpMode
			- method RsCmwWcdmaSig.Configure.RfSettings.envelopePower
			- method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Eattenuation.inputPy \n
			:return: user_margin: Range: 0 dB to (34 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:MARGin?')
		return Conversions.str_to_float(response)

	def set_margin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:RFSettings:MARGin \n
		Snippet: driver.configure.rfSettings.set_margin(user_margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode. The
		reference level minus the external input attenuation must be within the power range of the selected input connector;
		refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwWcdmaSig.Configure.RfSettings.enpMode
			- method RsCmwWcdmaSig.Configure.RfSettings.envelopePower
			- method RsCmwWcdmaSig.Configure.RfSettings.Carrier.Eattenuation.inputPy \n
			:param user_margin: Range: 0 dB to (34 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:RFSettings:MARGin {param}')

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
