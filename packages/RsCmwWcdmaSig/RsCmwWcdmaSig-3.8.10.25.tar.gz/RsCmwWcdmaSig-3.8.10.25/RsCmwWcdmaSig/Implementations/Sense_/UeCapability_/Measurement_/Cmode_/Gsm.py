from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gsm:
	"""Gsm commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gsm", core, parent)

	# noinspection PyTypeChecker
	def get(self, band: enums.CompressedModeBand) -> List[enums.CompressedMode]:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:MEASurement:CMODe:GSM \n
		Snippet: value: List[enums.CompressedMode] = driver.sense.ueCapability.measurement.cmode.gsm.get(band = enums.CompressedModeBand.OB1) \n
		Returns the UE capabilities for GSM neighbor cell measurements-related compressed mode. \n
			:param band: OB1 | OB2 | OB3 | OB4 | OB5 | OB6 | OB7 | OB8 | OB9 | OB10 | OB11 | OB12 | OB13 | OB14 | OB15 | OB16 | OB17 | OB18 | OB19 | OB20 | OB21 | OB22 | OB25 | OB26 | OB32 OB1, ..., OB22: WCDMA operating band I to XXII OB25, OB26, OB32: WCDMA operating band XXV, XXVI and XXXII
			:return: compressed_mode: NN | NY | YN | YY NN: compressed mode for the neighbor cell measurement not required (UL and DL) NY: compressed mode for the neighbor cell measurement required in DL only YN: compressed mode for the neighbor cell measurement required in UL only YY: compressed mode for the neighbor cell measurement required in UL and DL"""
		param = Conversions.enum_scalar_to_str(band, enums.CompressedModeBand)
		response = self._core.io.query_str(f'SENSe:WCDMa:SIGNaling<Instance>:UECapability:MEASurement:CMODe:GSM? {param}')
		return Conversions.str_to_list_enum(response, enums.CompressedMode)
