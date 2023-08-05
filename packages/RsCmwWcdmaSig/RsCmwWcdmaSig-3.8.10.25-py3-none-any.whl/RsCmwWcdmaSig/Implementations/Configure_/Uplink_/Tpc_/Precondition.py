from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Precondition:
	"""Precondition commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("precondition", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PRECondition \n
		Snippet: driver.configure.uplink.tpc.precondition.set() \n
		Reach the precondition defined for the active TPC pattern setup. Corresponds to pressing the 'Precond.' button. \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PRECondition')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PRECondition \n
		Snippet: driver.configure.uplink.tpc.precondition.set_with_opc() \n
		Reach the precondition defined for the active TPC pattern setup. Corresponds to pressing the 'Precond.' button. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PRECondition')
