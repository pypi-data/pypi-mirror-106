from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcarrier:
	"""Mcarrier commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mcarrier", core, parent)

	@property
	def enhanced(self):
		"""enhanced commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enhanced'):
			from .Mcarrier_.Enhanced import Enhanced
			self._enhanced = Enhanced(self._core, self._base)
		return self._enhanced

	def set(self, meas_carrier: enums.MeasCarrier, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CAGGregation:MCARrier \n
		Snippet: driver.configure.multiEval.listPy.segment.carrierAggregation.mcarrier.set(meas_carrier = enums.MeasCarrier.PCC, segment = repcap.Segment.Default) \n
		No command help available \n
			:param meas_carrier: No help available
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		param = Conversions.enum_scalar_to_str(meas_carrier, enums.MeasCarrier)
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CAGGregation:MCARrier {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.MeasCarrier:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CAGGregation:MCARrier \n
		Snippet: value: enums.MeasCarrier = driver.configure.multiEval.listPy.segment.carrierAggregation.mcarrier.get(segment = repcap.Segment.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: meas_carrier: No help available"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CAGGregation:MCARrier?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCarrier)

	def clone(self) -> 'Mcarrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcarrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
