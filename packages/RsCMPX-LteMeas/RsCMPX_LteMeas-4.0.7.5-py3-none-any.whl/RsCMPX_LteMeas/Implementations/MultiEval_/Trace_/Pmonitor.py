from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmonitor:
	"""Pmonitor commands group definition. 10 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pmonitor", core, parent)

	@property
	def scc(self):
		"""scc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scc'):
			from .Pmonitor_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def ulca(self):
		"""ulca commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulca'):
			from .Pmonitor_.Ulca import Ulca
			self._ulca = Ulca(self._core, self._base)
		return self._ulca

	@property
	def cc(self):
		"""cc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cc'):
			from .Pmonitor_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def pcc(self):
		"""pcc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcc'):
			from .Pmonitor_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	def clone(self) -> 'Pmonitor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pmonitor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
