from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 30 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	@property
	def ripple(self):
		"""ripple commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ripple'):
			from .EsFlatness_.Ripple import Ripple
			self._ripple = Ripple(self._core, self._base)
		return self._ripple

	@property
	def difference(self):
		"""difference commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_difference'):
			from .EsFlatness_.Difference import Difference
			self._difference = Difference(self._core, self._base)
		return self._difference

	@property
	def minr(self):
		"""minr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_minr'):
			from .EsFlatness_.Minr import Minr
			self._minr = Minr(self._core, self._base)
		return self._minr

	@property
	def maxr(self):
		"""maxr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_maxr'):
			from .EsFlatness_.Maxr import Maxr
			self._maxr = Maxr(self._core, self._base)
		return self._maxr

	@property
	def scIndex(self):
		"""scIndex commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scIndex'):
			from .EsFlatness_.ScIndex import ScIndex
			self._scIndex = ScIndex(self._core, self._base)
		return self._scIndex

	def clone(self) -> 'EsFlatness':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EsFlatness(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
