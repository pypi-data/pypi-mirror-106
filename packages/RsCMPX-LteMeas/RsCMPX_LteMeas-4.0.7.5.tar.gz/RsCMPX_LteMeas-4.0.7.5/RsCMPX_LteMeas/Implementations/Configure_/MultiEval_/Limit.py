from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 40 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def qpsk(self):
		"""qpsk commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_qpsk'):
			from .Limit_.Qpsk import Qpsk
			self._qpsk = Qpsk(self._core, self._base)
		return self._qpsk

	@property
	def qam(self):
		"""qam commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Limit_.Qam import Qam
			self._qam = Qam(self._core, self._base)
		return self._qam

	@property
	def seMask(self):
		"""seMask commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .Limit_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Limit_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pdynamics(self):
		"""pdynamics commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Limit_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
