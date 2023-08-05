from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	# noinspection PyTypeChecker
	class PdynamicsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: disables the limit check ON: enables the limit check
			- On_Power_Upper: float: Upper limit for the ON power Range: -256 dBm to 256 dBm, Unit: dBm
			- On_Power_Lower: float: Lower limit for the ON power Range: -256 dBm to 256 dBm, Unit: dBm
			- Off_Power_Upper: float: Upper limit for the OFF power Range: -256 dBm to 256 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('On_Power_Upper'),
			ArgStruct.scalar_float('On_Power_Lower'),
			ArgStruct.scalar_float('Off_Power_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.On_Power_Upper: float = None
			self.On_Power_Lower: float = None
			self.Off_Power_Upper: float = None

	def get_pdynamics(self) -> PdynamicsStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:SRS:LIMit:PDYNamics \n
		Snippet: value: PdynamicsStruct = driver.configure.srs.limit.get_pdynamics() \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. \n
			:return: structure: for return value, see the help for PdynamicsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:SRS:LIMit:PDYNamics?', self.__class__.PdynamicsStruct())

	def set_pdynamics(self, value: PdynamicsStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:SRS:LIMit:PDYNamics \n
		Snippet: driver.configure.srs.limit.set_pdynamics(value = PdynamicsStruct()) \n
		Defines limits for the ON power and OFF power determined with the power dynamics measurement. \n
			:param value: see the help for PdynamicsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:SRS:LIMit:PDYNamics', value)
