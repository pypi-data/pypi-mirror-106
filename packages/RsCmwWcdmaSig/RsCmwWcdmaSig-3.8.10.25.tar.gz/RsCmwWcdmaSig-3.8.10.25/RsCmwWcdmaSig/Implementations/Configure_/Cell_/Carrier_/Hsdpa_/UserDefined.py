from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	@property
	def tblock(self):
		"""tblock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tblock'):
			from .UserDefined_.Tblock import Tblock
			self._tblock = Tblock(self._core, self._base)
		return self._tblock

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:ENABle \n
		Snippet: value: bool = driver.configure.cell.carrier.hsdpa.userDefined.get_enable() \n
		Enables or disables the multi-carrier operation for data transport via additional HS-DSCH. \n
			:return: enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:ENABle \n
		Snippet: driver.configure.cell.carrier.hsdpa.userDefined.set_enable(enable = False) \n
		Enables or disables the multi-carrier operation for data transport via additional HS-DSCH. \n
			:param enable: OFF | ON
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:ENABle {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.HsdpaModulation:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:MODulation \n
		Snippet: value: enums.HsdpaModulation = driver.configure.cell.carrier.hsdpa.userDefined.get_modulation() \n
		Selects the modulation scheme to be used. \n
			:return: modulation: QPSK | Q16 | Q64 QPSK, 16-QAM, 64-QAM
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.HsdpaModulation)

	def set_modulation(self, modulation: enums.HsdpaModulation) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:MODulation \n
		Snippet: driver.configure.cell.carrier.hsdpa.userDefined.set_modulation(modulation = enums.HsdpaModulation.Q16) \n
		Selects the modulation scheme to be used. \n
			:param modulation: QPSK | Q16 | Q64 QPSK, 16-QAM, 64-QAM
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.enum_scalar_to_str(modulation, enums.HsdpaModulation)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:MODulation {param}')

	def get_ncodes(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:NCODes \n
		Snippet: value: int = driver.configure.cell.carrier.hsdpa.userDefined.get_ncodes() \n
		Specifies the number of HS-PDSCH channelization codes to be assigned to the UE. \n
			:return: number: Range: 1 to 15
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:NCODes?')
		return Conversions.str_to_int(response)

	def set_ncodes(self, number: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:NCODes \n
		Snippet: driver.configure.cell.carrier.hsdpa.userDefined.set_ncodes(number = 1) \n
		Specifies the number of HS-PDSCH channelization codes to be assigned to the UE. \n
			:param number: Range: 1 to 15
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:NCODes {param}')

	def get_tti(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:TTI \n
		Snippet: value: int = driver.configure.cell.carrier.hsdpa.userDefined.get_tti() \n
		Specifies the minimum distance between two consecutive transmission time intervals in which the HS-DSCH is allocated to
		the UE. \n
			:return: tti: Range: 1 to 3
		Global Repeated Capabilities: repcap.Carrier"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:TTI?')
		return Conversions.str_to_int(response)

	def set_tti(self, tti: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:CARRier<carrier>:HSDPa:UDEFined:TTI \n
		Snippet: driver.configure.cell.carrier.hsdpa.userDefined.set_tti(tti = 1) \n
		Specifies the minimum distance between two consecutive transmission time intervals in which the HS-DSCH is allocated to
		the UE. \n
			:param tti: Range: 1 to 3
		Global Repeated Capabilities: repcap.Carrier"""
		param = Conversions.decimal_value_to_str(tti)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:CARRier<Carrier>:HSDPa:UDEFined:TTI {param}')

	def clone(self) -> 'UserDefined':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefined(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
