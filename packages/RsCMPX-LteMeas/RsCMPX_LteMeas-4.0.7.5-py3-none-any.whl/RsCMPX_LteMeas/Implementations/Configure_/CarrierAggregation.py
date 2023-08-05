from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierAggregation:
	"""CarrierAggregation commands group definition. 12 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrierAggregation", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mode'):
			from .CarrierAggregation_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	@property
	def mcarrier(self):
		"""mcarrier commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mcarrier'):
			from .CarrierAggregation_.Mcarrier import Mcarrier
			self._mcarrier = Mcarrier(self._core, self._base)
		return self._mcarrier

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .CarrierAggregation_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def channelBw(self):
		"""channelBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw'):
			from .CarrierAggregation_.ChannelBw import ChannelBw
			self._channelBw = ChannelBw(self._core, self._base)
		return self._channelBw

	@property
	def scc(self):
		"""scc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .CarrierAggregation_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def maping(self):
		"""maping commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_maping'):
			from .CarrierAggregation_.Maping import Maping
			self._maping = Maping(self._core, self._base)
		return self._maping

	def clone(self) -> 'CarrierAggregation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierAggregation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
