from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sidelink:
	"""Sidelink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sidelink", core, parent)

	# noinspection PyTypeChecker
	class SidelinkStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Auto: bool: OFF: manual definition via the other settings ON: automatic detection of RB allocation
			- No_Rb_Pssch: int: Number of allocated RBs for the PSSCH in each measured slot
			- Offset_Pssch: int: Offset of the first allocated PSSCH resource block
			- Offset_Pscch: int: Offset of the first allocated PSCCH resource block"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Auto'),
			ArgStruct.scalar_int('No_Rb_Pssch'),
			ArgStruct.scalar_int('Offset_Pssch'),
			ArgStruct.scalar_int('Offset_Pscch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Auto: bool = None
			self.No_Rb_Pssch: int = None
			self.Offset_Pssch: int = None
			self.Offset_Pscch: int = None

	def set(self, structure: SidelinkStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RBALlocation:SIDelink \n
		Snippet: driver.configure.multiEval.listPy.segment.rbAllocation.sidelink.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Allows you to define the sidelink resource block allocation manually for segment <no>. By default, the RB allocation is
		detected automatically. Most allowed input ranges depend on other settings, see 'Sidelink Resource Block Allocation'. \n
			:param structure: for set value, see the help for SidelinkStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RBALlocation:SIDelink', structure)

	def get(self, segment=repcap.Segment.Default) -> SidelinkStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RBALlocation:SIDelink \n
		Snippet: value: SidelinkStruct = driver.configure.multiEval.listPy.segment.rbAllocation.sidelink.get(segment = repcap.Segment.Default) \n
		Allows you to define the sidelink resource block allocation manually for segment <no>. By default, the RB allocation is
		detected automatically. Most allowed input ranges depend on other settings, see 'Sidelink Resource Block Allocation'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SidelinkStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RBALlocation:SIDelink?', self.__class__.SidelinkStruct())
