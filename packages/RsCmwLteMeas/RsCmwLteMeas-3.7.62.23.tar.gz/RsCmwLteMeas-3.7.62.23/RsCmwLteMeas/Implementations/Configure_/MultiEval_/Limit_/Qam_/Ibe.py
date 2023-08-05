from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibe:
	"""Ibe commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ibe", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Ibe_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	# noinspection PyTypeChecker
	class IbeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
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

	def set(self, structure: IbeStruct, qAMmodOrder=repcap.QAMmodOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IBE \n
		Snippet: driver.configure.multiEval.limit.qam.ibe.set(value = [PROPERTY_STRUCT_NAME](), qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines parameters used for calculation of an upper limit for the inband emission, for QAM modulations, see 'Inband
		Emissions Limits'. \n
			:param structure: for set value, see the help for IbeStruct structure arguments.
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')"""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IBE', structure)

	def get(self, qAMmodOrder=repcap.QAMmodOrder.Default) -> IbeStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IBE \n
		Snippet: value: IbeStruct = driver.configure.multiEval.limit.qam.ibe.get(qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines parameters used for calculation of an upper limit for the inband emission, for QAM modulations, see 'Inband
		Emissions Limits'. \n
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IbeStruct structure arguments."""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:IBE?', self.__class__.IbeStruct())

	def clone(self) -> 'Ibe':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ibe(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
