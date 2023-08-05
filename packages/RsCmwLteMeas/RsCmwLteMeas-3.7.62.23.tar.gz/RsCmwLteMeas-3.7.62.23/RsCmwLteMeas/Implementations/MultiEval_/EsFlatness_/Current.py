from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def scIndex(self):
		"""scIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scIndex'):
			from .Current_.ScIndex import ScIndex
			self._scIndex = ScIndex(self._core, self._base)
		return self._scIndex

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified equalizer spectrum flatness limits. Unit: %
			- Ripple_1: float: Max (range 1) - min (range 1) Unit: dB
			- Ripple_2: float: Max (range 2) - min (range 2) Unit: dB
			- Max_R_1_Min_R_2: float: Max (range 1) - min (range 2) Unit: dB
			- Max_R_2_Min_R_1: float: Max (range 2) - min (range 1) Unit: dB
			- Min_R_1: float: Min (range 1) Unit: dB
			- Max_R_1: float: Max (range 1) Unit: dB
			- Min_R_2: float: Min (range 2) Unit: dB
			- Max_R_2: float: Max (range 2) Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Ripple_1'),
			ArgStruct.scalar_float('Ripple_2'),
			ArgStruct.scalar_float('Max_R_1_Min_R_2'),
			ArgStruct.scalar_float('Max_R_2_Min_R_1'),
			ArgStruct.scalar_float('Min_R_1'),
			ArgStruct.scalar_float('Max_R_1'),
			ArgStruct.scalar_float('Min_R_2'),
			ArgStruct.scalar_float('Max_R_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Ripple_1: float = None
			self.Ripple_2: float = None
			self.Max_R_1_Min_R_2: float = None
			self.Max_R_2_Min_R_1: float = None
			self.Min_R_1: float = None
			self.Max_R_1: float = None
			self.Min_R_2: float = None
			self.Max_R_2: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent \n
		Snippet: value: ResultData = driver.multiEval.esFlatness.current.read() \n
		Return current, average, extreme and standard deviation single value results of the equalizer spectrum flatness
		measurement. See also 'Equalizer Spectrum Flatness Limits'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent \n
		Snippet: value: ResultData = driver.multiEval.esFlatness.current.fetch() \n
		Return current, average, extreme and standard deviation single value results of the equalizer spectrum flatness
		measurement. See also 'Equalizer Spectrum Flatness Limits'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified equalizer spectrum flatness limits. Unit: %
			- Ripple_1: float: Limit check result for max (range 1) - min (range 1)
			- Ripple_2: float: Limit check result for max (range 2) - min (range 2)
			- Max_R_1_Min_R_2: float: Limit check result for max (range 1) - min (range 2)
			- Max_R_2_Min_R_1: float: Limit check result for max (range 2) - min (range 1)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Ripple_1'),
			ArgStruct.scalar_float('Ripple_2'),
			ArgStruct.scalar_float('Max_R_1_Min_R_2'),
			ArgStruct.scalar_float('Max_R_2_Min_R_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Ripple_1: float = None
			self.Ripple_2: float = None
			self.Max_R_1_Min_R_2: float = None
			self.Max_R_2_Min_R_1: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.esFlatness.current.calculate() \n
		Return current, average and extreme single value results of the equalizer spectrum flatness measurement.
		See also 'Equalizer Spectrum Flatness Limits'. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:LTE:MEASurement<Instance>:MEValuation:ESFLatness:CURRent?', self.__class__.CalculateStruct())

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
