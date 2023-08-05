from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 16 total commands, 13 Sub-groups, 0 group commands
	Repeated Capability: Segment, default value after init: Segment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("segment", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_segment_get', 'repcap_segment_set', repcap.Segment.Nr1)

	def repcap_segment_set(self, enum_value: repcap.Segment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Segment.Default
		Default value after init: Segment.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_segment_get(self) -> repcap.Segment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def scc(self):
		"""scc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scc'):
			from .Segment_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	@property
	def cc(self):
		"""cc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cc'):
			from .Segment_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def carrierAggregation(self):
		"""carrierAggregation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrierAggregation'):
			from .Segment_.CarrierAggregation import CarrierAggregation
			self._carrierAggregation = CarrierAggregation(self._core, self._base)
		return self._carrierAggregation

	@property
	def setup(self):
		"""setup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_setup'):
			from .Segment_.Setup import Setup
			self._setup = Setup(self._core, self._base)
		return self._setup

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Segment_.Tdd import Tdd
			self._tdd = Tdd(self._core, self._base)
		return self._tdd

	@property
	def rbAllocation(self):
		"""rbAllocation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbAllocation'):
			from .Segment_.RbAllocation import RbAllocation
			self._rbAllocation = RbAllocation(self._core, self._base)
		return self._rbAllocation

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Segment_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def seMask(self):
		"""seMask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seMask'):
			from .Segment_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Segment_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pmonitor(self):
		"""pmonitor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmonitor'):
			from .Segment_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Segment_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def emtc(self):
		"""emtc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_emtc'):
			from .Segment_.Emtc import Emtc
			self._emtc = Emtc(self._core, self._base)
		return self._emtc

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .Segment_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
