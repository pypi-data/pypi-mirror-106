from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: Number of subframes in the segment Range: 1 to 2000
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
			- Duplex_Mode: enums.DuplexMode: FDD | TDD Duplex mode used in the segment
			- Band: enums.Band: FDD UL: OB1 | ... | OB28 | OB30 | OB31 | OB65 | OB66 | OB68 | OB70 | ... | OB74 | OB85 TDD UL: OB33 | ... | OB45 | OB48 | OB50 | ... | OB52 | OB250 Sidelink: OB47 Operating band used in the segment
			- Frequency: float: Center frequency of CC1 used in the segment Range: 70 MHz to 6 GHz, Unit: Hz
			- Ch_Bandwidth: enums.ChannelBandwidth: B014 | B030 | B050 | B100 | B150 | B200 Channel bandwidth of CC1 used in the segment B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
			- Cyclic_Prefix: enums.CyclicPrefix: NORMal | EXTended Type of cyclic prefix used in the segment
			- Channel_Type: enums.SegmentChannelTypeExtended: AUTO | PUSCh | PUCCh | PSSCh | PSCCh Channel type to be measured in the segment (AUTO for automatic detection) Uplink: AUTO, PUSCh, PUCCh Sidelink: PSSCh, PSCCh
			- Retrigger_Flag: enums.RetriggerFlag: OFF | ON | IFPower Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. For subsequent segments, the retrigger flag is ignored for trigger mode ONCE and evaluated for trigger mode SEGMent, see [CMDLINK: TRIGger:LTE:MEASi:MEValuation:LIST:MODE CMDLINK]. OFF: measure the segment without retrigger ON: wait for a trigger event from the trigger source configured via [CMDLINK: TRIGger:LTE:MEASi:MEValuation:SOURce CMDLINK] IFPower: wait for a trigger event from the trigger source 'IF Power'
			- Evaluat_Offset: int: Number of subframes at the beginning of the segment that are not evaluated Range: 0 to 1000
			- Network_Sig_Value: enums.NetworkSigValueNoCarrAggr: Optional setting parameter. NS01 | ... | NS288 Network signaled value to be used for the segment"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexMode),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Ch_Bandwidth', enums.ChannelBandwidth),
			ArgStruct.scalar_enum('Cyclic_Prefix', enums.CyclicPrefix),
			ArgStruct.scalar_enum('Channel_Type', enums.SegmentChannelTypeExtended),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset'),
			ArgStruct.scalar_enum('Network_Sig_Value', enums.NetworkSigValueNoCarrAggr)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Duplex_Mode: enums.DuplexMode = None
			self.Band: enums.Band = None
			self.Frequency: float = None
			self.Ch_Bandwidth: enums.ChannelBandwidth = None
			self.Cyclic_Prefix: enums.CyclicPrefix = None
			self.Channel_Type: enums.SegmentChannelTypeExtended = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None
			self.Network_Sig_Value: enums.NetworkSigValueNoCarrAggr = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.multiEval.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCmwLteMeas.Configure.MultiEval.ListPy.lrange) . For uplink signals with TDD mode, see also method RsCmwLteMeas.
		Configure.MultiEval.ListPy.Segment.Tdd.set. For carrier-specific settings for carrier aggregation,
		see CONFigure:LTE:MEAS<i>:MEValuation:LIST:SEGMent<no>:CC<c>. The supported frequency range depends on the instrument
		model and the available options. The supported range can be smaller than stated here. Refer to the preface of your
		model-specific base unit manual. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length and analyzer settings of segment <no>. This command must be sent for all segments to be measured
		(method RsCmwLteMeas.Configure.MultiEval.ListPy.lrange) . For uplink signals with TDD mode, see also method RsCmwLteMeas.
		Configure.MultiEval.ListPy.Segment.Tdd.set. For carrier-specific settings for carrier aggregation,
		see CONFigure:LTE:MEAS<i>:MEValuation:LIST:SEGMent<no>:CC<c>. The supported frequency range depends on the instrument
		model and the available options. The supported range can be smaller than stated here. Refer to the preface of your
		model-specific base unit manual. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
