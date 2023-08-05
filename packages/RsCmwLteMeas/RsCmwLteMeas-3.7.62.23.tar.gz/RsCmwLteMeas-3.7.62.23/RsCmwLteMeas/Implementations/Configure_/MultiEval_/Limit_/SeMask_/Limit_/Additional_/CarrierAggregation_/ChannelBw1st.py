from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelBw1st:
	"""ChannelBw1st commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: FirstChannelBw, default value after init: FirstChannelBw.Bw150"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channelBw1st", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_firstChannelBw_get', 'repcap_firstChannelBw_set', repcap.FirstChannelBw.Bw150)

	def repcap_firstChannelBw_set(self, enum_value: repcap.FirstChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FirstChannelBw.Default
		Default value after init: FirstChannelBw.Bw150"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_firstChannelBw_get(self) -> repcap.FirstChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def channelBw2nd(self):
		"""channelBw2nd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw2nd'):
			from .ChannelBw1st_.ChannelBw2nd import ChannelBw2nd
			self._channelBw2nd = ChannelBw2nd(self._core, self._base)
		return self._channelBw2nd

	def clone(self) -> 'ChannelBw1st':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw1st(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
