from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iemissions:
	"""Iemissions commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iemissions", core, parent)

	@property
	def ulca(self):
		"""ulca commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulca'):
			from .Iemissions_.Ulca import Ulca
			self._ulca = Ulca(self._core, self._base)
		return self._ulca

	def get_scc(self) -> List[float]:
		"""SCPI: SENSe:LTE:MEASurement<Instance>:MEValuation:LIMit:IEMissions:SCC \n
		Snippet: value: List[float] = driver.sense.multiEval.limit.iemissions.get_scc() \n
		No command help available \n
			:return: power: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SENSe:LTE:MEASurement<Instance>:MEValuation:LIMit:IEMissions:SCC?')
		return response

	def get_pcc(self) -> List[float]:
		"""SCPI: SENSe:LTE:MEASurement<Instance>:MEValuation:LIMit:IEMissions[:PCC] \n
		Snippet: value: List[float] = driver.sense.multiEval.limit.iemissions.get_pcc() \n
		No command help available \n
			:return: power: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SENSe:LTE:MEASurement<Instance>:MEValuation:LIMit:IEMissions:PCC?')
		return response

	def clone(self) -> 'Iemissions':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iemissions(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
