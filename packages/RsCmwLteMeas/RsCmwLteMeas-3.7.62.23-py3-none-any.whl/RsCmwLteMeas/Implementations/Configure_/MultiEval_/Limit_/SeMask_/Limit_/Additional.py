from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Additional:
	"""Additional commands group definition. 4 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: Table, default value after init: Table.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("additional", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_table_get', 'repcap_table_set', repcap.Table.Nr1)

	def repcap_table_set(self, enum_value: repcap.Table) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Table.Default
		Default value after init: Table.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_table_get(self) -> repcap.Table:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def channelBw(self):
		"""channelBw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw'):
			from .Additional_.ChannelBw import ChannelBw
			self._channelBw = ChannelBw(self._core, self._base)
		return self._channelBw

	@property
	def carrierAggregation(self):
		"""carrierAggregation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrierAggregation'):
			from .Additional_.CarrierAggregation import CarrierAggregation
			self._carrierAggregation = CarrierAggregation(self._core, self._base)
		return self._carrierAggregation

	def clone(self) -> 'Additional':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Additional(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
