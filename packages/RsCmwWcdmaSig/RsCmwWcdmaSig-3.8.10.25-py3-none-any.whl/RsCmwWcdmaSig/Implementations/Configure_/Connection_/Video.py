from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("video", core, parent)

	# noinspection PyTypeChecker
	def get_drate(self) -> enums.VideoRate:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CONNection:VIDeo:DRATe \n
		Snippet: value: enums.VideoRate = driver.configure.connection.video.get_drate() \n
		Queries the data rate for video calls. \n
			:return: rate: R64K R64K: 64 kbps
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CONNection:VIDeo:DRATe?')
		return Conversions.str_to_scalar_enum(response, enums.VideoRate)
