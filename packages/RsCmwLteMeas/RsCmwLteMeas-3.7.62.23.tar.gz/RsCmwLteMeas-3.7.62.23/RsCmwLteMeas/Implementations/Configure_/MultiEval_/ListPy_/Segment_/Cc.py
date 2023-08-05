from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, enum_value: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class CcStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Frequency: float: Center frequency of the component carrier, used in the segment Range: 70 MHz to 6 GHz, Unit: Hz
			- Ch_Bandwidth: enums.ChannelBandwidth: B014 | B030 | B050 | B100 | B150 | B200 Channel bandwidth of the component carrier, used in the segment B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Ch_Bandwidth', enums.ChannelBandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: float = None
			self.Ch_Bandwidth: enums.ChannelBandwidth = None

	def set(self, structure: CcStruct, segment=repcap.Segment.Default, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CC<c> \n
		Snippet: driver.configure.multiEval.listPy.segment.cc.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		Defines carrier-specific analyzer settings for component carrier CC<c>, in segment <no>. This command is only relevant
		for carrier aggregation. The supported frequency range depends on the instrument model and the available options.
		The supported range can be smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param structure: for set value, see the help for CcStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CC{carrierComponent_cmd_val}', structure)

	def get(self, segment=repcap.Segment.Default, carrierComponent=repcap.CarrierComponent.Default) -> CcStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CC<c> \n
		Snippet: value: CcStruct = driver.configure.multiEval.listPy.segment.cc.get(segment = repcap.Segment.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		Defines carrier-specific analyzer settings for component carrier CC<c>, in segment <no>. This command is only relevant
		for carrier aggregation. The supported frequency range depends on the instrument model and the available options.
		The supported range can be smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for CcStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CC{carrierComponent_cmd_val}?', self.__class__.CcStruct())

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
