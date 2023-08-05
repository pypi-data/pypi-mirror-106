from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitude:
	"""EvMagnitude commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evMagnitude", core, parent)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Rms: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Peak: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def set(self, structure: EvMagnitudeStruct, qAMmodOrder=repcap.QAMmodOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:EVMagnitude \n
		Snippet: driver.configure.multiEval.limit.qam.evMagnitude.set(value = [PROPERTY_STRUCT_NAME](), qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) , for QAM modulations. \n
			:param structure: for set value, see the help for EvMagnitudeStruct structure arguments.
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')"""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		self._core.io.write_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:EVMagnitude', structure)

	def get(self, qAMmodOrder=repcap.QAMmodOrder.Default) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.multiEval.limit.qam.evMagnitude.get(qAMmodOrder = repcap.QAMmodOrder.Default) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) , for QAM modulations. \n
			:param qAMmodOrder: optional repeated capability selector. Default value: Qam16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments."""
		qAMmodOrder_cmd_val = self._base.get_repcap_cmd_value(qAMmodOrder, repcap.QAMmodOrder)
		return self._core.io.query_struct(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:QAM{qAMmodOrder_cmd_val}:EVMagnitude?', self.__class__.EvMagnitudeStruct())
