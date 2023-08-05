from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qam:
	"""Qam commands group definition. 2 total commands, 1 Sub-groups, 1 group commands
	Repeated Capability: QuadratureAM, default value after init: QuadratureAM.QAM16"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qam", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_quadratureAM_get', 'repcap_quadratureAM_set', repcap.QuadratureAM.QAM16)

	def repcap_quadratureAM_set(self, enum_value: repcap.QuadratureAM) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to QuadratureAM.Default
		Default value after init: QuadratureAM.QAM16"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_quadratureAM_get(self) -> repcap.QuadratureAM:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def userDefined(self):
		"""userDefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_userDefined'):
			from .Qam_.UserDefined import UserDefined
			self._userDefined = UserDefined(self._core, self._base)
		return self._userDefined

	def set(self, sequence: enums.RvcSequence, quadratureAM=repcap.QuadratureAM.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM<nr> \n
		Snippet: driver.configure.cell.hsdpa.userDefined.rvcSequences.qam.set(sequence = enums.RvcSequence.S1, quadratureAM = repcap.QuadratureAM.Default) \n
		Specifies an RV coding sequence to be used for signals with 16-QAM or 64-QAM modulation. If UDEFined is selected, the
		sequence is defined via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qam.UserDefined.set. \n
			:param sequence: S1 | S2 | S3 | S4 | S5 | S6 | S7 | UDEFined S1: {0} S2: {6} S3: {0, 2, 5, 6} S4: {6, 2, 1, 5} S5: {0, 0, 0, 0} S6: {6, 6, 6, 6} S7: {6, 0, 4, 5} UDEFined: user-defined sequence
			:param quadratureAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Qam')"""
		param = Conversions.enum_scalar_to_str(sequence, enums.RvcSequence)
		quadratureAM_cmd_val = self._base.get_repcap_cmd_value(quadratureAM, repcap.QuadratureAM)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM{quadratureAM_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, quadratureAM=repcap.QuadratureAM.Default) -> enums.RvcSequence:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM<nr> \n
		Snippet: value: enums.RvcSequence = driver.configure.cell.hsdpa.userDefined.rvcSequences.qam.get(quadratureAM = repcap.QuadratureAM.Default) \n
		Specifies an RV coding sequence to be used for signals with 16-QAM or 64-QAM modulation. If UDEFined is selected, the
		sequence is defined via method RsCmwWcdmaSig.Configure.Cell.Hsdpa.UserDefined.RvcSequences.Qam.UserDefined.set. \n
			:param quadratureAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Qam')
			:return: sequence: S1 | S2 | S3 | S4 | S5 | S6 | S7 | UDEFined S1: {0} S2: {6} S3: {0, 2, 5, 6} S4: {6, 2, 1, 5} S5: {0, 0, 0, 0} S6: {6, 6, 6, 6} S7: {6, 0, 4, 5} UDEFined: user-defined sequence"""
		quadratureAM_cmd_val = self._base.get_repcap_cmd_value(quadratureAM, repcap.QuadratureAM)
		response = self._core.io.query_str(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM{quadratureAM_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.RvcSequence)

	def clone(self) -> 'Qam':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qam(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
