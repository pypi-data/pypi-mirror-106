from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffset:
	"""IqOffset commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqOffset", core, parent)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Offset_1: float: Offset for high TX power range
			- Offset_2: float: Offset for intermediate TX power range
			- Offset_3: float: Offset for low TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def set(self, structure: IqOffsetStruct, qAMmodOrder=repcap.QAMmodOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IBE:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.qam.ibe.iqOffset.set(value = [PROPERTY_STRUCT_NAME](), qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission, for QAM modulations.
		Three different values can be set for three TX power ranges, see 'Inband Emissions Limits'. \n
			:param structure: for set value, see the help for IqOffsetStruct structure arguments.
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')"""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IBE:IQOFfset', structure)

	def get(self, qAMmodOrder=repcap.QAMmodOrder.Default) -> IqOffsetStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IBE:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.multiEval.limit.qam.ibe.iqOffset.get(qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission, for QAM modulations.
		Three different values can be set for three TX power ranges, see 'Inband Emissions Limits'. \n
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IBE:IQOFfset?', self.__class__.IqOffsetStruct())
