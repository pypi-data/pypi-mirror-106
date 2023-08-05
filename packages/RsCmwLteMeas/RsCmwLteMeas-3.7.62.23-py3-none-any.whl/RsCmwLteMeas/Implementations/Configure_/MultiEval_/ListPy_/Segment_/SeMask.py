from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	# noinspection PyTypeChecker
	class SeMaskStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Sem_Statistics: int: Statistical length in slots Range: 1 to 1000
			- Se_Enable: bool: OFF | ON Enable or disable the measurement of spectrum emission results ON: Spectrum emission results are measured according to the other enable flags in this command. Results for which there is no explicit enable flag are also measured. OFF: No spectrum emission results at all are measured. The other enable flags in this command are ignored.
			- Obw_Enable: bool: OFF | ON Enable or disable measurement of occupied bandwidth
			- Sem_Enable: bool: OFF | ON Enable or disable measurement of spectrum emission trace and margin results"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sem_Statistics'),
			ArgStruct.scalar_bool('Se_Enable'),
			ArgStruct.scalar_bool('Obw_Enable'),
			ArgStruct.scalar_bool('Sem_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sem_Statistics: int = None
			self.Se_Enable: bool = None
			self.Obw_Enable: bool = None
			self.Sem_Enable: bool = None

	def set(self, structure: SeMaskStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SEMask \n
		Snippet: driver.configure.multiEval.listPy.segment.seMask.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param structure: for set value, see the help for SeMaskStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SEMask', structure)

	def get(self, segment=repcap.Segment.Default) -> SeMaskStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SEMask \n
		Snippet: value: SeMaskStruct = driver.configure.multiEval.listPy.segment.seMask.get(segment = repcap.Segment.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SeMaskStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SEMask?', self.__class__.SeMaskStruct())
