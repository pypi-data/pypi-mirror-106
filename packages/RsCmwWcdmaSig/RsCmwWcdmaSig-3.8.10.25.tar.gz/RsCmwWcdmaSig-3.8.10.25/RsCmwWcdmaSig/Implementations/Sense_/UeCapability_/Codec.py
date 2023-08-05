from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Codec:
	"""Codec commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("codec", core, parent)

	# noinspection PyTypeChecker
	def get_gsm(self) -> List[enums.YesNoStatus]:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:CODec:GSM \n
		Snippet: value: List[enums.YesNoStatus] = driver.sense.ueCapability.codec.get_gsm() \n
		Indicates codec list supported by the UE in GSM and UMTS networks. The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
			:return: supported: NO | YES 14 values indicate support for: 1: GSM FR 2: GSM HR 3: GSM EFR 4: FR AMR 5: HR AMR 6: UMTS AMR 7: UMTS AMR 2 8: TDMA EFR 9: PDC EFR 10: FR AMR-WB 11: UMTS AMR-WB 12: OHR AMR 13: OFR AMR-WB 14: OHR AMR-WB
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UECapability:CODec:GSM?')
		return Conversions.str_to_list_enum(response, enums.YesNoStatus)

	# noinspection PyTypeChecker
	def get_umts(self) -> List[enums.YesNoStatus]:
		"""SCPI: SENSe:WCDMa:SIGNaling<instance>:UECapability:CODec:UMTS \n
		Snippet: value: List[enums.YesNoStatus] = driver.sense.ueCapability.codec.get_umts() \n
		Indicates codec list supported by the UE in GSM and UMTS networks. The number to the left of each result parameter is
		provided for easy identification of the parameter position within the result array. \n
			:return: supported: NO | YES 14 values indicate support for: 1: GSM FR 2: GSM HR 3: GSM EFR 4: FR AMR 5: HR AMR 6: UMTS AMR 7: UMTS AMR 2 8: TDMA EFR 9: PDC EFR 10: FR AMR-WB 11: UMTS AMR-WB 12: OHR AMR 13: OFR AMR-WB 14: OHR AMR-WB
		"""
		response = self._core.io.query_str('SENSe:WCDMa:SIGNaling<Instance>:UECapability:CODec:UMTS?')
		return Conversions.str_to_list_enum(response, enums.YesNoStatus)
