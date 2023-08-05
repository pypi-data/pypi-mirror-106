from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: Number of subframes in the segment
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet.
			- Duplex_Mode: enums.Mode: Duplex mode used in the segment
			- Band: enums.Band: TDD UL: OB33 | ... | OB45 | OB48 | OB50 | ... | OB53 | OB250 Sidelink: OB47 Operating band used in the segment
			- Frequency: float: Center frequency of CC1 used in the segment For the supported range, see 'Frequency Ranges'.
			- Ch_Bandwidth: enums.ChannelBandwidth: Channel bandwidth of CC1 used in the segment B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
			- Cyclic_Prefix: enums.CyclicPrefix: Type of cyclic prefix used in the segment
			- Channel_Type: enums.SegmentChannelTypeExtended: Channel type to be measured in the segment (AUTO for automatic detection) Uplink: AUTO, PUSCh, PUCCh Sidelink: PSSCh, PSCCh
			- Retrigger_Flag: enums.RetriggerFlag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. For subsequent segments, the retrigger flag is ignored for trigger mode ONCE and evaluated for trigger mode SEGMent, see [CMDLINK: TRIGger:LTE:MEASi:MEValuation:LIST:MODE CMDLINK]. OFF: measure the segment without retrigger ON: wait for a trigger event from the trigger source configured via [CMDLINK: TRIGger:LTE:MEASi:MEValuation:SOURce CMDLINK] IFPower: wait for a trigger event from the trigger source IF Power
			- Evaluat_Offset: int: Number of subframes at the beginning of the segment that are not evaluated
			- Network_Sig_Value: enums.NetworkSigValueNoCarrAggr: Optional setting parameter. Network signaled value to be used for the segment"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.Mode),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Ch_Bandwidth', enums.ChannelBandwidth),
			ArgStruct.scalar_enum('Cyclic_Prefix', enums.CyclicPrefix),
			ArgStruct.scalar_enum('Channel_Type', enums.SegmentChannelTypeExtended),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset'),
			ArgStruct.scalar_enum('Network_Sig_Value', enums.NetworkSigValueNoCarrAggr)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Duplex_Mode: enums.Mode = None
			self.Band: enums.Band = None
			self.Frequency: float = None
			self.Ch_Bandwidth: enums.ChannelBandwidth = None
			self.Cyclic_Prefix: enums.CyclicPrefix = None
			self.Channel_Type: enums.SegmentChannelTypeExtended = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None
			self.Network_Sig_Value: enums.NetworkSigValueNoCarrAggr = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.multiEval.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCMPX_LteMeas.Configure.MultiEval.ListPy.lrange) . For uplink signals with TDD mode, see also method
		RsCMPX_LteMeas.Configure.MultiEval.ListPy.Segment.Tdd.set. For carrier-specific settings for carrier aggregation, see
		CONFigure:LTE:MEAS<i>:MEValuation:LIST:SEGMent<no>:CC<c>. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCMPX_LteMeas.Configure.MultiEval.ListPy.lrange) . For uplink signals with TDD mode, see also method
		RsCMPX_LteMeas.Configure.MultiEval.ListPy.Segment.Tdd.set. For carrier-specific settings for carrier aggregation, see
		CONFigure:LTE:MEAS<i>:MEValuation:LIST:SEGMent<no>:CC<c>. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
