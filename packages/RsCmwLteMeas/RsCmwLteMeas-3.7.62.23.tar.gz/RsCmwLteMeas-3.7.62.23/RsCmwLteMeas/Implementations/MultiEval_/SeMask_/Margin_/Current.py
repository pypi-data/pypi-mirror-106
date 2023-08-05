from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def negativ(self):
		"""negativ commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_negativ'):
			from .Current_.Negativ import Negativ
			self._negativ = Negativ(self._core, self._base)
		return self._negativ

	@property
	def positiv(self):
		"""positiv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_positiv'):
			from .Current_.Positiv import Positiv
			self._positiv = Positiv(self._core, self._base)
		return self._positiv

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
