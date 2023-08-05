from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:EXECute \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.execute.set() \n
		Triggers the execution of a single absolute grant pattern (repetition ONCE) . \n
		Global Repeated Capabilities: repcap.Carrier
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:EXECute')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSUPa:EAGCh:PATTern:EXECute \n
		Snippet: driver.configure.cell.carrier.hsupa.eagch.pattern.execute.set_with_opc() \n
		Triggers the execution of a single absolute grant pattern (repetition ONCE) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		Global Repeated Capabilities: repcap.Carrier
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSUPa:EAGCh:PATTern:EXECute')
