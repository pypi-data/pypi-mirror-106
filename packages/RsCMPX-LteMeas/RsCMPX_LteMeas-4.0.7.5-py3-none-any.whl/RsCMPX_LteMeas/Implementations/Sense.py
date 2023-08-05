from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def carrierAggregation(self):
		"""carrierAggregation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrierAggregation'):
			from .Sense_.CarrierAggregation import CarrierAggregation
			self._carrierAggregation = CarrierAggregation(self._core, self._base)
		return self._carrierAggregation

	@property
	def multiEval(self):
		"""multiEval commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_multiEval'):
			from .Sense_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
