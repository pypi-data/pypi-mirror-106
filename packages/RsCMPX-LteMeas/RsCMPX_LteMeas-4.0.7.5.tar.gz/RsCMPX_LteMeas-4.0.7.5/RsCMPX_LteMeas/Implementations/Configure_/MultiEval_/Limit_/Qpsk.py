from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qpsk:
	"""Qpsk commands group definition. 9 total commands, 1 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qpsk", core, parent)

	@property
	def ibe(self):
		"""ibe commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ibe'):
			from .Qpsk_.Ibe import Ibe
			self._ibe = Ibe(self._core, self._base)
		return self._ibe

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
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.multiEval.limit.qpsk.get_ev_magnitude() \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for QPSK. \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:EVMagnitude \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for QPSK. \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:EVMagnitude', value)

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
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.multiEval.limit.qpsk.get_merror() \n
		Defines upper limits for the RMS and peak values of the magnitude error for QPSK. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:MERRor \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_merror(value = MerrorStruct()) \n
		Defines upper limits for the RMS and peak values of the magnitude error for QPSK. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:MERRor', value)

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
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.multiEval.limit.qpsk.get_perror() \n
		Defines symmetric limits for the RMS and peak values of the phase error for QPSK. The limit check fails if the absolute
		value of the measured phase error exceeds the specified values. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:PERRor \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_perror(value = PerrorStruct()) \n
		Defines symmetric limits for the RMS and peak values of the phase error for QPSK. The limit check fails if the absolute
		value of the measured phase error exceeds the specified values. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:PERRor', value)

	def get_freq_error(self) -> float or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:FERRor \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.qpsk.get_freq_error() \n
		Defines an upper limit for the carrier frequency error (QPSK modulation) . \n
			:return: frequency_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:FERRor?')
		return Conversions.str_to_float_or_bool(response)

	def set_freq_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:FERRor \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_freq_error(frequency_error = 1.0) \n
		Defines an upper limit for the carrier frequency error (QPSK modulation) . \n
			:param frequency_error: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:FERRor {param}')

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Offset_1: float: I/Q origin offset limit for high TX power range
			- Offset_2: float: I/Q origin offset limit for intermediate TX power range
			- Offset_3: float: I/Q origin offset limit for low TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def get_iq_offset(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.multiEval.limit.qpsk.get_iq_offset() \n
		Defines upper limits for the I/Q origin offset (QPSK modulation) . Three different I/Q origin offset limits can be set
		for three TX power ranges. For details, see 'I/Q Origin Offset Limits'. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IQOFfset?', self.__class__.IqOffsetStruct())

	def set_iq_offset(self, value: IqOffsetStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_iq_offset(value = IqOffsetStruct()) \n
		Defines upper limits for the I/Q origin offset (QPSK modulation) . Three different I/Q origin offset limits can be set
		for three TX power ranges. For details, see 'I/Q Origin Offset Limits'. \n
			:param value: see the help for IqOffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IQOFfset', value)

	# noinspection PyTypeChecker
	class SflatnessStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Lower: float: No parameter help available
			- Upper: float: No parameter help available
			- Edge_Lower: float: No parameter help available
			- Edge_Upper: float: No parameter help available
			- Edge_Frequency: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper'),
			ArgStruct.scalar_float('Edge_Lower'),
			ArgStruct.scalar_float('Edge_Upper'),
			ArgStruct.scalar_float('Edge_Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Lower: float = None
			self.Upper: float = None
			self.Edge_Lower: float = None
			self.Edge_Upper: float = None
			self.Edge_Frequency: float = None

	def get_sflatness(self) -> SflatnessStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:SFLatness \n
		Snippet: value: SflatnessStruct = driver.configure.multiEval.limit.qpsk.get_sflatness() \n
		No command help available \n
			:return: structure: for return value, see the help for SflatnessStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:SFLatness?', self.__class__.SflatnessStruct())

	def set_sflatness(self, value: SflatnessStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:SFLatness \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_sflatness(value = SflatnessStruct()) \n
		No command help available \n
			:param value: see the help for SflatnessStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:SFLatness', value)

	# noinspection PyTypeChecker
	class EsFlatnessStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Range_1: float: Upper limit for max(range 1) - min(range 1)
			- Range_2: float: Upper limit for max(range 2) - min(range 2)
			- Max_1_Min_2: float: Upper limit for max(range 1) - min(range 2)
			- Max_2_Min_1: float: Upper limit for max(range 2) - min(range 1)
			- Edge_Frequency: float: Frequency band edge distance of border between range 1 and range 2"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Range_1'),
			ArgStruct.scalar_float('Range_2'),
			ArgStruct.scalar_float('Max_1_Min_2'),
			ArgStruct.scalar_float('Max_2_Min_1'),
			ArgStruct.scalar_float('Edge_Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Range_1: float = None
			self.Range_2: float = None
			self.Max_1_Min_2: float = None
			self.Max_2_Min_1: float = None
			self.Edge_Frequency: float = None

	def get_es_flatness(self) -> EsFlatnessStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:ESFLatness \n
		Snippet: value: EsFlatnessStruct = driver.configure.multiEval.limit.qpsk.get_es_flatness() \n
		Defines limits for the equalizer spectrum flatness (QPSK modulation) . \n
			:return: structure: for return value, see the help for EsFlatnessStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:ESFLatness?', self.__class__.EsFlatnessStruct())

	def set_es_flatness(self, value: EsFlatnessStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:ESFLatness \n
		Snippet: driver.configure.multiEval.limit.qpsk.set_es_flatness(value = EsFlatnessStruct()) \n
		Defines limits for the equalizer spectrum flatness (QPSK modulation) . \n
			:param value: see the help for EsFlatnessStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:ESFLatness', value)

	def clone(self) -> 'Qpsk':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qpsk(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
