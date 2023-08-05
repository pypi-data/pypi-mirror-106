from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsIndex:
	"""DsIndex commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dsIndex", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .DsIndex_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	def fetch(self) -> int:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:PRACh:MODulation:DSINdex \n
		Snippet: value: int = driver.prach.modulation.dsIndex.fetch() \n
		Returns the automatically detected or manually configured sequence index for single-preamble measurements. \n
		Use RsCmwLteMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: sequence_index: Sequence index"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:LTE:MEASurement<Instance>:PRACh:MODulation:DSINdex?', suppressed)
		return Conversions.str_to_int(response)

	def clone(self) -> 'DsIndex':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DsIndex(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
