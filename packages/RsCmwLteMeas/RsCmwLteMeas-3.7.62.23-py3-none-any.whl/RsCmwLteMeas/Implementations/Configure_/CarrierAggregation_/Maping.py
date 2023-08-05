from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maping:
	"""Maping commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maping", core, parent)

	@property
	def scc(self):
		"""scc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scc'):
			from .Maping_.Scc import Scc
			self._scc = Scc(self._core, self._base)
		return self._scc

	def get_pcc(self) -> str:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:CAGGregation:MAPing:PCC \n
		Snippet: value: str = driver.configure.carrierAggregation.maping.get_pcc() \n
		This command is only relevant for combined signal path measurements with contiguous uplink CA. It queries to which CC the
		PCC is mapped. The measurement identifies the aggregated carriers as CC1 to CC4. The signaling application uses PCC and
		SCC<n>. \n
			:return: cc: String indicating the CC, examples: 'CC1', 'CC2', 'INV' 'INV' means that the PCC is not contained in the measured set of aggregated uplink carriers.
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:CAGGregation:MAPing:PCC?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cc_1: enums.CarrAggrMaping: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Carrier mapped to CC1
			- Cc_2: enums.CarrAggrMaping: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Carrier mapped to CC2
			- Cc_3: enums.CarrAggrMaping: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Carrier mapped to CC3
			- Cc_4: enums.CarrAggrMaping: INV | PCC | SCC1 | SCC2 | SCC3 | SCC4 | SCC5 | SCC6 | SCC7 Carrier mapped to CC4"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Cc_1', enums.CarrAggrMaping),
			ArgStruct.scalar_enum('Cc_2', enums.CarrAggrMaping),
			ArgStruct.scalar_enum('Cc_3', enums.CarrAggrMaping),
			ArgStruct.scalar_enum('Cc_4', enums.CarrAggrMaping)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cc_1: enums.CarrAggrMaping = None
			self.Cc_2: enums.CarrAggrMaping = None
			self.Cc_3: enums.CarrAggrMaping = None
			self.Cc_4: enums.CarrAggrMaping = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:CAGGregation:MAPing \n
		Snippet: value: ValueStruct = driver.configure.carrierAggregation.maping.get_value() \n
		This command is only relevant for combined signal path measurements with contiguous uplink CA. It queries which carriers
		are mapped to CC1 to CC4. The measurement identifies the aggregated carriers as CC1 to CC4. The signaling application
		uses PCC and SCC<n>. A returned INV means that no carrier is mapped to the CC. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:CAGGregation:MAPing?', self.__class__.ValueStruct())

	def clone(self) -> 'Maping':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maping(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
