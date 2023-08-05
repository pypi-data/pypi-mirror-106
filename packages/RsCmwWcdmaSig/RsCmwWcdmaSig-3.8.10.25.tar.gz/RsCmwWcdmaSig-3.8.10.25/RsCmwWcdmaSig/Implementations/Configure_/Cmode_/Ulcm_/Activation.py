from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Activation:
	"""Activation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("activation", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:ULCM:ACTivation \n
		Snippet: driver.configure.cmode.ulcm.activation.set() \n
		Activates the selected pattern type for the UL compressed mode TX test. \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:ULCM:ACTivation')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CMODe:ULCM:ACTivation \n
		Snippet: driver.configure.cmode.ulcm.activation.set_with_opc() \n
		Activates the selected pattern type for the UL compressed mode TX test. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:CMODe:ULCM:ACTivation')
