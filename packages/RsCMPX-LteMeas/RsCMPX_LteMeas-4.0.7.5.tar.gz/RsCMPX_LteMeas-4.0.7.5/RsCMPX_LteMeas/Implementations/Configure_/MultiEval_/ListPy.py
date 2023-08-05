from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 23 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def segment(self):
		"""segment commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	# noinspection PyTypeChecker
	class LrangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: First measured segment in the range of configured segments
			- Nr_Segments: int: Number of measured segments"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Nr_Segments')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Nr_Segments: int = None

	def get_lrange(self) -> LrangeStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: value: LrangeStruct = driver.configure.multiEval.listPy.get_lrange() \n
		Select a range of measured segments. The segments must be configured using method RsCMPX_LteMeas.Configure.MultiEval.
		ListPy.Segment.Setup.set. \n
			:return: structure: for return value, see the help for LrangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge?', self.__class__.LrangeStruct())

	def set_lrange(self, value: LrangeStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: driver.configure.multiEval.listPy.set_lrange(value = LrangeStruct()) \n
		Select a range of measured segments. The segments must be configured using method RsCMPX_LteMeas.Configure.MultiEval.
		ListPy.Segment.Setup.set. \n
			:param value: see the help for LrangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge', value)

	def get_os_index(self) -> int or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: value: int or bool = driver.configure.multiEval.listPy.get_os_index() \n
		No command help available \n
			:return: offline_seg_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex?')
		return Conversions.str_to_int_or_bool(response)

	def set_os_index(self, offline_seg_index: int or bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: driver.configure.multiEval.listPy.set_os_index(offline_seg_index = 1) \n
		No command help available \n
			:param offline_seg_index: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(offline_seg_index)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex {param}')

	# noinspection PyTypeChecker
	def get_plc_mode(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:PLCMode \n
		Snippet: value: enums.ParameterSetMode = driver.configure.multiEval.listPy.get_plc_mode() \n
		Selects which physical cell ID setting is used for list mode measurements. \n
			:return: plc_id_mode:
				- GLOBal: The global setting is used for all segments, see CONFigure:LTE:MEASi:MEValuation:CCno:PLCid.
				- LIST: The cell ID is configured per segment, see CONFigure:LTE:MEASi:MEValuation:LIST:SEGMentno:PLCid."""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:PLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_plc_mode(self, plc_id_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:PLCMode \n
		Snippet: driver.configure.multiEval.listPy.set_plc_mode(plc_id_mode = enums.ParameterSetMode.GLOBal) \n
		Selects which physical cell ID setting is used for list mode measurements. \n
			:param plc_id_mode:
				- GLOBal: The global setting is used for all segments, see CONFigure:LTE:MEASi:MEValuation:CCno:PLCid.
				- LIST: The cell ID is configured per segment, see CONFigure:LTE:MEASi:MEValuation:LIST:SEGMentno:PLCid."""
		param = Conversions.enum_scalar_to_str(plc_id_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:PLCMode {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: value: bool = driver.configure.multiEval.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF: Disable list mode ON: Enable list mode
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: driver.configure.multiEval.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF: Disable list mode ON: Enable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
