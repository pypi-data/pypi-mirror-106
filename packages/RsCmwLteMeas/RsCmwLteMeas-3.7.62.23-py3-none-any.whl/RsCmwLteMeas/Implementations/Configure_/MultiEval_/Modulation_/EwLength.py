from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EwLength:
	"""EwLength commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ewLength", core, parent)

	@property
	def channelBw(self):
		"""channelBw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channelBw'):
			from .EwLength_.ChannelBw import ChannelBw
			self._channelBw = ChannelBw(self._core, self._base)
		return self._channelBw

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Length_Cp_Normal: List[int]: No parameter help available
			- Length_Cp_Extended: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Length_Cp_Normal', DataType.IntegerList, None, False, False, 6),
			ArgStruct('Length_Cp_Extended', DataType.IntegerList, None, False, False, 6)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length_Cp_Normal: List[int] = None
			self.Length_Cp_Extended: List[int] = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: value: ValueStruct = driver.configure.multiEval.modulation.ewLength.get_value() \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the cyclic prefix (CP) type. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:MODulation:EWLength?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: driver.configure.multiEval.modulation.ewLength.set_value(value = ValueStruct()) \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the cyclic prefix (CP) type. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:LTE:MEASurement<Instance>:MEValuation:MODulation:EWLength', value)

	def clone(self) -> 'EwLength':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EwLength(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
