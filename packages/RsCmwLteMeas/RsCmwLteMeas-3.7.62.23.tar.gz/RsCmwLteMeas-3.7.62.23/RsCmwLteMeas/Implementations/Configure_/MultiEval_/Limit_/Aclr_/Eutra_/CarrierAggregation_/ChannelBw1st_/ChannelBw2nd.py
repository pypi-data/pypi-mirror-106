from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
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

	# noinspection PyTypeChecker
	class ChannelBw2ndStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Relative_Level: float or bool: Range: -256 dB to 256 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Absolute_Level: float or bool: Range: -256 dBm to 256 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Relative_Level'),
			ArgStruct.scalar_float_ext('Absolute_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relative_Level: float or bool = None
			self.Absolute_Level: float or bool = None

	def set(self, structure: ChannelBw2ndStruct, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2> \n
		Snippet: driver.configure.multiEval.limit.aclr.eutra.carrierAggregation.channelBw1st.channelBw2nd.set(value = [PROPERTY_STRUCT_NAME](), firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent E-UTRA channel. The settings are defined
		separately for each channel bandwidth combination, for two aggregated carriers. The following bandwidth combinations are
		supported: Example: For the first line in the figure, use ...:CBANdwidth200:CBANdwidth50. \n
			:param structure: for set value, see the help for ChannelBw2ndStruct structure arguments.
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')"""
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}', structure)

	def get(self, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default) -> ChannelBw2ndStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2> \n
		Snippet: value: ChannelBw2ndStruct = driver.configure.multiEval.limit.aclr.eutra.carrierAggregation.channelBw1st.channelBw2nd.get(firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default) \n
		Defines relative and absolute limits for the ACLR measured in an adjacent E-UTRA channel. The settings are defined
		separately for each channel bandwidth combination, for two aggregated carriers. The following bandwidth combinations are
		supported: Example: For the first line in the figure, use ...:CBANdwidth200:CBANdwidth50. \n
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:return: structure: for return value, see the help for ChannelBw2ndStruct structure arguments."""
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:ACLR:EUTRa:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}?', self.__class__.ChannelBw2ndStruct())

	def clone(self) -> 'ChannelBw2nd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw2nd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
