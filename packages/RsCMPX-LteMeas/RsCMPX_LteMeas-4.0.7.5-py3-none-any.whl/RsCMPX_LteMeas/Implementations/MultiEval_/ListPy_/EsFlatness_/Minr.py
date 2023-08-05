from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minr:
	"""Minr commands group definition. 7 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: MinRange, default value after init: MinRange.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minr", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_minRange_get', 'repcap_minRange_set', repcap.MinRange.Nr1)

	def repcap_minRange_set(self, enum_value: repcap.MinRange) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MinRange.Default
		Default value after init: MinRange.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_minRange_get(self) -> repcap.MinRange:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Minr_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Minr_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extreme'):
			from .Minr_.Extreme import Extreme
			self._extreme = Extreme(self._core, self._base)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .Minr_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Minr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Minr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
