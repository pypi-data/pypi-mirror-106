from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 24 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	@property
	def obw(self):
		"""obw commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .SeMask_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	@property
	def txPower(self):
		"""txPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_txPower'):
			from .SeMask_.TxPower import TxPower
			self._txPower = TxPower(self._core, self._base)
		return self._txPower

	@property
	def margin(self):
		"""margin commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .SeMask_.Margin import Margin
			self._margin = Margin(self._core, self._base)
		return self._margin

	@property
	def dchType(self):
		"""dchType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dchType'):
			from .SeMask_.DchType import DchType
			self._dchType = DchType(self._core, self._base)
		return self._dchType

	@property
	def dallocation(self):
		"""dallocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dallocation'):
			from .SeMask_.Dallocation import Dallocation
			self._dallocation = Dallocation(self._core, self._base)
		return self._dallocation

	def clone(self) -> 'SeMask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeMask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
