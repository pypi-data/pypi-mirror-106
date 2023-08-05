from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.prach.limit.get_ev_magnitude() \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:EVMagnitude \n
		Snippet: driver.configure.prach.limit.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.prach.limit.get_merror() \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:MERRor \n
		Snippet: driver.configure.prach.limit.set_merror(value = MerrorStruct()) \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.prach.limit.get_perror() \n
		Defines symmetric limits for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified values. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PERRor \n
		Snippet: driver.configure.prach.limit.set_perror(value = PerrorStruct()) \n
		Defines symmetric limits for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified values. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PERRor', value)

	def get_freq_error(self) -> float or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:FERRor \n
		Snippet: value: float or bool = driver.configure.prach.limit.get_freq_error() \n
		Defines an upper limit for the carrier frequency error. \n
			:return: frequency_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:FERRor?')
		return Conversions.str_to_float_or_bool(response)

	def set_freq_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:FERRor \n
		Snippet: driver.configure.prach.limit.set_freq_error(frequency_error = 1.0) \n
		Defines an upper limit for the carrier frequency error. \n
			:param frequency_error: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:FERRor {param}')

	# noinspection PyTypeChecker
	class PdynamicsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- On_Power_Upper: float: Upper limit for the ON power
			- On_Power_Lower: float: Lower limit for the ON power
			- Off_Power_Upper: float: Upper limit for the OFF power"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('On_Power_Upper'),
			ArgStruct.scalar_float('On_Power_Lower'),
			ArgStruct.scalar_float('Off_Power_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.On_Power_Upper: float = None
			self.On_Power_Lower: float = None
			self.Off_Power_Upper: float = None

	def get_pdynamics(self) -> PdynamicsStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: value: PdynamicsStruct = driver.configure.prach.limit.get_pdynamics() \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. \n
			:return: structure: for return value, see the help for PdynamicsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PDYNamics?', self.__class__.PdynamicsStruct())

	def set_pdynamics(self, value: PdynamicsStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: driver.configure.prach.limit.set_pdynamics(value = PdynamicsStruct()) \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. \n
			:param value: see the help for PdynamicsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:PRACh:LIMit:PDYNamics', value)
