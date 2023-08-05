from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocombination:
	"""Ocombination commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ocombination", core, parent)

	# noinspection PyTypeChecker
	class OcombinationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Relative_Level: float or bool: No parameter help available
			- Absolute_Level: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def set(self, structure: OcombinationStruct, utraAdjChannel=repcap.UtraAdjChannel.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CAGGregation:OCOMbination \n
		Snippet: driver.configure.multiEval.limit.aclr.utra.carrierAggregation.ocombination.set(value = [PROPERTY_STRUCT_NAME](), utraAdjChannel = repcap.UtraAdjChannel.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings apply to all 'other' channel bandwidth combinations, not covered by other commands in this chapter. \n
			:param structure: for set value, see the help for OcombinationStruct structure arguments.
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')"""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CAGGregation:OCOMbination', structure)

	def get(self, utraAdjChannel=repcap.UtraAdjChannel.Default) -> OcombinationStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA<nr>:CAGGregation:OCOMbination \n
		Snippet: value: OcombinationStruct = driver.configure.multiEval.limit.aclr.utra.carrierAggregation.ocombination.get(utraAdjChannel = repcap.UtraAdjChannel.Default) \n
		Defines relative and absolute limits for the ACLR measured in the first or second adjacent UTRA channel, depending on
		<no>. The settings apply to all 'other' channel bandwidth combinations, not covered by other commands in this chapter. \n
			:param utraAdjChannel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Utra')
			:return: structure: for return value, see the help for OcombinationStruct structure arguments."""
		utraAdjChannel_cmd_val = self._base.get_repcap_cmd_value(utraAdjChannel, repcap.UtraAdjChannel)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:UTRA{utraAdjChannel_cmd_val}:CAGGregation:OCOMbination?', self.__class__.OcombinationStruct())
