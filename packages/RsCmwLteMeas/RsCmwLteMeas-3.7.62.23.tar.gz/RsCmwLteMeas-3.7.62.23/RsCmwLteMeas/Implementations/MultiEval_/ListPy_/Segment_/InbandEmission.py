from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InbandEmission:
	"""InbandEmission commands group definition. 18 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("inbandEmission", core, parent)

	@property
	def scc(self):
		"""scc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .InbandEmission_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .InbandEmission_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def margin(self):
		"""margin commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .InbandEmission_.Margin import Margin
			self._margin = Margin(self._core, self._base)
		return self._margin

	def clone(self) -> 'InbandEmission':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InbandEmission(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
