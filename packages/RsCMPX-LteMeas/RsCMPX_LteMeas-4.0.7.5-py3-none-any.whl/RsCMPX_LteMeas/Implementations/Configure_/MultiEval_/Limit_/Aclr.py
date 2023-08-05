from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	@property
	def utra(self):
		"""utra commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_utra'):
			from .Aclr_.Utra import Utra
			self._utra = Utra(self._core, self._base)
		return self._utra

	@property
	def eutra(self):
		"""eutra commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eutra'):
			from .Aclr_.Eutra import Eutra
			self._eutra = Eutra(self._core, self._base)
		return self._eutra

	def clone(self) -> 'Aclr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aclr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
