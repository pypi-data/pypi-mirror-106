from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CombinedSignalPath:
	"""CombinedSignalPath commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("combinedSignalPath", core, parent)

	def set(self, master: str, carrier: str = None) -> None:
		"""SCPI: ROUTe:LTE:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.scenario.combinedSignalPath.set(master = '1', carrier = '1') \n
		Activates the combined signal path scenario and selects the master application and carrier. The master controls most
		signal routing settings, analyzer settings and some measurement control settings while the combined signal path scenario
		is active. The command usage depends on the carrier aggregation mode of the measured signal: no UL carrier aggregation,
		non-contiguous UL carrier aggregation or intraband contiguous UL carrier aggregation. The following table provides an
		overview.
			Table Header: CA type / Setting command / Query returns \n
			- No UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master> <Carrier> can be skipped and equals 'PCC'. / <Master>, 'PCC'
			- Non-contiguous UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master>, <Carrier> <Carrier>: measured carrier ('PCC', 'SCC2', ...) / <Master>, <Carrier>
			- Intraband contiguous UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master>, <Carrier> <Carrier>: set of carriers ('Set A', 'Set B', ...) / <Master>, <Carrier>, <Set> <Carrier>: carrier selecting RF path ('PCC', 'SCC2', ...) <Set>: measured set of carriers ('Set A', 'Set B', ...) \n
			:param master: String parameter selecting the master application Example: 'LTE Sig1' or 'LTE Sig2'
			:param carrier: String parameter selecting an uplink carrier or a set of uplink carriers configured in the master application Examples: 'PCC', 'SCC2', 'Set A', 'Set B' If a set is selected, a query returns the carrier of the set that is used by the measurement to select the RF path.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('master', master, DataType.String), ArgSingle('carrier', carrier, DataType.String, True))
		self._core.io.write(f'ROUTe:LTE:MEASurement<Instance>:SCENario:CSPath {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Master: str: String parameter selecting the master application Example: 'LTE Sig1' or 'LTE Sig2'
			- Carrier: str: String parameter selecting an uplink carrier or a set of uplink carriers configured in the master application Examples: 'PCC', 'SCC2', 'Set A', 'Set B' If a set is selected, a query returns the carrier of the set that is used by the measurement to select the RF path.
			- Set_Py: str: String parameter indicating the measured set of uplink carriers ('Set A' or 'Set B') . Only returned for intraband contiguous UL CA."""
		__meta_args_list = [
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_str('Carrier'),
			ArgStruct.scalar_str('Set_Py')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Master: str = None
			self.Carrier: str = None
			self.Set_Py: str = None

	def get(self) -> GetStruct:
		"""SCPI: ROUTe:LTE:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: GetStruct = driver.route.scenario.combinedSignalPath.get() \n
		Activates the combined signal path scenario and selects the master application and carrier. The master controls most
		signal routing settings, analyzer settings and some measurement control settings while the combined signal path scenario
		is active. The command usage depends on the carrier aggregation mode of the measured signal: no UL carrier aggregation,
		non-contiguous UL carrier aggregation or intraband contiguous UL carrier aggregation. The following table provides an
		overview.
			Table Header: CA type / Setting command / Query returns \n
			- No UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master> <Carrier> can be skipped and equals 'PCC'. / <Master>, 'PCC'
			- Non-contiguous UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master>, <Carrier> <Carrier>: measured carrier ('PCC', 'SCC2', ...) / <Master>, <Carrier>
			- Intraband contiguous UL CA / ROUT:LTE:MEAS<i>:SCEN:CSP <Master>, <Carrier> <Carrier>: set of carriers ('Set A', 'Set B', ...) / <Master>, <Carrier>, <Set> <Carrier>: carrier selecting RF path ('PCC', 'SCC2', ...) <Set>: measured set of carriers ('Set A', 'Set B', ...) \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:LTE:MEASurement<Instance>:SCENario:CSPath?', self.__class__.GetStruct())
