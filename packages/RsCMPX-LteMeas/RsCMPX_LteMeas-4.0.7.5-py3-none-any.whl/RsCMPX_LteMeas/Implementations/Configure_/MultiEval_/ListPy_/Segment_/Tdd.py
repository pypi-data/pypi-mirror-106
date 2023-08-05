from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdd:
	"""Tdd commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tdd", core, parent)

	# noinspection PyTypeChecker
	class TddStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Uplink_Downlink: int: UL-DL configuration, defining the combination of uplink, downlink and special subframes within a radio frame
			- Special_Subframe: int: Special subframe configuration, defining the inner structure of special subframes"""
		__meta_args_list = [
			ArgStruct.scalar_int('Uplink_Downlink'),
			ArgStruct.scalar_int('Special_Subframe')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Uplink_Downlink: int = None
			self.Special_Subframe: int = None

	def set(self, structure: TddStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:TDD \n
		Snippet: driver.configure.multiEval.listPy.segment.tdd.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines segment settings only relevant for uplink measurements with the duplex mode TDD.
		For general segment configuration, see method RsCMPX_LteMeas.Configure.MultiEval.ListPy.Segment.Setup.set. \n
			:param structure: for set value, see the help for TddStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:TDD', structure)

	def get(self, segment=repcap.Segment.Default) -> TddStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:TDD \n
		Snippet: value: TddStruct = driver.configure.multiEval.listPy.segment.tdd.get(segment = repcap.Segment.Default) \n
		Defines segment settings only relevant for uplink measurements with the duplex mode TDD.
		For general segment configuration, see method RsCMPX_LteMeas.Configure.MultiEval.ListPy.Segment.Setup.set. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for TddStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:TDD?', self.__class__.TddStruct())
