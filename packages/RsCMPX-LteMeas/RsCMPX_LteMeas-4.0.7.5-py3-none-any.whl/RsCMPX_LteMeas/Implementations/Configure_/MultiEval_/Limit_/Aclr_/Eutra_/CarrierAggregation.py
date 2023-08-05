from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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

	# noinspection PyTypeChecker
	class OcombinationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Relative_Level: float or bool: No parameter help available
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def get_ocombination(self) -> OcombinationStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:OCOMbination \n
		Snippet: value: OcombinationStruct = driver.configure.multiEval.limit.aclr.eutra.carrierAggregation.get_ocombination() \n
		Defines relative and absolute limits for the ACLR measured in an adjacent E-UTRA channel. The settings apply to all
		'other' channel bandwidth combinations, not covered by other commands in this chapter. \n
			:return: structure: for return value, see the help for OcombinationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:OCOMbination?', self.__class__.OcombinationStruct())

	def set_ocombination(self, value: OcombinationStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:OCOMbination \n
		Snippet: driver.configure.multiEval.limit.aclr.eutra.carrierAggregation.set_ocombination(value = OcombinationStruct()) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent E-UTRA channel. The settings apply to all
		'other' channel bandwidth combinations, not covered by other commands in this chapter. \n
			:param value: see the help for OcombinationStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:OCOMbination', value)

	def clone(self) -> 'CarrierAggregation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CarrierAggregation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
