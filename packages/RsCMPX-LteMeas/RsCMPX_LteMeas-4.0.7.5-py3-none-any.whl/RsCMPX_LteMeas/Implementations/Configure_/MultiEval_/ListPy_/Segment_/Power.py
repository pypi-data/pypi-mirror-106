from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	class PowerStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Power_Statistics: int: Statistical length in subframes
			- Power_Enable: bool: Enables or disables the measurement of the total TX power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Power_Statistics'),
			ArgStruct.scalar_bool('Power_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Power_Statistics: int = None
			self.Power_Enable: bool = None

	def set(self, structure: PowerStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:POWer \n
		Snippet: driver.configure.multiEval.listPy.segment.power.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines settings for the measurement of the total TX power of all carriers for segment <no>. \n
			:param structure: for set value, see the help for PowerStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:POWer', structure)

	def get(self, segment=repcap.Segment.Default) -> PowerStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:POWer \n
		Snippet: value: PowerStruct = driver.configure.multiEval.listPy.segment.power.get(segment = repcap.Segment.Default) \n
		Defines settings for the measurement of the total TX power of all carriers for segment <no>. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for PowerStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:POWer?', self.__class__.PowerStruct())
