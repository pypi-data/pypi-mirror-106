from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def rbIndex(self):
		"""rbIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbIndex'):
			from .Current_.RbIndex import RbIndex
			self._rbIndex = RbIndex(self._core, self._base)
		return self._rbIndex

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Margin: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Margin')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Margin: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:IEMission[:PCC]:MARGin:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.inbandEmission.pcc.margin.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:MEValuation:IEMission:PCC:MARGin:CURRent?', self.__class__.FetchStruct())

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
