from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adjust:
	"""Adjust commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("adjust", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:ADJust \n
		Snippet: driver.configure.downlink.level.adjust.set() \n
		Corrects the power levels of all enabled channels to minimize the difference between the total power level of the
		channels and the base level. \n
		"""
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:ADJust')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:LEVel:ADJust \n
		Snippet: driver.configure.downlink.level.adjust.set_with_opc() \n
		Corrects the power levels of all enabled channels to minimize the difference between the total power level of the
		channels and the base level. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwWcdmaSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:LEVel:ADJust')
