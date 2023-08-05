from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Utra_1: bool: OFF | ON
			- Utra_2: bool: OFF | ON
			- Eutra: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Utra_1'),
			ArgStruct.scalar_bool('Utra_2'),
			ArgStruct.scalar_bool('Eutra')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Utra_1: bool = None
			self.Utra_2: bool = None
			self.Eutra: bool = None

	def get_enable(self) -> EnableStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: value: EnableStruct = driver.configure.multiEval.spectrum.aclr.get_enable() \n
		Enables or disables the evaluation of the first adjacent UTRA channels, second adjacent UTRA channels and first adjacent
		E-UTRA channels. \n
			:return: structure: for return value, see the help for EnableStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle?', self.__class__.EnableStruct())

	def set_enable(self, value: EnableStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: driver.configure.multiEval.spectrum.aclr.set_enable(value = EnableStruct()) \n
		Enables or disables the evaluation of the first adjacent UTRA channels, second adjacent UTRA channels and first adjacent
		E-UTRA channels. \n
			:param value: see the help for EnableStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle', value)
