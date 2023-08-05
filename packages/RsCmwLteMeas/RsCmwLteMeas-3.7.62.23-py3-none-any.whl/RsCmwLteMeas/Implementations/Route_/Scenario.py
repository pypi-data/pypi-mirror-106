from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 4 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def combinedSignalPath(self):
		"""combinedSignalPath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_combinedSignalPath'):
			from .Scenario_.CombinedSignalPath import CombinedSignalPath
			self._combinedSignalPath = CombinedSignalPath(self._core, self._base)
		return self._combinedSignalPath

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .Scenario_.MaProtocol import MaProtocol
			self._maProtocol = MaProtocol(self._core, self._base)
		return self._maProtocol

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rf_Converter: enums.RxConverter: RX module for the input path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rf_Converter: enums.RxConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:LTE:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.scenario.get_salone() \n
		Activates the standalone scenario and selects the RF input path for the measured RF signal. For possible connector and
		converter values, see 'Values for RF Path Selection'. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:LTE:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.scenario.set_salone(value = SaloneStruct()) \n
		Activates the standalone scenario and selects the RF input path for the measured RF signal. For possible connector and
		converter values, see 'Values for RF Path Selection'. \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:LTE:MEASurement<Instance>:SCENario:SALone', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:LTE:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: scenario: SALone | CSPath | MAPRotocol SALone: Standalone (non-signaling) CSPath: Combined signal path MAPRotocol: Measure at protocol test
		"""
		response = self._core.io.query_str('ROUTe:LTE:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
