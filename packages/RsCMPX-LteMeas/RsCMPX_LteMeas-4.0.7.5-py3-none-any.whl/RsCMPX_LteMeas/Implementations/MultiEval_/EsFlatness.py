from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 13 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	@property
	def current(self):
		"""current commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .EsFlatness_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .EsFlatness_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_extreme'):
			from .EsFlatness_.Extreme import Extreme
			self._extreme = Extreme(self._core, self._base)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_standardDev'):
			from .EsFlatness_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'EsFlatness':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EsFlatness(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
