from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


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
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- On_Power_Upper: float: Upper limit for the 'ON power'
			- On_Power_Lower: float: Lower limit for the 'ON power'
			- Off_Power_Upper: float: Upper limit for the 'OFF power' and the 'SRS OFF' power"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('On_Power_Upper'),
			ArgStruct.scalar_float('On_Power_Lower'),
			ArgStruct.scalar_float('Off_Power_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.On_Power_Upper: float = None
			self.On_Power_Lower: float = None
			self.Off_Power_Upper: float = None

	def set(self, structure: ChannelBwStruct, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:CBANdwidth<Band> \n
		Snippet: driver.configure.multiEval.limit.pdynamics.channelBw.set(value = [PROPERTY_STRUCT_NAME](), channelBw = repcap.ChannelBw.Default) \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. Separate limits can be
		defined for each channel bandwidth. \n
			:param structure: for set value, see the help for ChannelBwStruct structure arguments.
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')"""
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:CBANdwidth{channelBw_cmd_val}', structure)

	def get(self, channelBw=repcap.ChannelBw.Default) -> ChannelBwStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:CBANdwidth<Band> \n
		Snippet: value: ChannelBwStruct = driver.configure.multiEval.limit.pdynamics.channelBw.get(channelBw = repcap.ChannelBw.Default) \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. Separate limits can be
		defined for each channel bandwidth. \n
			:param channelBw: optional repeated capability selector. Default value: Bw14 (settable in the interface 'ChannelBw')
			:return: structure: for return value, see the help for ChannelBwStruct structure arguments."""
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:CBANdwidth{channelBw_cmd_val}?', self.__class__.ChannelBwStruct())

	def clone(self) -> 'ChannelBw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
