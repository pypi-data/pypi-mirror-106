from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitude:
	"""EvMagnitude commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evMagnitude", core, parent)

	# noinspection PyTypeChecker
	class EvmSymbolStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: Do not measure the results and hide the result diagram ON: Measure the results and show the diagram
			- Symbol: int: SC-FDMA symbol to be evaluated Range: 0 to 6
			- Low_High: enums.LowHigh: LOW | HIGH Low or high EVM window position"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_int('Symbol'),
			ArgStruct.scalar_enum('Low_High', enums.LowHigh)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Symbol: int = None
			self.Low_High: enums.LowHigh = None

	def get_evm_symbol(self) -> EvmSymbolStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude:EVMSymbol \n
		Snippet: value: EvmSymbolStruct = driver.configure.multiEval.result.evMagnitude.get_evm_symbol() \n
		Enables or disables the measurement of EVM vs. modulation symbol results and configures the scope of the measurement. \n
			:return: structure: for return value, see the help for EvmSymbolStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude:EVMSymbol?', self.__class__.EvmSymbolStruct())

	def set_evm_symbol(self, value: EvmSymbolStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude:EVMSymbol \n
		Snippet: driver.configure.multiEval.result.evMagnitude.set_evm_symbol(value = EvmSymbolStruct()) \n
		Enables or disables the measurement of EVM vs. modulation symbol results and configures the scope of the measurement. \n
			:param value: see the help for EvmSymbolStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude:EVMSymbol', value)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.multiEval.result.evMagnitude.get_value() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
			Table Header: Mnemonic / View type \n
			- EVMagnitude / Error vector magnitude
			- MERRor / Magnitude error
			- IEMissions / Inband emissions
			- ESFLatness / Equalizer spectrum flatness
			- SEMask / Spectrum emission mask
			- RBATable / Resource block allocation table
			- BLER / Block error ratio
			- EVMC / EVM vs. subcarrier
			- PERRor / Phase error
			- IQ / I/Q constellation diagram
			- TXM / TX meas. statistical overview
			- ACLR / Adj. channel leakage power ratio
			- PMONitor / Power monitor
			- PDYNamics / Power dynamics
		For reset values, see CONFigure:LTE:MEAS<i>:MEValuation. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.multiEval.result.evMagnitude.set_value(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
			Table Header: Mnemonic / View type \n
			- EVMagnitude / Error vector magnitude
			- MERRor / Magnitude error
			- IEMissions / Inband emissions
			- ESFLatness / Equalizer spectrum flatness
			- SEMask / Spectrum emission mask
			- RBATable / Resource block allocation table
			- BLER / Block error ratio
			- EVMC / EVM vs. subcarrier
			- PERRor / Phase error
			- IQ / I/Q constellation diagram
			- TXM / TX meas. statistical overview
			- ACLR / Adj. channel leakage power ratio
			- PMONitor / Power monitor
			- PDYNamics / Power dynamics
		For reset values, see CONFigure:LTE:MEAS<i>:MEValuation. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')
