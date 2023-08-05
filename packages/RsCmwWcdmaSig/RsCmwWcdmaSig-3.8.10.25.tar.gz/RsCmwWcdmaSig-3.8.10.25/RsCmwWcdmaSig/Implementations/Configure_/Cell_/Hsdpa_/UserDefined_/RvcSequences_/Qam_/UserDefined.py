from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefined:
	"""UserDefined commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("userDefined", core, parent)

	# noinspection PyTypeChecker
	class UserDefinedStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Length: int: The first Length entries of the user defined coding sequence are used. Range: 1 to 8
			- Sequence: List[int]: Up to 8 values separated by commas. If you specify n values, they overwrite the first n entries of the user-defined sequence. Range: 0 to 7"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct('Sequence', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Sequence: List[int] = None

	def set(self, structure: UserDefinedStruct, quadratureAM=repcap.QuadratureAM.Default) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM<nr>:UDEFined \n
		Snippet: driver.configure.cell.hsdpa.userDefined.rvcSequences.qam.userDefined.set(value = [PROPERTY_STRUCT_NAME](), quadratureAM = repcap.QuadratureAM.Default) \n
		Specifies an RV coding sequence to be used for signals with 16-QAM or 64-QAM modulation if UDEFined is set via
		CONFigure:WCDMa:SIGN<i>:CELL:HSDPa:UDEFined:RVCSequences:QAM<no>. \n
			:param structure: for set value, see the help for UserDefinedStruct structure arguments.
			:param quadratureAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Qam')"""
		quadratureAM_cmd_val = self._base.get_repcap_cmd_value(quadratureAM, repcap.QuadratureAM)
		self._core.io.write_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM{quadratureAM_cmd_val}:UDEFined', structure)

	def get(self, quadratureAM=repcap.QuadratureAM.Default) -> UserDefinedStruct:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM<nr>:UDEFined \n
		Snippet: value: UserDefinedStruct = driver.configure.cell.hsdpa.userDefined.rvcSequences.qam.userDefined.get(quadratureAM = repcap.QuadratureAM.Default) \n
		Specifies an RV coding sequence to be used for signals with 16-QAM or 64-QAM modulation if UDEFined is set via
		CONFigure:WCDMa:SIGN<i>:CELL:HSDPa:UDEFined:RVCSequences:QAM<no>. \n
			:param quadratureAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for UserDefinedStruct structure arguments."""
		quadratureAM_cmd_val = self._base.get_repcap_cmd_value(quadratureAM, repcap.QuadratureAM)
		return self._core.io.query_struct(f'CONFigure:WCDMa:SIGNaling<Instance>:CELL:HSDPa:UDEFined:RVCSequences:QAM{quadratureAM_cmd_val}:UDEFined?', self.__class__.UserDefinedStruct())
