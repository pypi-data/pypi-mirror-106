from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 60 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def rbaTable(self):
		"""rbaTable commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbaTable'):
			from .Trace_.RbaTable import RbaTable
			self._rbaTable = RbaTable(self._core, self._base)
		return self._rbaTable

	@property
	def iq(self):
		"""iq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Trace_.Iq import Iq
			self._iq = Iq(self._core, self._base)
		return self._iq

	@property
	def iemissions(self):
		"""iemissions commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iemissions'):
			from .Trace_.Iemissions import Iemissions
			self._iemissions = Iemissions(self._core, self._base)
		return self._iemissions

	@property
	def evmc(self):
		"""evmc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_evmc'):
			from .Trace_.Evmc import Evmc
			self._evmc = Evmc(self._core, self._base)
		return self._evmc

	@property
	def evmSymbol(self):
		"""evmSymbol commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmSymbol'):
			from .Trace_.EvmSymbol import EvmSymbol
			self._evmSymbol = EvmSymbol(self._core, self._base)
		return self._evmSymbol

	@property
	def esFlatness(self):
		"""esFlatness commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_esFlatness'):
			from .Trace_.EsFlatness import EsFlatness
			self._esFlatness = EsFlatness(self._core, self._base)
		return self._esFlatness

	@property
	def seMask(self):
		"""seMask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .Trace_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Trace_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pmonitor(self):
		"""pmonitor commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmonitor'):
			from .Trace_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	@property
	def pdynamics(self):
		"""pdynamics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Trace_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
