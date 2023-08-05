from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emtc:
	"""Emtc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emtc", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:EMTC:ENABle \n
		Snippet: value: bool = driver.configure.emtc.get_enable() \n
		Enables or disables eMTC. For the combined signal path scenario, useCONFigure:LTE:EMTC:ENABle. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:EMTC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:EMTC:ENABle \n
		Snippet: driver.configure.emtc.set_enable(enable = False) \n
		Enables or disables eMTC. For the combined signal path scenario, useCONFigure:LTE:EMTC:ENABle. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:EMTC:ENABle {param}')

	def get_nband(self) -> int:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:EMTC:NBANd \n
		Snippet: value: int = driver.configure.emtc.get_nband() \n
		Selects the narrowband used for eMTC. \n
			:return: number: The maximum depends on the channel BW, see 'eMTC narrowbands'. Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:EMTC:NBANd?')
		return Conversions.str_to_int(response)

	def set_nband(self, number: int) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:EMTC:NBANd \n
		Snippet: driver.configure.emtc.set_nband(number = 1) \n
		Selects the narrowband used for eMTC. \n
			:param number: The maximum depends on the channel BW, see 'eMTC narrowbands'. Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:EMTC:NBANd {param}')
