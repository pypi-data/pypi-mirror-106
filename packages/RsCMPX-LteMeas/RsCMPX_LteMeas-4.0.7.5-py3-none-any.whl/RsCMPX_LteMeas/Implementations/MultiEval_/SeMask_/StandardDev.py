from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for spectrum emission measurements exceeding the specified spectrum emission mask limits.
			- Obw: float: Occupied bandwidth
			- Tx_Power: float: Total TX power in the slot over all component carriers"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Tx_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Obw: float = None
			self.Tx_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.seMask.standardDev.read() \n
		Return the current, average and standard deviation single value results of the spectrum emission measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.seMask.standardDev.fetch() \n
		Return the current, average and standard deviation single value results of the spectrum emission measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Obw: float: No parameter help available
			- Tx_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Tx_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Obw: float = None
			self.Tx_Power: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation \n
		Snippet: value: CalculateStruct = driver.multiEval.seMask.standardDev.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:LTE:MEASurement<Instance>:MEValuation:SEMask:SDEViation?', self.__class__.CalculateStruct())
