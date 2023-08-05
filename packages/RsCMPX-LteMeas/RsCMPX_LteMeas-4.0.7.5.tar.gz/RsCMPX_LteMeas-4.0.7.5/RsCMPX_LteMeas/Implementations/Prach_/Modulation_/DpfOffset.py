from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpfOffset:
	"""DpfOffset commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpfOffset", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .DpfOffset_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	def fetch(self) -> int:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:PRACh:MODulation:DPFoffset \n
		Snippet: value: int = driver.prach.modulation.dpfOffset.fetch() \n
		Returns the automatically detected or manually configured PRACH frequency offset for single-preamble measurements. \n
		Suppressed linked return values: reliability \n
			:return: prach_freq_offset: PRACH frequency offset"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:LTE:MEASurement<Instance>:PRACh:MODulation:DPFoffset?', suppressed)
		return Conversions.str_to_int(response)

	def clone(self) -> 'DpfOffset':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DpfOffset(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
