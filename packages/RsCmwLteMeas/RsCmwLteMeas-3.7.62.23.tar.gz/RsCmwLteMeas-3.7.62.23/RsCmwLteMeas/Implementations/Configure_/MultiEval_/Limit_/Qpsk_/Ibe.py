from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibe:
	"""Ibe commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ibe", core, parent)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Offset_1: float: Offset for high TX power range Range: -256 dBc to 256 dBc, Unit: dB
			- Offset_2: float: Offset for intermediate TX power range Range: -256 dBc to 256 dBc, Unit: dB
			- Offset_3: float: Offset for low TX power range Range: -256 dBc to 256 dBc, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def get_iq_offset(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.multiEval.limit.qpsk.ibe.get_iq_offset() \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission (QPSK modulation) . Three
		different values can be set for three TX power ranges, see 'Inband Emissions Limits'. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE:IQOFfset?', self.__class__.IqOffsetStruct())

	def set_iq_offset(self, value: IqOffsetStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.qpsk.ibe.set_iq_offset(value = IqOffsetStruct()) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission (QPSK modulation) . Three
		different values can be set for three TX power ranges, see 'Inband Emissions Limits'. \n
			:param value: see the help for IqOffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE:IQOFfset', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON OFF: disables the limit check ON: enables the limit check
			- Minimum: float: Range: -256 dB to 256 dB, Unit: dB
			- Evm: float: Range: 0 % to 100 %, Unit: %
			- Rb_Power: float: Range: -256 dBm to 256 dBm, Unit: dBm
			- Iq_Image: float: Range: -256 dB to 256 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Rb_Power'),
			ArgStruct.scalar_float('Iq_Image')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Minimum: float = None
			self.Evm: float = None
			self.Rb_Power: float = None
			self.Iq_Image: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE \n
		Snippet: value: ValueStruct = driver.configure.multiEval.limit.qpsk.ibe.get_value() \n
		Defines parameters used for calculation of an upper limit for the inband emission (QPSK modulation) , see 'Inband
		Emissions Limits'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE \n
		Snippet: driver.configure.multiEval.limit.qpsk.ibe.set_value(value = ValueStruct()) \n
		Defines parameters used for calculation of an upper limit for the inband emission (QPSK modulation) , see 'Inband
		Emissions Limits'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QPSK:IBE', value)
