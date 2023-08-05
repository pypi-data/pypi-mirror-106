from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	# noinspection PyTypeChecker
	def get_crelease(self) -> enums.CallRelease:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:CSWitched:CRELease \n
		Snippet: value: enums.CallRelease = driver.configure.connection.cswitched.get_crelease() \n
		Specifies the signaling volume during the call release. \n
			:return: call_release: NORMal | LOCal NORMal: normal release LOCal: local end release without signaling
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:CRELease?')
		return Conversions.str_to_scalar_enum(response, enums.CallRelease)

	def set_crelease(self, call_release: enums.CallRelease) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:CSWitched:CRELease \n
		Snippet: driver.configure.connection.cswitched.set_crelease(call_release = enums.CallRelease.LOCal) \n
		Specifies the signaling volume during the call release. \n
			:param call_release: NORMal | LOCal NORMal: normal release LOCal: local end release without signaling
		"""
		param = Conversions.enum_scalar_to_str(call_release, enums.CallRelease)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CONNection:CSWitched:CRELease {param}')
