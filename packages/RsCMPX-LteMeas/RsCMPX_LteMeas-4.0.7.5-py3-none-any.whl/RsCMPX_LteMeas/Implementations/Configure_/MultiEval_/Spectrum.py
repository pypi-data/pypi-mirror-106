from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	@property
	def seMask(self):
		"""seMask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seMask'):
			from .Spectrum_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Spectrum_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	def clone(self) -> 'Spectrum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
