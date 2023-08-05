from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for power dynamics measurements exceeding the specified power dynamics limits.
			- Off_Power_Before: float: OFF power mean value for subframe before preamble without transient period
			- On_Power_Rms: float: ON power mean value over preamble
			- On_Power_Peak: float: ON power peak value within preamble
			- Off_Power_After: float: OFF power mean value for subframe after preamble without transient period"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Off_Power_Before'),
			ArgStruct.scalar_float('On_Power_Rms'),
			ArgStruct.scalar_float('On_Power_Peak'),
			ArgStruct.scalar_float('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float = None
			self.On_Power_Rms: float = None
			self.On_Power_Peak: float = None
			self.Off_Power_After: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: ResultData = driver.prach.pdynamics.minimum.read() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: ResultData = driver.prach.pdynamics.minimum.fetch() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for power dynamics measurements exceeding the specified power dynamics limits.
			- Off_Power_Before: float: OFF power mean value for subframe before preamble without transient period
			- On_Power_Rms: float: ON power mean value over preamble
			- On_Power_Peak: float: ON power peak value within preamble
			- Off_Power_After: float: OFF power mean value for subframe after preamble without transient period"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Off_Power_Before'),
			ArgStruct.scalar_float('On_Power_Rms'),
			ArgStruct.scalar_float('On_Power_Peak'),
			ArgStruct.scalar_float('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float = None
			self.On_Power_Rms: float = None
			self.On_Power_Peak: float = None
			self.Off_Power_After: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum \n
		Snippet: value: CalculateStruct = driver.prach.pdynamics.minimum.calculate() \n
		Return the current, average, minimum, maximum and standard deviation single value results of the power dynamics
		measurement. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:LTE:MEASurement<Instance>:PRACh:PDYNamics:MINimum?', self.__class__.CalculateStruct())
