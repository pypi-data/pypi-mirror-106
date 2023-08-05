from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelBw2nd:
	"""ChannelBw2nd commands group definition. 2 total commands, 1 Sub-groups, 1 group commands
	Repeated Capability: SecondChannelBw, default value after init: SecondChannelBw.Bw50"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channelBw2nd", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondChannelBw_get', 'repcap_secondChannelBw_set', repcap.SecondChannelBw.Bw50)

	def repcap_secondChannelBw_set(self, enum_value: repcap.SecondChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondChannelBw.Default
		Default value after init: SecondChannelBw.Bw50"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondChannelBw_get(self) -> repcap.SecondChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def channelBw3rd(self):
		"""channelBw3rd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw3rd'):
			from .ChannelBw2nd_.ChannelBw3rd import ChannelBw3rd
			self._channelBw3rd = ChannelBw3rd(self._core, self._base)
		return self._channelBw3rd

	def set(self, obw_limit: float or bool, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2> \n
		Snippet: driver.configure.multiEval.limit.seMask.obwLimit.carrierAggregation.channelBw1st.channelBw2nd.set(obw_limit = 1.0, firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default) \n
		Defines an upper limit for the occupied bandwidth. The setting is defined separately for each channel bandwidth
		combination, for two aggregated carriers. The following bandwidth combinations are supported: Example: For the first line
		in the figure, use ...:CBANdwidth200:CBANdwidth50. \n
			:param obw_limit: Range: 0 MHz to 40 MHz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')"""
		param = Conversions.decimal_or_bool_value_to_str(obw_limit)
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val} {param}')

	def get(self, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default) -> float or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2> \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.seMask.obwLimit.carrierAggregation.channelBw1st.channelBw2nd.get(firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default) \n
		Defines an upper limit for the occupied bandwidth. The setting is defined separately for each channel bandwidth
		combination, for two aggregated carriers. The following bandwidth combinations are supported: Example: For the first line
		in the figure, use ...:CBANdwidth200:CBANdwidth50. \n
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:return: obw_limit: Range: 0 MHz to 40 MHz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		response = self._core.io.query_str(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}?')
		return Conversions.str_to_float_or_bool(response)

	def clone(self) -> 'ChannelBw2nd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw2nd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
