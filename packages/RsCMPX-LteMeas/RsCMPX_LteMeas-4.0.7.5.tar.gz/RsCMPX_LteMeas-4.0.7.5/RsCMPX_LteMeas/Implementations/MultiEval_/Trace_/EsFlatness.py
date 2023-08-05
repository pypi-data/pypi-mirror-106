from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_phase'):
			from .EsFlatness_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	def read(self) -> List[float]:
		"""SCPI: READ:LTE:MEASurement<Instance>:MEValuation:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.multiEval.trace.esFlatness.read() \n
		Returns the values of the equalizer spectrum flatness trace. See also 'Square Equalizer Spectrum Flatness'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:LTE:MEASurement<Instance>:MEValuation:TRACe:ESFLatness?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.multiEval.trace.esFlatness.fetch() \n
		Returns the values of the equalizer spectrum flatness trace. See also 'Square Equalizer Spectrum Flatness'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:LTE:MEASurement<Instance>:MEValuation:TRACe:ESFLatness?', suppressed)
		return response

	def clone(self) -> 'EsFlatness':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EsFlatness(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
