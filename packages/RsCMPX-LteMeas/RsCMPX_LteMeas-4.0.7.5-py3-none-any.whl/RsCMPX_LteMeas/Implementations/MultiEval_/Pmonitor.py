from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmonitor:
	"""Pmonitor commands group definition. 65 total commands, 9 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pmonitor", core, parent)

	@property
	def cc(self):
		"""cc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Pmonitor_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def scc(self):
		"""scc commands group. 5 Sub-classes, 0 commands."""
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
	def pcc(self):
		"""pcc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcc'):
			from .Pmonitor_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Pmonitor_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Pmonitor_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_maximum'):
			from .Pmonitor_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_minimum'):
			from .Pmonitor_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_standardDev'):
			from .Pmonitor_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Pmonitor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pmonitor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
