from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 20 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def segment(self):
		"""segment commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def singleCmw(self):
		"""singleCmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	# noinspection PyTypeChecker
	class LrangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: First measured segment in the range of configured segments Range: 1 to 2000
			- Nr_Segments: int: Number of measured segments Range: 1 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Nr_Segments')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Nr_Segments: int = None

	def get_lrange(self) -> LrangeStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: value: LrangeStruct = driver.configure.multiEval.listPy.get_lrange() \n
		Select a range of measured segments. The segments must be configured using method RsCmwLteMeas.Configure.MultiEval.ListPy.
		Segment.Setup.set. \n
			:return: structure: for return value, see the help for LrangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge?', self.__class__.LrangeStruct())

	def set_lrange(self, value: LrangeStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: driver.configure.multiEval.listPy.set_lrange(value = LrangeStruct()) \n
		Select a range of measured segments. The segments must be configured using method RsCmwLteMeas.Configure.MultiEval.ListPy.
		Segment.Setup.set. \n
			:param value: see the help for LrangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:LRANge', value)

	def get_os_index(self) -> int or bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: value: int or bool = driver.configure.multiEval.listPy.get_os_index() \n
		Selects the number of the segment to be displayed in offline mode. The index refers to the range of measured segments,
		see method RsCmwLteMeas.Configure.MultiEval.ListPy.lrange. Setting a value also enables the offline mode. \n
			:return: offline_seg_index: Range: 1 to number of measured segments Additional parameters: OFF (disables the offline mode)
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex?')
		return Conversions.str_to_int_or_bool(response)

	def set_os_index(self, offline_seg_index: int or bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: driver.configure.multiEval.listPy.set_os_index(offline_seg_index = 1) \n
		Selects the number of the segment to be displayed in offline mode. The index refers to the range of measured segments,
		see method RsCmwLteMeas.Configure.MultiEval.ListPy.lrange. Setting a value also enables the offline mode. \n
			:param offline_seg_index: Range: 1 to number of measured segments Additional parameters: OFF (disables the offline mode)
		"""
		param = Conversions.decimal_or_bool_value_to_str(offline_seg_index)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:OSINdex {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: value: bool = driver.configure.multiEval.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF | ON OFF: Disable list mode ON: Enable list mode
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: driver.configure.multiEval.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF | ON OFF: Disable list mode ON: Enable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
