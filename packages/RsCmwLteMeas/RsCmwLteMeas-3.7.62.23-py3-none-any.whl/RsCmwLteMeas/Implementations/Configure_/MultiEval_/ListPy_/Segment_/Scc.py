from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scc:
	"""Scc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: SecondaryCC, default value after init: SecondaryCC.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_secondaryCC_get', 'repcap_secondaryCC_set', repcap.SecondaryCC.CC1)

	def repcap_secondaryCC_set(self, enum_value: repcap.SecondaryCC) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCC.Default
		Default value after init: SecondaryCC.CC1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_secondaryCC_get(self) -> repcap.SecondaryCC:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class SccStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Frequency: float: No parameter help available
			- Ch_Bandwidth: enums.ChannelBandwidth: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Ch_Bandwidth', enums.ChannelBandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: float = None
			self.Ch_Bandwidth: enums.ChannelBandwidth = None

	def set(self, structure: SccStruct, segment=repcap.Segment.Default, secondaryCC=repcap.SecondaryCC.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCC<c> \n
		Snippet: driver.configure.multiEval.listPy.segment.scc.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default, secondaryCC = repcap.SecondaryCC.Default) \n
		No command help available \n
			:param structure: for set value, see the help for SccStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param secondaryCC: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		secondaryCC_cmd_val = self._base.get_repcap_cmd_value(secondaryCC, repcap.SecondaryCC)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCC{secondaryCC_cmd_val}', structure)

	def get(self, segment=repcap.Segment.Default, secondaryCC=repcap.SecondaryCC.Default) -> SccStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SCC<c> \n
		Snippet: value: SccStruct = driver.configure.multiEval.listPy.segment.scc.get(segment = repcap.Segment.Default, secondaryCC = repcap.SecondaryCC.Default) \n
		No command help available \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param secondaryCC: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for SccStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		secondaryCC_cmd_val = self._base.get_repcap_cmd_value(secondaryCC, repcap.SecondaryCC)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SCC{secondaryCC_cmd_val}?', self.__class__.SccStruct())

	def clone(self) -> 'Scc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
