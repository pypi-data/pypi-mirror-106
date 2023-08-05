from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orb:
	"""Orb commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: RBoffset, default value after init: RBoffset.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("orb", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_rBoffset_get', 'repcap_rBoffset_set', repcap.RBoffset.Nr1)

	def repcap_rBoffset_set(self, enum_value: repcap.RBoffset) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RBoffset.Default
		Default value after init: RBoffset.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_rBoffset_get(self) -> repcap.RBoffset:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, offset_rb: int, rBoffset=repcap.RBoffset.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RBALlocation:MCLuster:ORB<Number> \n
		Snippet: driver.configure.multiEval.rbAllocation.mcluster.orb.set(offset_rb = 1, rBoffset = repcap.RBoffset.Default) \n
		Specifies the offset of the first allocated resource block, for multi-cluster allocation.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:RMC:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:UDCHannels:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:CONNection:SCC<c>:RMC:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:CONNection:SCC<c>:UDCHannels:MCLuster:UL \n
			:param offset_rb: For the allowed input ranges, see 'Uplink Resource Block Allocation'.
			:param rBoffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Orb')"""
		param = Conversions.decimal_value_to_str(offset_rb)
		rBoffset_cmd_val = self._base.get_repcap_cmd_value(rBoffset, repcap.RBoffset)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:RBALlocation:MCLuster:ORB{rBoffset_cmd_val} {param}')

	def get(self, rBoffset=repcap.RBoffset.Default) -> int:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RBALlocation:MCLuster:ORB<Number> \n
		Snippet: value: int = driver.configure.multiEval.rbAllocation.mcluster.orb.get(rBoffset = repcap.RBoffset.Default) \n
		Specifies the offset of the first allocated resource block, for multi-cluster allocation.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:RMC:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:UDCHannels:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:CONNection:SCC<c>:RMC:MCLuster:UL
			- CONFigure:LTE:SIGN<i>:CONNection:SCC<c>:UDCHannels:MCLuster:UL \n
			:param rBoffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Orb')
			:return: offset_rb: For the allowed input ranges, see 'Uplink Resource Block Allocation'."""
		rBoffset_cmd_val = self._base.get_repcap_cmd_value(rBoffset, repcap.RBoffset)
		response = self._core.io.query_str(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:RBALlocation:MCLuster:ORB{rBoffset_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Orb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Orb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
