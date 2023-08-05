from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pexecute:
	"""Pexecute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pexecute", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PEXecute \n
		Snippet: driver.configure.uplink.tpc.pexecute.set() \n
		Execute the active TPC pattern setup. Corresponds to pressing the 'Execute' button. For pattern setups with precondition,
		it is recommended to press the 'Precond.' button first (method RsCmwWcdmaSig.Configure.Uplink.Tpc.Precondition.set) . \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PEXecute')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:TPC:PEXecute \n
		Snippet: driver.configure.uplink.tpc.pexecute.set_with_opc() \n
		Execute the active TPC pattern setup. Corresponds to pressing the 'Execute' button. For pattern setups with precondition,
		it is recommended to press the 'Precond.' button first (method RsCmwWcdmaSig.Configure.Uplink.Tpc.Precondition.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:TPC:PEXecute')
