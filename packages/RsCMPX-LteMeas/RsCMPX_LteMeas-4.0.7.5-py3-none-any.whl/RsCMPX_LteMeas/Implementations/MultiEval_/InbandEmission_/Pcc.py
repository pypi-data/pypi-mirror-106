from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcc:
	"""Pcc commands group definition. 6 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcc", core, parent)

	@property
	def margin(self):
		"""margin commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .Pcc_.Margin import Margin
			self._margin = Margin(self._core, self._base)
		return self._margin

	def clone(self) -> 'Pcc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
