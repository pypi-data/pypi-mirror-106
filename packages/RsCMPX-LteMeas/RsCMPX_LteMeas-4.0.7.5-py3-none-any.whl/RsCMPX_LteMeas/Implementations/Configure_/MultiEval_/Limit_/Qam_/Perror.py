from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perror:
	"""Perror commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("perror", core, parent)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def set(self, structure: PerrorStruct, qAMmodOrder=repcap.QAMmodOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PERRor \n
		Snippet: driver.configure.multiEval.limit.qam.perror.set(value = [PROPERTY_STRUCT_NAME](), qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines symmetric limits for the RMS and peak values of the phase error, for QAM modulations. The limit check fails if
		the absolute value of the measured phase error exceeds the specified values. \n
			:param structure: for set value, see the help for PerrorStruct structure arguments.
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')"""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:PERRor', structure)

	def get(self, qAMmodOrder=repcap.QAMmodOrder.Default) -> PerrorStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.multiEval.limit.qam.perror.get(qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines symmetric limits for the RMS and peak values of the phase error, for QAM modulations. The limit check fails if
		the absolute value of the measured phase error exceeds the specified values. \n
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for PerrorStruct structure arguments."""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:PERRor?', self.__class__.PerrorStruct())
