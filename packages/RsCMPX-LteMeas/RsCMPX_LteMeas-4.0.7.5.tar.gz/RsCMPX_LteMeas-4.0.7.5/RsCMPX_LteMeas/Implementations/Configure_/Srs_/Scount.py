from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scount", core, parent)

	def get_pdynamics(self) -> int:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:SRS:SCOunt:PDYNamics \n
		Snippet: value: int = driver.configure.srs.scount.get_pdynamics() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:SRS:SCOunt:PDYNamics?')
		return Conversions.str_to_int(response)

	def set_pdynamics(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:SRS:SCOunt:PDYNamics \n
		Snippet: driver.configure.srs.scount.set_pdynamics(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:SRS:SCOunt:PDYNamics {param}')
