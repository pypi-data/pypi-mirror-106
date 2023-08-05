from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcSpacing:
	"""AcSpacing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acSpacing", core, parent)

	def set(self, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.multiEval.listPy.segment.carrierAggregation.acSpacing.set(segment = repcap.Segment.Default) \n
		Adjusts the component carrier frequencies in segment <no>, so that the carriers are aggregated contiguously. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CAGGregation:ACSPacing')

	def set_with_opc(self, segment=repcap.Segment.Default) -> None:
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.multiEval.listPy.segment.carrierAggregation.acSpacing.set_with_opc(segment = repcap.Segment.Default) \n
		Adjusts the component carrier frequencies in segment <no>, so that the carriers are aggregated contiguously. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteMeas.utilities.opc_timeout_set() to set the timeout value. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		self._core.io.write_with_opc(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CAGGregation:ACSPacing')
