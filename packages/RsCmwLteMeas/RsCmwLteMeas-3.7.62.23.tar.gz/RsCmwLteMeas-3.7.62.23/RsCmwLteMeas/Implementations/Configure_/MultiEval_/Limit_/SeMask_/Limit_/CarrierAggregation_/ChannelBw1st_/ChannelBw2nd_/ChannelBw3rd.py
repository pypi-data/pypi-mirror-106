from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelBw3rd:
	"""ChannelBw3rd commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: ThirdChannelBw, default value after init: ThirdChannelBw.Bw100"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channelBw3rd", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_thirdChannelBw_get', 'repcap_thirdChannelBw_set', repcap.ThirdChannelBw.Bw100)

	def repcap_thirdChannelBw_set(self, enum_value: repcap.ThirdChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ThirdChannelBw.Default
		Default value after init: ThirdChannelBw.Bw100"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_thirdChannelBw_get(self) -> repcap.ThirdChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ChannelBw3rdStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the aggregated channel bandwidth Range: 0 MHz to 65 MHz, Unit: Hz
			- Frequency_End: float: Stop frequency of the area, relative to the edges of the aggregated channel bandwidth Range: 0 MHz to 65 MHz, Unit: Hz
			- Level: float: Upper limit for the area Range: -256 dBm to 256 dBm, Unit: dBm
			- Rbw: enums.Rbw: K030 | K100 | M1 Resolution bandwidth to be used for the area K030: 30 kHz K100: 100 kHz M1: 1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.Rbw)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.Rbw = None

	def set(self, structure: ChannelBw3rdStruct, limit=repcap.Limit.Default, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default, thirdChannelBw=repcap.ThirdChannelBw.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2>:CBANdwidth<Band3> \n
		Snippet: driver.configure.multiEval.limit.seMask.limit.carrierAggregation.channelBw1st.channelBw2nd.channelBw3rd.set(value = [PROPERTY_STRUCT_NAME](), limit = repcap.Limit.Default, firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default, thirdChannelBw = repcap.ThirdChannelBw.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The settings are defined separately for each channel bandwidth combination,
		for three aggregated carriers. The following bandwidth combinations are supported: Example: For the first line in the
		figure, use ...:CBANdwidth200:CBANdwidth150:CBANdwidth100. \n
			:param structure: for set value, see the help for ChannelBw3rdStruct structure arguments.
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:param thirdChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw3rd')"""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		thirdChannelBw_cmd_val = self._base.get_repcap_cmd_value(thirdChannelBw, repcap.ThirdChannelBw)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}:CBANdwidth{thirdChannelBw_cmd_val}', structure)

	def get(self, limit=repcap.Limit.Default, firstChannelBw=repcap.FirstChannelBw.Default, secondChannelBw=repcap.SecondChannelBw.Default, thirdChannelBw=repcap.ThirdChannelBw.Default) -> ChannelBw3rdStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CAGGregation:CBANdwidth<Band1>:CBANdwidth<Band2>:CBANdwidth<Band3> \n
		Snippet: value: ChannelBw3rdStruct = driver.configure.multiEval.limit.seMask.limit.carrierAggregation.channelBw1st.channelBw2nd.channelBw3rd.get(limit = repcap.Limit.Default, firstChannelBw = repcap.FirstChannelBw.Default, secondChannelBw = repcap.SecondChannelBw.Default, thirdChannelBw = repcap.ThirdChannelBw.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The settings are defined separately for each channel bandwidth combination,
		for three aggregated carriers. The following bandwidth combinations are supported: Example: For the first line in the
		figure, use ...:CBANdwidth200:CBANdwidth150:CBANdwidth100. \n
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param firstChannelBw: optional repeated capability selector. Default value: Bw150 (settable in the interface 'ChannelBw1st')
			:param secondChannelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'ChannelBw2nd')
			:param thirdChannelBw: optional repeated capability selector. Default value: Bw100 (settable in the interface 'ChannelBw3rd')
			:return: structure: for return value, see the help for ChannelBw3rdStruct structure arguments."""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		firstChannelBw_cmd_val = self._base.get_repcap_cmd_value(firstChannelBw, repcap.FirstChannelBw)
		secondChannelBw_cmd_val = self._base.get_repcap_cmd_value(secondChannelBw, repcap.SecondChannelBw)
		thirdChannelBw_cmd_val = self._base.get_repcap_cmd_value(thirdChannelBw, repcap.ThirdChannelBw)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CAGGregation:CBANdwidth{firstChannelBw_cmd_val}:CBANdwidth{secondChannelBw_cmd_val}:CBANdwidth{thirdChannelBw_cmd_val}?', self.__class__.ChannelBw3rdStruct())

	def clone(self) -> 'ChannelBw3rd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelBw3rd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
