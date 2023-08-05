from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("set", core, parent)

	def set(self, set_type: enums.TpcSetType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:SET \n
		Snippet: driver.configure.uplink.tpc.set.set(set_type = enums.TpcSetType.ALL0) \n
		Selects the active TPC setup. A query returns also properties of the active setup. \n
			:param set_type: CLOop | ALTernating | ALL1 | ALL0 | SALT | SAL1 | SAL0 | CONTinuous | TSE | TSF | PHUP | PHDown | TSABc | TSEF | TSGH | MPEDch | ULCM | CTFC | DHIB CLOop: 'Closed Loop' ALTernating: 'Alternating' ALL1: 'All 1' ALL0: 'All 0' SALT: 'Single Pattern + Alternating' SAL1: 'Single Pattern + All 1' SAL0: 'Single Pattern + All 0' CONTinuous: 'Continuous Pattern' TSE: 'TPC Test Step E' TSF: 'TPC Test Step F' PHUP: 'Phase Discontinuity Up' PHDown: 'Phase Discontinuity Down' TSABc: 'TPC Test Step ABC' TSEF: 'TPC Test Step EF' TSGH: 'TPC Test Step GH' MPEDch: 'Max. Power E-DCH' ULCM: 'TPC Test Step UL CM' CTFC: 'Change of TFC' DHIB: 'DC HSPA In-Band Emission'
		"""
		param = Conversions.enum_scalar_to_str(set_type, enums.TpcSetType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:SET {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Set_Type: enums.TpcSetType: CLOop | ALTernating | ALL1 | ALL0 | SALT | SAL1 | SAL0 | CONTinuous | TSE | TSF | PHUP | PHDown | TSABc | TSEF | TSGH | MPEDch | ULCM | CTFC | DHIB CLOop: 'Closed Loop' ALTernating: 'Alternating' ALL1: 'All 1' ALL0: 'All 0' SALT: 'Single Pattern + Alternating' SAL1: 'Single Pattern + All 1' SAL0: 'Single Pattern + All 0' CONTinuous: 'Continuous Pattern' TSE: 'TPC Test Step E' TSF: 'TPC Test Step F' PHUP: 'Phase Discontinuity Up' PHDown: 'Phase Discontinuity Down' TSABc: 'TPC Test Step ABC' TSEF: 'TPC Test Step EF' TSGH: 'TPC Test Step GH' MPEDch: 'Max. Power E-DCH' ULCM: 'TPC Test Step UL CM' CTFC: 'Change of TFC' DHIB: 'DC HSPA In-Band Emission'
			- Precondition: enums.Condition: NONE | ALTernating | MAXPower | MINPower | TPOWer Precondition of the active setup: none, alternating up and down, maximum, minimum or target power.
			- Pconfig: str: Active setup configuration information. The content depends on the setup type: - closed loop: target power in dBm - single and continuous patterns: user-defined pattern - phase discontinuity: number of repetitions - test step EF, GH: number of 0 bits - DC HSPA in-band emission: pattern selection for the carrier one and two and number of selected bits - others: presentation of the fixed pattern
			- Trigger: enums.TriggerMode: ONCE | PERiodic Type of generated trigger signal. See 'Generating TPC Trigger Signals'"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Set_Type', enums.TpcSetType),
			ArgStruct.scalar_enum('Precondition', enums.Condition),
			ArgStruct.scalar_str('Pconfig'),
			ArgStruct.scalar_enum('Trigger', enums.TriggerMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Set_Type: enums.TpcSetType = None
			self.Precondition: enums.Condition = None
			self.Pconfig: str = None
			self.Trigger: enums.TriggerMode = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:SET \n
		Snippet: value: GetStruct = driver.configure.uplink.tpc.set.get() \n
		Selects the active TPC setup. A query returns also properties of the active setup. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:SET?', self.__class__.GetStruct())
