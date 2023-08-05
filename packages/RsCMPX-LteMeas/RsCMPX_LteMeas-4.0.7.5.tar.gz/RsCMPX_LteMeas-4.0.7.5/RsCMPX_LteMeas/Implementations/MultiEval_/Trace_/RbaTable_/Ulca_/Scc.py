from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands
	Repeated Capability: SecondaryCC, default value after init: SecondaryCC.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondaryCC_get', 'repcap_secondaryCC_set', repcap.SecondaryCC.CC1)

	def repcap_secondaryCC_set(self, enum_value: repcap.SecondaryCC) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCC.Default
		Default value after init: SecondaryCC.CC1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondaryCC_get(self) -> repcap.SecondaryCC:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Channel_Type: List[enums.RbTableChannelType]: No parameter help available
			- Offset_Rb: List[int]: No parameter help available
			- No_Rb: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Channel_Type', DataType.EnumList, enums.RbTableChannelType, False, True, 1),
			ArgStruct('Offset_Rb', DataType.IntegerList, None, False, True, 1),
			ArgStruct('No_Rb', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Channel_Type: List[enums.RbTableChannelType] = None
			self.Offset_Rb: List[int] = None
			self.No_Rb: List[int] = None

	def read(self, secondaryCC=repcap.SecondaryCC.Default) -> ResultData:
		"""SCPI: READ:LTE:MEASurement<Instance>:MEValuation:TRACe:RBATable:ULCA:SCC<Nr> \n
		Snippet: value: ResultData = driver.multiEval.trace.rbaTable.ulca.scc.read(secondaryCC = repcap.SecondaryCC.Default) \n
		No command help available \n
			:param secondaryCC: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		secondaryCC_cmd_val = self._base.get_repcap_cmd_value(secondaryCC, repcap.SecondaryCC)
		return self._core.io.query_struct(f'READ:LTE:MEASurement<Instance>:MEValuation:TRACe:RBATable:ULCA:SCC{secondaryCC_cmd_val}?', self.__class__.ResultData())

	def fetch(self, secondaryCC=repcap.SecondaryCC.Default) -> ResultData:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:TRACe:RBATable:ULCA:SCC<Nr> \n
		Snippet: value: ResultData = driver.multiEval.trace.rbaTable.ulca.scc.fetch(secondaryCC = repcap.SecondaryCC.Default) \n
		No command help available \n
			:param secondaryCC: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		secondaryCC_cmd_val = self._base.get_repcap_cmd_value(secondaryCC, repcap.SecondaryCC)
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:MEValuation:TRACe:RBATable:ULCA:SCC{secondaryCC_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
