from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timeout:
	"""Timeout commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("timeout", core, parent)

	@property
	def n(self):
		"""n commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n'):
			from .Timeout_.N import N
			self._n = N(self._core, self._base)
		return self._n

	@property
	def t(self):
		"""t commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_t'):
			from .Timeout_.T import T
			self._t = T(self._core, self._base)
		return self._t

	def get_moc(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:MOC \n
		Snippet: value: int = driver.configure.cell.timeout.get_moc() \n
		Defines the time period of R&S CMW alerting state. \n
			:return: timeout: 0: the alerting state is skipped 1 to 255: time period the R&S CMW waits before changes to 'Call Established' state Range: 0 to 255, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:MOC?')
		return Conversions.str_to_int(response)

	def set_moc(self, timeout: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:MOC \n
		Snippet: driver.configure.cell.timeout.set_moc(timeout = 1) \n
		Defines the time period of R&S CMW alerting state. \n
			:param timeout: 0: the alerting state is skipped 1 to 255: time period the R&S CMW waits before changes to 'Call Established' state Range: 0 to 255, Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:MOC {param}')

	def get_at_offset(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:ATOFfset \n
		Snippet: value: int = driver.configure.cell.timeout.get_at_offset() \n
		Specifies a delay value, used by the RRC for calculation of the activation time in peer messages. Low values correspond
		to fast signaling, high values to slow signaling. \n
			:return: offset: Range: 0 to 10
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:ATOFfset?')
		return Conversions.str_to_int(response)

	def set_at_offset(self, offset: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:ATOFfset \n
		Snippet: driver.configure.cell.timeout.set_at_offset(offset = 1) \n
		Specifies a delay value, used by the RRC for calculation of the activation time in peer messages. Low values correspond
		to fast signaling, high values to slow signaling. \n
			:param offset: Range: 0 to 10
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:ATOFfset {param}')

	def get_ppif(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:PPIF \n
		Snippet: value: int = driver.configure.cell.timeout.get_ppif() \n
		Number of paging indicators that the R&S CMW transmits in each PICH frame. \n
			:return: indications: 18 | 36 | 72 | 144
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:PPIF?')
		return Conversions.str_to_int(response)

	def set_ppif(self, indications: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:PPIF \n
		Snippet: driver.configure.cell.timeout.set_ppif(indications = 1) \n
		Number of paging indicators that the R&S CMW transmits in each PICH frame. \n
			:param indications: 18 | 36 | 72 | 144
		"""
		param = Conversions.decimal_value_to_str(indications)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:PPIF {param}')

	def get_prepetitions(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:PREPetitions \n
		Snippet: value: int = driver.configure.cell.timeout.get_prepetitions() \n
		Specifies the number of paging procedures to be performed if the UE does not answer paging. \n
			:return: repetitions: Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:PREPetitions?')
		return Conversions.str_to_int(response)

	def set_prepetitions(self, repetitions: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:PREPetitions \n
		Snippet: driver.configure.cell.timeout.set_prepetitions(repetitions = 1) \n
		Specifies the number of paging procedures to be performed if the UE does not answer paging. \n
			:param repetitions: Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(repetitions)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:PREPetitions {param}')

	def get_osynch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:OSYNch \n
		Snippet: value: int = driver.configure.cell.timeout.get_osynch() \n
		Sets the out-of-synchronization timeout value. This value specifies the time after which the instrument, having waited
		for a signal from the connected UE, releases the connection and returns to state registered. \n
			:return: value: Range: 2 s to 25 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:OSYNch?')
		return Conversions.str_to_int(response)

	def set_osynch(self, value: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:TOUT:OSYNch \n
		Snippet: driver.configure.cell.timeout.set_osynch(value = 1) \n
		Sets the out-of-synchronization timeout value. This value specifies the time after which the instrument, having waited
		for a signal from the connected UE, releases the connection and returns to state registered. \n
			:param value: Range: 2 s to 25 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:TOUT:OSYNch {param}')

	def clone(self) -> 'Timeout':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Timeout(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
