from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierAggregation:
	"""CarrierAggregation commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrierAggregation", core, parent)

	@property
	def channelBw1st(self):
		"""channelBw1st commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_channelBw1st'):
			from .CarrierAggregation_.ChannelBw1st import ChannelBw1st
			self._channelBw1st = ChannelBw1st(self._core, self._base)
		return self._channelBw1st

	def get_ocombination(self) -> float or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:OCOMbination \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.seMask.obwLimit.carrierAggregation.get_ocombination() \n
		Defines an upper limit for the occupied bandwidth. The setting applies to all 'other' channel bandwidth combinations, not
		covered by other commands in this chapter. \n
			:return: obw_limit: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:OCOMbination?')
		return Conversions.str_to_float_or_bool(response)

	def set_ocombination(self, obw_limit: float or bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:OCOMbination \n
		Snippet: driver.configure.multiEval.limit.seMask.obwLimit.carrierAggregation.set_ocombination(obw_limit = 1.0) \n
		Defines an upper limit for the occupied bandwidth. The setting applies to all 'other' channel bandwidth combinations, not
		covered by other commands in this chapter. \n
			:param obw_limit: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(obw_limit)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:OCOMbination {param}')

	def clone(self) -> 'CarrierAggregation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierAggregation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
