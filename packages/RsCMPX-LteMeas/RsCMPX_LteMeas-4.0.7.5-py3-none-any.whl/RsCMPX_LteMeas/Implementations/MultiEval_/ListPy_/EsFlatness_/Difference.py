from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Difference:
	"""Difference commands group definition. 7 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: Difference, default value after init: Difference.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("difference", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_difference_get', 'repcap_difference_set', repcap.Difference.Nr1)

	def repcap_difference_set(self, enum_value: repcap.Difference) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Difference.Default
		Default value after init: Difference.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_difference_get(self) -> repcap.Difference:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Difference_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Difference_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extreme'):
			from .Difference_.Extreme import Extreme
			self._extreme = Extreme(self._core, self._base)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .Difference_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Difference':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Difference(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
