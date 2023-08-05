from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DchType:
	"""DchType commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dchType", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Channel_Type: enums.UplinkChannelType: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Channel_Type', enums.UplinkChannelType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Channel_Type: enums.UplinkChannelType = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:DCHType \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.dchType.fetch(segment = repcap.Segment.Default) \n
		Return the uplink channel type for segment <no> in list mode. The result is determined from the last measured slot of the
		statistical length. The individual measurements provide identical detected channel type results when measuring the same
		slot. However different statistical lengths can be defined for the measurements so that the measured slots and returned
		results can differ. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:DCHType?', self.__class__.FetchStruct())
