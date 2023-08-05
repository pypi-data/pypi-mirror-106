from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 344 total commands, 9 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def sreliability(self):
		"""sreliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sreliability'):
			from .ListPy_.Sreliability import Sreliability
			self._sreliability = Sreliability(self._core, self._base)
		return self._sreliability

	@property
	def modulation(self):
		"""modulation commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .ListPy_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def inbandEmission(self):
		"""inbandEmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inbandEmission'):
			from .ListPy_.InbandEmission import InbandEmission
			self._inbandEmission = InbandEmission(self._core, self._base)
		return self._inbandEmission

	@property
	def esFlatness(self):
		"""esFlatness commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_esFlatness'):
			from .ListPy_.EsFlatness import EsFlatness
			self._esFlatness = EsFlatness(self._core, self._base)
		return self._esFlatness

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def seMask(self):
		"""seMask commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .ListPy_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .ListPy_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .ListPy_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def pmonitor(self):
		"""pmonitor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmonitor'):
			from .ListPy_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
