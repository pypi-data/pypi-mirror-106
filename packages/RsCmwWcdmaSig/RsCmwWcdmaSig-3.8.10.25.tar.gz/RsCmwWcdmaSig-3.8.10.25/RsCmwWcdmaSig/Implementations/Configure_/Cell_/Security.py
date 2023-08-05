from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Security:
	"""Security commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("security", core, parent)

	# noinspection PyTypeChecker
	def get_ciphering(self) -> enums.Cipher:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:CIPHering \n
		Snippet: value: enums.Cipher = driver.configure.cell.security.get_ciphering() \n
		Specifies ciphering to be used for a radio bearer. \n
			:return: cipher: UEA0 | UEA1 | UEA2 UEA0: no ciphering UEA1: algorithm 1 (KASUMI) UEA2: algorithm 2 (SNOW 3G)
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:CIPHering?')
		return Conversions.str_to_scalar_enum(response, enums.Cipher)

	def set_ciphering(self, cipher: enums.Cipher) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:CIPHering \n
		Snippet: driver.configure.cell.security.set_ciphering(cipher = enums.Cipher.UEA0) \n
		Specifies ciphering to be used for a radio bearer. \n
			:param cipher: UEA0 | UEA1 | UEA2 UEA0: no ciphering UEA1: algorithm 1 (KASUMI) UEA2: algorithm 2 (SNOW 3G)
		"""
		param = Conversions.enum_scalar_to_str(cipher, enums.Cipher)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:CIPHering {param}')

	def get_opc(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:OPC \n
		Snippet: value: float = driver.configure.cell.security.get_opc() \n
		Specifies the key OPc as 32-digit hexadecimal number. \n
			:return: opc: Range: #H00000000000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:OPC?')
		return Conversions.str_to_float(response)

	def set_opc(self, opc: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:OPC \n
		Snippet: driver.configure.cell.security.set_opc(opc = 1.0) \n
		Specifies the key OPc as 32-digit hexadecimal number. \n
			:param opc: Range: #H00000000000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(opc)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:OPC {param}')

	# noinspection PyTypeChecker
	def get_sim_card(self) -> enums.SimCardType:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:SIMCard \n
		Snippet: value: enums.SimCardType = driver.configure.cell.security.get_sim_card() \n
		Selects the type of the SIM card used for registration. \n
			:return: sim_card_type: C3G | C2G | MILenage C3G: 3G USIM C2G: 2G SIM MILenage: USIM with MILENAGE algorithm set
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:SIMCard?')
		return Conversions.str_to_scalar_enum(response, enums.SimCardType)

	def set_sim_card(self, sim_card_type: enums.SimCardType) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:SIMCard \n
		Snippet: driver.configure.cell.security.set_sim_card(sim_card_type = enums.SimCardType.C2G) \n
		Selects the type of the SIM card used for registration. \n
			:param sim_card_type: C3G | C2G | MILenage C3G: 3G USIM C2G: 2G SIM MILenage: USIM with MILENAGE algorithm set
		"""
		param = Conversions.enum_scalar_to_str(sim_card_type, enums.SimCardType)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:SIMCard {param}')

	def get_skey(self) -> float:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: value: float = driver.configure.cell.security.get_skey() \n
		Defines the secret key K as 32-digit hexadecimal number. Leading zeros can be omitted. K is used for the authentication
		procedure including a possible integrity check. \n
			:return: secret_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:SKEY?')
		return Conversions.str_to_float(response)

	def set_skey(self, secret_key: float) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:SKEY \n
		Snippet: driver.configure.cell.security.set_skey(secret_key = 1.0) \n
		Defines the secret key K as 32-digit hexadecimal number. Leading zeros can be omitted. K is used for the authentication
		procedure including a possible integrity check. \n
			:param secret_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(secret_key)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:SKEY {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:ENABle \n
		Snippet: value: bool = driver.configure.cell.security.get_enable() \n
		Enables or disables the security mode during authentication. With enabled security mode, the UE performs an integrity
		check. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:ENABle \n
		Snippet: driver.configure.cell.security.set_enable(enable = False) \n
		Enables or disables the security mode during authentication. With enabled security mode, the UE performs an integrity
		check. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:ENABle {param}')

	def get_authenticate(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:AUTHenticat \n
		Snippet: value: bool = driver.configure.cell.security.get_authenticate() \n
		Enables or disables authentication, to be performed during registration. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:AUTHenticat?')
		return Conversions.str_to_bool(response)

	def set_authenticate(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:SECurity:AUTHenticat \n
		Snippet: driver.configure.cell.security.set_authenticate(enable = False) \n
		Enables or disables authentication, to be performed during registration. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:SECurity:AUTHenticat {param}')
