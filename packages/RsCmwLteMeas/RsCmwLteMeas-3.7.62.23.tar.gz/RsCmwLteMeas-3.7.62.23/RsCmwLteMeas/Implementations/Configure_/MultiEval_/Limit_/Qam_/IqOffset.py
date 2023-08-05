from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffset:
	"""IqOffset commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqOffset", core, parent)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: disables the limit check ON: enables the limit check
			- Offset_1: float: I/Q origin offset limit for high TX power range Range: -256 dBc to 256 dBc, Unit: dBc
			- Offset_2: float: I/Q origin offset limit for intermediate TX power range Range: -256 dBc to 256 dBc, Unit: dBc
			- Offset_3: float: I/Q origin offset limit for low TX power range Range: -256 dBc to 256 dBc, Unit: dBc"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def set(self, structure: IqOffsetStruct, qAMmodOrder=repcap.QAMmodOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.qam.iqOffset.set(value = [PROPERTY_STRUCT_NAME](), qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines upper limits for the I/Q origin offset, for QAM modulations. Three different I/Q origin offset limits can be set
		for three TX power ranges. For details, see 'I/Q Origin Offset Limits'. \n
			:param structure: for set value, see the help for IqOffsetStruct structure arguments.
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')"""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IQOFfset', structure)

	def get(self, qAMmodOrder=repcap.QAMmodOrder.Default) -> IqOffsetStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.multiEval.limit.qam.iqOffset.get(qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines upper limits for the I/Q origin offset, for QAM modulations. Three different I/Q origin offset limits can be set
		for three TX power ranges. For details, see 'I/Q Origin Offset Limits'. \n
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IQOFfset?', self.__class__.IqOffsetStruct())
