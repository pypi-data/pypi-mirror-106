from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("network", core, parent)

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:NETWork:BAND \n
		Snippet: value: enums.Band = driver.configure.network.get_band() \n
		No command help available \n
			:return: band: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:NETWork:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:NETWork:BAND \n
		Snippet: driver.configure.network.set_band(band = enums.Band.OB1) \n
		No command help available \n
			:param band: No help available
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:NETWork:BAND {param}')

	# noinspection PyTypeChecker
	def get_dmode(self) -> enums.Mode:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:NETWork:DMODe \n
		Snippet: value: enums.Mode = driver.configure.network.get_dmode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:MEASurement<Instance>:NETWork:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.Mode)

	def set_dmode(self, mode: enums.Mode) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:NETWork:DMODe \n
		Snippet: driver.configure.network.set_dmode(mode = enums.Mode.FDD) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Mode)
		self._core.io.write_with_opc(f'CONFigure:LTE:MEASurement<Instance>:NETWork:DMODe {param}')
