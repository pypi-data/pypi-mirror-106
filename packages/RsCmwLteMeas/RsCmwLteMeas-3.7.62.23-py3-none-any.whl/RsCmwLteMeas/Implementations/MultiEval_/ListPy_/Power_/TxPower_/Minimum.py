from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:LIST:POWer:TXPower:MINimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.power.txPower.minimum.fetch() \n
		Return the total TX power of all component carriers, for all measured list mode segments. \n
		Use RsCmwLteMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: tx_power: Comma-separated list of values, one per measured segment Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:LTE:MEASurement<Instance>:MEValuation:LIST:POWer:TXPower:MINimum?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:LTE:MEASurement<Instance>:MEValuation:LIST:POWer:TXPower:MINimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.power.txPower.minimum.calculate() \n
		No command help available \n
		Use RsCmwLteMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: tx_power: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:LTE:MEASurement<Instance>:MEValuation:LIST:POWer:TXPower:MINimum?', suppressed)
		return response
