from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 8 total commands, 3 Sub-groups, 0 group commands
	Repeated Capability: Limit, default value after init: Limit.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_limit_get', 'repcap_limit_set', repcap.Limit.Nr1)

	def repcap_limit_set(self, enum_value: repcap.Limit) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Limit.Default
		Default value after init: Limit.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_limit_get(self) -> repcap.Limit:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def channelBw(self):
		"""channelBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw'):
			from .Limit_.ChannelBw import ChannelBw
			self._channelBw = ChannelBw(self._core, self._base)
		return self._channelBw

	@property
	def additional(self):
		"""additional commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_additional'):
			from .Limit_.Additional import Additional
			self._additional = Additional(self._core, self._base)
		return self._additional

	@property
	def carrierAggregation(self):
		"""carrierAggregation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrierAggregation'):
			from .Limit_.CarrierAggregation import CarrierAggregation
			self._carrierAggregation = CarrierAggregation(self._core, self._base)
		return self._carrierAggregation

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
