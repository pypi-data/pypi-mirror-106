from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bler:
	"""Bler commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bler", core, parent)

	# noinspection PyTypeChecker
	class SframesStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sub_Frames: int: No parameter help available
			- Sched_Subfr_Per_Fr: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sub_Frames'),
			ArgStruct.scalar_int('Sched_Subfr_Per_Fr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sub_Frames: int = None
			self.Sched_Subfr_Per_Fr: int = None

	def get_sframes(self) -> SframesStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:BLER:SFRames \n
		Snippet: value: SframesStruct = driver.configure.multiEval.bler.get_sframes() \n
		No command help available \n
			:return: structure: for return value, see the help for SframesStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:BLER:SFRames?', self.__class__.SframesStruct())

	def set_sframes(self, value: SframesStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:BLER:SFRames \n
		Snippet: driver.configure.multiEval.bler.set_sframes(value = SframesStruct()) \n
		No command help available \n
			:param value: see the help for SframesStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:BLER:SFRames', value)
