from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Precondition:
	"""Precondition commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("precondition", core, parent)

	# noinspection PyTypeChecker
	def get_phdown(self) -> enums.ConditionB:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:PHDown \n
		Snippet: value: enums.ConditionB = driver.configure.uplink.tpcset.precondition.get_phdown() \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:return: condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:PHDown?')
		return Conversions.str_to_scalar_enum(response, enums.ConditionB)

	def set_phdown(self, condition: enums.ConditionB) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:PHDown \n
		Snippet: driver.configure.uplink.tpcset.precondition.set_phdown(condition = enums.ConditionB.ALTernating) \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:param condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.ConditionB)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:PHDown {param}')

	# noinspection PyTypeChecker
	def get_phup(self) -> enums.ConditionB:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:PHUP \n
		Snippet: value: enums.ConditionB = driver.configure.uplink.tpcset.precondition.get_phup() \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:return: condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:PHUP?')
		return Conversions.str_to_scalar_enum(response, enums.ConditionB)

	def set_phup(self, condition: enums.ConditionB) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:PHUP \n
		Snippet: driver.configure.uplink.tpcset.precondition.set_phup(condition = enums.ConditionB.ALTernating) \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:param condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.ConditionB)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:PHUP {param}')

	# noinspection PyTypeChecker
	def get_continuous(self) -> enums.Condition:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:CONTinuous \n
		Snippet: value: enums.Condition = driver.configure.uplink.tpcset.precondition.get_continuous() \n
		Select the precondition for 'Continuous Pattern'. \n
			:return: condition: NONE | ALTernating | MAXPower | MINPower | TPOWer
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:CONTinuous?')
		return Conversions.str_to_scalar_enum(response, enums.Condition)

	def set_continuous(self, condition: enums.Condition) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:CONTinuous \n
		Snippet: driver.configure.uplink.tpcset.precondition.set_continuous(condition = enums.Condition.ALTernating) \n
		Select the precondition for 'Continuous Pattern'. \n
			:param condition: NONE | ALTernating | MAXPower | MINPower | TPOWer
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.Condition)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:CONTinuous {param}')

	# noinspection PyTypeChecker
	def get_single(self) -> enums.ConditionB:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:SINGle \n
		Snippet: value: enums.ConditionB = driver.configure.uplink.tpcset.precondition.get_single() \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:return: condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:SINGle?')
		return Conversions.str_to_scalar_enum(response, enums.ConditionB)

	def set_single(self, condition: enums.ConditionB) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPCSet:PRECondition:SINGle \n
		Snippet: driver.configure.uplink.tpcset.precondition.set_single(condition = enums.ConditionB.ALTernating) \n
		Select the preconditions for 'Single Pattern', 'Phase Discontinuity Up' and 'Phase Discontinuity Down'. \n
			:param condition: ALTernating | MAXPower | MINPower | TPOWer
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.ConditionB)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPCSet:PRECondition:SINGle {param}')
