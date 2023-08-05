from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psettings:
	"""Psettings commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("psettings", core, parent)

	# noinspection PyTypeChecker
	class ErgmStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Test_Mode: enums.TestMode: HOLD | UPDown 'Missed Hold', 'Missed Up/Down'
			- Tti: enums.TransTimeInterval: M2 | M10 2 ms, 10 ms"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Test_Mode', enums.TestMode),
			ArgStruct.scalar_enum('Tti', enums.TransTimeInterval)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Test_Mode: enums.TestMode = None
			self.Tti: enums.TransTimeInterval = None

	# noinspection PyTypeChecker
	def get_ergm(self) -> ErgmStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:PSETtings:ERGM \n
		Snippet: value: ErgmStruct = driver.configure.psettings.get_ergm() \n
		Selects mode and TTI for the 'E-RGCH Measurement'wizard. \n
			:return: structure: for return value, see the help for ErgmStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:PSETtings:ERGM?', self.__class__.ErgmStruct())

	def set_ergm(self, value: ErgmStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:PSETtings:ERGM \n
		Snippet: driver.configure.psettings.set_ergm(value = ErgmStruct()) \n
		Selects mode and TTI for the 'E-RGCH Measurement'wizard. \n
			:param value: see the help for ErgmStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:PSETtings:ERGM', value)

	# noinspection PyTypeChecker
	def get_hump(self) -> enums.SubTest:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:PSETtings:HUMP \n
		Snippet: value: enums.SubTest = driver.configure.psettings.get_hump() \n
		Selects a subtest for the HSUPA maximum output power wizard. \n
			:return: sub_test: S1 | S2 | S3 | S4 | S5 Subtest 1 to subtest 5
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:PSETtings:HUMP?')
		return Conversions.str_to_scalar_enum(response, enums.SubTest)

	def set_hump(self, sub_test: enums.SubTest) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:PSETtings:HUMP \n
		Snippet: driver.configure.psettings.set_hump(sub_test = enums.SubTest.S1) \n
		Selects a subtest for the HSUPA maximum output power wizard. \n
			:param sub_test: S1 | S2 | S3 | S4 | S5 Subtest 1 to subtest 5
		"""
		param = Conversions.enum_scalar_to_str(sub_test, enums.SubTest)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:PSETtings:HUMP {param}')

	def set_value(self, selection: enums.WizzardSelection) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:PSETtings \n
		Snippet: driver.configure.psettings.set_value(selection = enums.WizzardSelection.DHIP) \n
		Executes the wizard to apply the selected predefined set of WCDMA settings.
			INTRO_CMD_HELP: Configure the following selections before executing the wizard: \n
			- 'General Settings'
			- HUMP: see method RsCmwWcdmaSig.Configure.Psettings.hump
			- ERGM: see method RsCmwWcdmaSig.Configure.Psettings.ergm \n
			:param selection: HDMT | HUMT | HSMT | HUMP | DHIP | ERGM | HCQI | OOS HDMT: HSDPA maximum throughput HUMT: HSUPA maximum throughput HSMT: HSPA maximum throughput HUMP: HSUPA maximum output power DHIP: Dual carrier HSPA inner loop power control ERGM: HSUPA E-RGCH measurement HCQI: HSDPA CQI measurement OOS: Out-of-sync handling
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.WizzardSelection)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:PSETtings {param}')
