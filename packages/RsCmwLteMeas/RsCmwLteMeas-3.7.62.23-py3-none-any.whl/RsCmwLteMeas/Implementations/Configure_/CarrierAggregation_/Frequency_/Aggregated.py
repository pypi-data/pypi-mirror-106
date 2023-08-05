from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aggregated:
	"""Aggregated commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aggregated", core, parent)

	def get_low(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:LOW \n
		Snippet: value: float = driver.configure.carrierAggregation.frequency.aggregated.get_low() \n
		Queries the lower edge of the aggregated bandwidth. \n
			:return: frequency_low: Range: 60 MHz to 6010 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:LOW?')
		return Conversions.str_to_float(response)

	def get_center(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:CENTer \n
		Snippet: value: float = driver.configure.carrierAggregation.frequency.aggregated.get_center() \n
		Queries the center frequency of the aggregated bandwidth. \n
			:return: frequency_center: Range: 60 MHz to 6010 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:CENTer?')
		return Conversions.str_to_float(response)

	def get_high(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:HIGH \n
		Snippet: value: float = driver.configure.carrierAggregation.frequency.aggregated.get_high() \n
		Queries the upper edge of the aggregated bandwidth. \n
			:return: frequency_high: Range: 60 MHz to 6010 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:CAGGregation:FREQuency:AGGRegated:HIGH?')
		return Conversions.str_to_float(response)
