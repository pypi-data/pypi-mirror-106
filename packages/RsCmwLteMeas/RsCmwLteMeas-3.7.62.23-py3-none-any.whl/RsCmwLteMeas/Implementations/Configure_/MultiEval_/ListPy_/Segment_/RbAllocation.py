from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbAllocation:
	"""RbAllocation commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rbAllocation", core, parent)

	@property
	def sidelink(self):
		"""sidelink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sidelink'):
			from .RbAllocation_.Sidelink import Sidelink
			self._sidelink = Sidelink(self._core, self._base)
		return self._sidelink

	# noinspection PyTypeChecker
	class RbAllocationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Auto: bool: OFF | ON OFF: manual definition via NoRB and Offset ON: automatic detection of RB allocation
			- No_Rb: int: Number of allocated resource blocks in each measured slot Range: see table below
			- Offset: int: Offset of first allocated resource block from edge of allocated UL transmission bandwidth Range: 0 to max(NoRB) - NoRB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Auto'),
			ArgStruct.scalar_int('No_Rb'),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Auto: bool = None
			self.No_Rb: int = None
			self.Offset: int = None

	def set(self, structure: RbAllocationStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RBALlocation \n
		Snippet: driver.configure.multiEval.listPy.segment.rbAllocation.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Allows you to define the uplink resource block allocation manually for segment <no>. By default, the RB allocation is
		detected automatically. \n
			:param structure: for set value, see the help for RbAllocationStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RBALlocation', structure)

	def get(self, segment=repcap.Segment.Default) -> RbAllocationStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:RBALlocation \n
		Snippet: value: RbAllocationStruct = driver.configure.multiEval.listPy.segment.rbAllocation.get(segment = repcap.Segment.Default) \n
		Allows you to define the uplink resource block allocation manually for segment <no>. By default, the RB allocation is
		detected automatically. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for RbAllocationStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:RBALlocation?', self.__class__.RbAllocationStruct())

	def clone(self) -> 'RbAllocation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RbAllocation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
