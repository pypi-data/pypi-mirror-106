from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
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
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the channel bandwidth
			- Frequency_End: float: Stop frequency of the area, relative to the edges of the channel bandwidth
			- Level: float: Upper limit for the area
			- Rbw: enums.Rbw: Resolution bandwidth to be used for the area K030: 30 kHz K100: 100 kHz M1: 1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.Rbw)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.Rbw = None

	def set(self, structure: ChannelBwStruct, limit=repcap.Limit.Default, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CBANdwidth<Band> \n
		Snippet: driver.configure.multiEval.limit.seMask.limit.channelBw.set(value = [PROPERTY_STRUCT_NAME](), limit = repcap.Limit.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The emission mask applies to the channel bandwidth <Band>. \n
			:param structure: for set value, see the help for ChannelBwStruct structure arguments.
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')"""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CBANdwidth{channelBw_cmd_val}', structure)

	def get(self, limit=repcap.Limit.Default, channelBw=repcap.ChannelBw.Default) -> ChannelBwStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CBANdwidth<Band> \n
		Snippet: value: ChannelBwStruct = driver.configure.multiEval.limit.seMask.limit.channelBw.get(limit = repcap.Limit.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The emission mask applies to the channel bandwidth <Band>. \n
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')
			:return: structure: for return value, see the help for ChannelBwStruct structure arguments."""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CBANdwidth{channelBw_cmd_val}?', self.__class__.ChannelBwStruct())

	def clone(self) -> 'ChannelBw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
