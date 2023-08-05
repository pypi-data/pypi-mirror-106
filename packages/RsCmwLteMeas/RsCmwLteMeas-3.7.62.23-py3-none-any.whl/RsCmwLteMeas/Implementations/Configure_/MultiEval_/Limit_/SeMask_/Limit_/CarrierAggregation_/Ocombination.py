from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocombination:
	"""Ocombination commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ocombination", core, parent)

	# noinspection PyTypeChecker
	class OcombinationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the aggregated channel bandwidth Range: 0 MHz to 65 MHz, Unit: Hz
			- Frequency_End: float: Stop frequency of the area, relative to the edges of the aggregated channel bandwidth Range: 0 MHz to 65 MHz, Unit: Hz
			- Level: float: Upper limit for the area Range: -256 dBm to 256 dBm, Unit: dBm
			- Rbw: enums.Rbw: K030 | K100 | M1 Resolution bandwidth to be used for the area K030: 30 kHz K100: 100 kHz M1: 1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.Rbw)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.Rbw = None

	def set(self, structure: OcombinationStruct, limit=repcap.Limit.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CAGGregation:OCOMbination \n
		Snippet: driver.configure.multiEval.limit.seMask.limit.carrierAggregation.ocombination.set(value = [PROPERTY_STRUCT_NAME](), limit = repcap.Limit.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The settings apply to all 'other' channel bandwidth combinations, not covered
		by other commands in this section. \n
			:param structure: for set value, see the help for OcombinationStruct structure arguments.
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')"""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CAGGregation:OCOMbination', structure)

	def get(self, limit=repcap.Limit.Default) -> OcombinationStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit<nr>:CAGGregation:OCOMbination \n
		Snippet: value: OcombinationStruct = driver.configure.multiEval.limit.seMask.limit.carrierAggregation.ocombination.get(limit = repcap.Limit.Default) \n
		Defines general requirements for the emission mask area <no>. The activation state, the area borders, an upper limit and
		the resolution bandwidth must be specified. The settings apply to all 'other' channel bandwidth combinations, not covered
		by other commands in this section. \n
			:param limit: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for OcombinationStruct structure arguments."""
		limit_cmd_val = self._base.get_repcap_cmd_value(limit, repcap.Limit)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:LIMit{limit_cmd_val}:CAGGregation:OCOMbination?', self.__class__.OcombinationStruct())
