from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelBw:
	"""ChannelBw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: ChannelBw, default value after init: ChannelBw.Bw14"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channelBw", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_channelBw_get', 'repcap_channelBw_set', repcap.ChannelBw.Bw14)

	def repcap_channelBw_set(self, enum_value: repcap.ChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelBw.Default
		Default value after init: ChannelBw.Bw14"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_channelBw_get(self) -> repcap.ChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ChannelBwStruct(StructBase):
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

	def set(self, structure: ChannelBwStruct, utraAdjChannel=repcap.UtraAdjChannel.Default, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CBANdwidth<Band> \n
		Snippet: driver.configure.multiEval.limit.aclr.utra.channelBw.set(value = [PROPERTY_STRUCT_NAME](), utraAdjChannel = repcap.UtraAdjChannel.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings are defined separately for each channel bandwidth. \n
			:param structure: for set value, see the help for ChannelBwStruct structure arguments.
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')"""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CBANdwidth{channelBw_cmd_val}', structure)

	def get(self, utraAdjChannel=repcap.UtraAdjChannel.Default, channelBw=repcap.ChannelBw.Default) -> ChannelBwStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CBANdwidth<Band> \n
		Snippet: value: ChannelBwStruct = driver.configure.multiEval.limit.aclr.utra.channelBw.get(utraAdjChannel = repcap.UtraAdjChannel.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings are defined separately for each channel bandwidth. \n
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')
			:return: structure: for return value, see the help for ChannelBwStruct structure arguments."""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CBANdwidth{channelBw_cmd_val}?', self.__class__.ChannelBwStruct())

	def clone(self) -> 'ChannelBw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
