from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eutra:
	"""Eutra commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eutra", core, parent)

	@property
	def channelBw(self):
		"""channelBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw'):
			from .Eutra_.ChannelBw import ChannelBw
			self._channelBw = ChannelBw(self._core, self._base)
		return self._channelBw

	@property
	def carrierAggregation(self):
		"""carrierAggregation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrierAggregation'):
			from .Eutra_.CarrierAggregation import CarrierAggregation
			self._carrierAggregation = CarrierAggregation(self._core, self._base)
		return self._carrierAggregation

	def clone(self) -> 'Eutra':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eutra(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
