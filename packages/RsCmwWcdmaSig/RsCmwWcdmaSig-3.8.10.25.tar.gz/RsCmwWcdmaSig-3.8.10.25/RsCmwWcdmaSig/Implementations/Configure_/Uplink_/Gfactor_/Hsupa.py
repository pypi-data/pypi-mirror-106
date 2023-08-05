from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsupa:
	"""Hsupa commands group definition. 7 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsupa", core, parent)

	@property
	def etfci(self):
		"""etfci commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_etfci'):
			from .Hsupa_.Etfci import Etfci
			self._etfci = Etfci(self._core, self._base)
		return self._etfci

	def get_edpcch(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:EDPCch \n
		Snippet: value: int = driver.configure.uplink.gfactor.hsupa.get_edpcch() \n
		Specifies the signaled value ΔE-DPCCH for HSUPA. \n
			:return: delta: Range: 0 to 8
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:EDPCch?')
		return Conversions.str_to_int(response)

	def set_edpcch(self, delta: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:EDPCch \n
		Snippet: driver.configure.uplink.gfactor.hsupa.set_edpcch(delta = 1) \n
		Specifies the signaled value ΔE-DPCCH for HSUPA. \n
			:param delta: Range: 0 to 8
		"""
		param = Conversions.decimal_value_to_str(delta)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:EDPCch {param}')

	def get_dttp(self) -> int:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:DTTP \n
		Snippet: value: int = driver.configure.uplink.gfactor.hsupa.get_dttp() \n
		Sets the offset for traffic to total pilot power. The E-DPCCH power is highest for ΔT2TP value of 0 and lowest for value
		6. \n
			:return: delta_t_2_tp: Range: 0 to 6
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:DTTP?')
		return Conversions.str_to_int(response)

	def set_dttp(self, delta_t_2_tp: int) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:DTTP \n
		Snippet: driver.configure.uplink.gfactor.hsupa.set_dttp(delta_t_2_tp = 1) \n
		Sets the offset for traffic to total pilot power. The E-DPCCH power is highest for ΔT2TP value of 0 and lowest for value
		6. \n
			:param delta_t_2_tp: Range: 0 to 6
		"""
		param = Conversions.decimal_value_to_str(delta_t_2_tp)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:DTTP {param}')

	# noinspection PyTypeChecker
	def get_edp_formula(self) -> enums.UeAlgorithm:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:EDPFormula \n
		Snippet: value: enums.UeAlgorithm = driver.configure.uplink.gfactor.hsupa.get_edp_formula() \n
		Specifies the UE algorithm for the calculation of E-DPDCH power based on the signaled reference E-TFCIs. \n
			:return: formula: EXTRapolation | INTerpolation
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:EDPFormula?')
		return Conversions.str_to_scalar_enum(response, enums.UeAlgorithm)

	def set_edp_formula(self, formula: enums.UeAlgorithm) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:UL:GFACtor:HSUPa:EDPFormula \n
		Snippet: driver.configure.uplink.gfactor.hsupa.set_edp_formula(formula = enums.UeAlgorithm.EXTRapolation) \n
		Specifies the UE algorithm for the calculation of E-DPDCH power based on the signaled reference E-TFCIs. \n
			:param formula: EXTRapolation | INTerpolation
		"""
		param = Conversions.enum_scalar_to_str(formula, enums.UeAlgorithm)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:UL:GFACtor:HSUPa:EDPFormula {param}')

	def clone(self) -> 'Hsupa':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hsupa(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
