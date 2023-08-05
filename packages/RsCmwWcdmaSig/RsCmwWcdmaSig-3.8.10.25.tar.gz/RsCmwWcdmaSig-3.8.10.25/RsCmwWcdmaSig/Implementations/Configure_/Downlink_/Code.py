from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("code", core, parent)

	def get_scpich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:SCPich \n
		Snippet: value: int = driver.configure.downlink.code.get_scpich() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:SCPich?')
		return Conversions.str_to_int(response)

	def set_scpich(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:SCPich \n
		Snippet: driver.configure.downlink.code.set_scpich(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:SCPich {param}')

	def get_pccpch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:PCCPch \n
		Snippet: value: int = driver.configure.downlink.code.get_pccpch() \n
		Queries the channelization code number of the P-CCPCH. \n
			:return: channel_code: The returned value is fixed. Range: 1
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:PCCPch?')
		return Conversions.str_to_int(response)

	def get_sccpch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:SCCPch \n
		Snippet: value: int = driver.configure.downlink.code.get_sccpch() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:SCCPch?')
		return Conversions.str_to_int(response)

	def set_sccpch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:SCCPch \n
		Snippet: driver.configure.downlink.code.set_sccpch(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:SCCPch {param}')

	def get_pich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:PICH \n
		Snippet: value: int = driver.configure.downlink.code.get_pich() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:PICH?')
		return Conversions.str_to_int(response)

	def set_pich(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:PICH \n
		Snippet: driver.configure.downlink.code.set_pich(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:PICH {param}')

	def get_aich(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:AICH \n
		Snippet: value: int = driver.configure.downlink.code.get_aich() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:AICH?')
		return Conversions.str_to_int(response)

	def set_aich(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:AICH \n
		Snippet: driver.configure.downlink.code.set_aich(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:AICH {param}')

	def get_dpch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:DPCH \n
		Snippet: value: int = driver.configure.downlink.code.get_dpch() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:DPCH?')
		return Conversions.str_to_int(response)

	def set_dpch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:DPCH \n
		Snippet: driver.configure.downlink.code.set_dpch(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:DPCH {param}')

	def get_fdpch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:FDPCh \n
		Snippet: value: int = driver.configure.downlink.code.get_fdpch() \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:return: channel_code: Range: See table below
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:FDPCh?')
		return Conversions.str_to_int(response)

	def set_fdpch(self, channel_code: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:DL:CODE:FDPCh \n
		Snippet: driver.configure.downlink.code.set_fdpch(channel_code = 1) \n
		Set the channelization code number of the channel indicated by the last mnemonic. \n
			:param channel_code: Range: See table below
		"""
		param = Conversions.decimal_value_to_str(channel_code)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:DL:CODE:FDPCh {param}')
