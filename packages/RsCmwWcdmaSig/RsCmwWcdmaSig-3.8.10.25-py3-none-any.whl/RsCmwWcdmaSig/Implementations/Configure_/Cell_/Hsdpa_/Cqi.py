from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqi:
	"""Cqi commands group definition. 12 total commands, 2 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cqi", core, parent)

	@property
	def conformance(self):
		"""conformance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conformance'):
			from .Cqi_.Conformance import Conformance
			self._conformance = Conformance(self._core, self._base)
		return self._conformance

	@property
	def rvcSequences(self):
		"""rvcSequences commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rvcSequences'):
			from .Cqi_.RvcSequences import RvcSequences
			self._rvcSequences = RvcSequences(self._core, self._base)
		return self._rvcSequences

	def get_rfactor(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:RFACtor \n
		Snippet: value: int = driver.configure.cell.hsdpa.cqi.get_rfactor() \n
		Specifies how often the UE transmits the same CQI value per feedback cycle (CQI repetition factor) . \n
			:return: factor: Range: 1 to 4
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:RFACtor?')
		return Conversions.str_to_int(response)

	def set_rfactor(self, factor: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:RFACtor \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_rfactor(factor = 1) \n
		Specifies how often the UE transmits the same CQI value per feedback cycle (CQI repetition factor) . \n
			:param factor: Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(factor)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:RFACtor {param}')

	def get_fb_cycle(self) -> float or bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:FBCYcle \n
		Snippet: value: float or bool = driver.configure.cell.hsdpa.cqi.get_fb_cycle() \n
		Specifies the time after which the UE sends a new CQI value on the HS-DPCCH (CQI feedback cycle) . The CQI transmission
		can also be disabled completely. \n
			:return: feedback_cycle: Range: 2 ms to 160 ms, Unit: s Additional parameters: OFF | ON (disables | enables CQI transmission)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:FBCYcle?')
		return Conversions.str_to_float_or_bool(response)

	def set_fb_cycle(self, feedback_cycle: float or bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:FBCYcle \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_fb_cycle(feedback_cycle = 1.0) \n
		Specifies the time after which the UE sends a new CQI value on the HS-DPCCH (CQI feedback cycle) . The CQI transmission
		can also be disabled completely. \n
			:param feedback_cycle: Range: 2 ms to 160 ms, Unit: s Additional parameters: OFF | ON (disables | enables CQI transmission)
		"""
		param = Conversions.decimal_or_bool_value_to_str(feedback_cycle)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:FBCYcle {param}')

	def get_tti(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:TTI \n
		Snippet: value: int = driver.configure.cell.hsdpa.cqi.get_tti() \n
		Queries the minimum distance between two consecutive transmission time intervals in which the HS-DSCH is allocated to the
		UE. \n
			:return: tti: Range: 1 to 3
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:TTI?')
		return Conversions.str_to_int(response)

	def get_harq(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:HARQ \n
		Snippet: value: int = driver.configure.cell.hsdpa.cqi.get_harq() \n
		Specifies the number of HARQ processes. \n
			:return: number: Range: 1 to 8
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:HARQ?')
		return Conversions.str_to_int(response)

	def set_harq(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:HARQ \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_harq(number = 1) \n
		Specifies the number of HARQ processes. \n
			:param number: Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:HARQ {param}')

	# noinspection PyTypeChecker
	def get_tindex(self) -> enums.TableIndex:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:TINDex \n
		Snippet: value: enums.TableIndex = driver.configure.cell.hsdpa.cqi.get_tindex() \n
		Specifies the method to be used for selection of the CQI table index. \n
			:return: table_index: FIXed | SEQuence | CONFormance | FOLLow FIXed A fixed mapping table row is used. See also method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsdpa.Cqi.fixed SEQuence A sequence of mapping table rows is used. See also method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.sequence CONFormance A CQI reporting test is to be performed. See also method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsdpa.Cqi.conformance FOLLow The CQI value to be used is proposed by the UE. See also method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.follow
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:TINDex?')
		return Conversions.str_to_scalar_enum(response, enums.TableIndex)

	def set_tindex(self, table_index: enums.TableIndex) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:TINDex \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_tindex(table_index = enums.TableIndex.CONFormance) \n
		Specifies the method to be used for selection of the CQI table index. \n
			:param table_index: FIXed | SEQuence | CONFormance | FOLLow FIXed A fixed mapping table row is used. See also method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsdpa.Cqi.fixed SEQuence A sequence of mapping table rows is used. See also method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.sequence CONFormance A CQI reporting test is to be performed. See also method RsCmwWcdmaSig.Configure.Cell.Carrier.Hsdpa.Cqi.conformance FOLLow The CQI value to be used is proposed by the UE. See also method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.follow
		"""
		param = Conversions.enum_scalar_to_str(table_index, enums.TableIndex)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:TINDex {param}')

	# noinspection PyTypeChecker
	class SequenceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Min_Value: int: Range: 1 to 30
			- Max_Value: int: Range: 1 to 30"""
		__meta_args_list = [
			ArgStruct.scalar_int('Min_Value'),
			ArgStruct.scalar_int('Max_Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Value: int = None
			self.Max_Value: int = None

	def get_sequence(self) -> SequenceStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:SEQuence \n
		Snippet: value: SequenceStruct = driver.configure.cell.hsdpa.cqi.get_sequence() \n
		Selects the range of CQI table indices to be used cyclically if SEQuence is configured via method RsCmwWcdmaSig.Configure.
		Cell.Hsdpa.Cqi.tindex. \n
			:return: structure: for return value, see the help for SequenceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:SEQuence?', self.__class__.SequenceStruct())

	def set_sequence(self, value: SequenceStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:SEQuence \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_sequence(value = SequenceStruct()) \n
		Selects the range of CQI table indices to be used cyclically if SEQuence is configured via method RsCmwWcdmaSig.Configure.
		Cell.Hsdpa.Cqi.tindex. \n
			:param value: see the help for SequenceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:SEQuence', value)

	# noinspection PyTypeChecker
	class FollowStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Min_Value: int: Range: 1 to 30
			- Max_Value: int: Range: 1 to 30"""
		__meta_args_list = [
			ArgStruct.scalar_int('Min_Value'),
			ArgStruct.scalar_int('Max_Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Value: int = None
			self.Max_Value: int = None

	def get_follow(self) -> FollowStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:FOLLow \n
		Snippet: value: FollowStruct = driver.configure.cell.hsdpa.cqi.get_follow() \n
		Defines the allowed range of CQI table indices. A value proposed by the UE is accepted if it is located within the range
		and FOLLow is configured via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.tindex. \n
			:return: structure: for return value, see the help for FollowStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:FOLLow?', self.__class__.FollowStruct())

	def set_follow(self, value: FollowStruct) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:CQI:FOLLow \n
		Snippet: driver.configure.cell.hsdpa.cqi.set_follow(value = FollowStruct()) \n
		Defines the allowed range of CQI table indices. A value proposed by the UE is accepted if it is located within the range
		and FOLLow is configured via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.Cqi.tindex. \n
			:param value: see the help for FollowStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:CQI:FOLLow', value)

	def clone(self) -> 'Cqi':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cqi(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
