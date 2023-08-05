from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelBw3rd:
	"""ChannelBw3rd commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: ThirdChannelBw, default value after init: ThirdChannelBw.Bw100"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channelBw3rd", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_thirdChannelBw_get', 'repcap_thirdChannelBw_set', repcap.ThirdChannelBw.Bw100)

	def repcap_thirdChannelBw_set(self, enum_value: repcap.ThirdChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ThirdChannelBw.Default
		Default value after init: ThirdChannelBw.Bw100"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_thirdChannelBw_get(self) -> repcap.ThirdChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ChannelBw3rdStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Relative_Level: float or bool: No parameter help available
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def set(self, structure: ChannelBw3rdStruct, utraAdjChannel=repcap.UtraAdjChannel.Default, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default, thirdChannelBw=repcap.ThirdChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2>:CBANdwidth<Band3> \n
		Snippet: driver.configure.multiEval.limit.aclr.utra.carrierAggregation.channelBw1st.channelBw2nd.channelBw3rd.set(value = [PROPERTY_STRUCT_NAME](), utraAdjChannel = repcap.UtraAdjChannel.Default, firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default, thirdChannelBw = repcap.ThirdChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings are defined separately for each channel bandwidth combination, for three aggregated carriers.
		The following bandwidth combinations are supported: Example: For the first line in the figure, use ...
		:CBANdwidth200:CBANdwidth150:CBANdwidth100. \n
			:param structure: for set value, see the help for ChannelBw3rdStruct structure arguments.
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')
			:param firstChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:param thirdChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw3rd')"""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		thirdChannelBw_cmd_val = self._base.get_repcap_cmd_value(thirdChannelBw, repcap.ThirdChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}:CBANdwidth{thirdChannelBw_cmd_val}', structure)

	def get(self, utraAdjChannel=repcap.UtraAdjChannel.Default, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default, thirdChannelBw=repcap.ThirdChannelBw.Default) -> ChannelBw3rdStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2>:CBANdwidth<Band3> \n
		Snippet: value: ChannelBw3rdStruct = driver.configure.multiEval.limit.aclr.utra.carrierAggregation.channelBw1st.channelBw2nd.channelBw3rd.get(utraAdjChannel = repcap.UtraAdjChannel.Default, firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default, thirdChannelBw = repcap.ThirdChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings are defined separately for each channel bandwidth combination, for three aggregated carriers.
		The following bandwidth combinations are supported: Example: For the first line in the figure, use ...
		:CBANdwidth200:CBANdwidth150:CBANdwidth100. \n
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')
			:param firstChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:param thirdChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw3rd')
			:return: structure: for return value, see the help for ChannelBw3rdStruct structure arguments."""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		thirdChannelBw_cmd_val = self._base.get_repcap_cmd_value(thirdChannelBw, repcap.ThirdChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}:CBANdwidth{thirdChannelBw_cmd_val}?', self.__class__.ChannelBw3rdStruct())

	def clone(self) -> 'ChannelBw3rd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw3rd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
