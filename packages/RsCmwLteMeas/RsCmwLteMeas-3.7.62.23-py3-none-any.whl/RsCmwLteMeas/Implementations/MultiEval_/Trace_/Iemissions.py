from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iemissions:
	"""Iemissions commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iemissions", core, parent)

	@property
	def cc(self):
		"""cc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cc'):
			from .Iemissions_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	def clone(self) -> 'Iemissions':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iemissions(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
