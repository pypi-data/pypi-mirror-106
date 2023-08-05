from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utra:
	"""Utra commands group definition. 8 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: UtraAdjChannel, default value after init: UtraAdjChannel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("utra", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_utraAdjChannel_get', 'repcap_utraAdjChannel_set', repcap.UtraAdjChannel.Ch1)

	def repcap_utraAdjChannel_set(self, enum_value: repcap.UtraAdjChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UtraAdjChannel.Default
		Default value after init: UtraAdjChannel.Ch1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_utraAdjChannel_get(self) -> repcap.UtraAdjChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def negativ(self):
		"""negativ commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_negativ'):
			from .Utra_.Negativ import Negativ
			self._negativ = Negativ(self._core, self._base)
		return self._negativ

	@property
	def positiv(self):
		"""positiv commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_positiv'):
			from .Utra_.Positiv import Positiv
			self._positiv = Positiv(self._core, self._base)
		return self._positiv

	def clone(self) -> 'Utra':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Utra(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
