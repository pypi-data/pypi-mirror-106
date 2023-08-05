from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def pcc(self):
		"""pcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcc'):
			from .RfSettings_.Pcc import Pcc
			self._pcc = Pcc(self._core, self._base)
		return self._pcc

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .RfSettings_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF input connector.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:EATTenuation:INPut
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:EATTenuation:INPut \n
			:return: rf_input_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF input connector.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:EATTenuation:INPut
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:EATTenuation:INPut \n
			:param rf_input_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine its reference power. The reference power
		minus the external input attenuation must be within the power range of the selected input connector; refer to the data
		sheet.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:UMARgin
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:UMARgin \n
			:return: user_margin: Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine its reference power. The reference power
		minus the external input attenuation must be within the power range of the selected input connector; refer to the data
		sheet.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:UMARgin
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:UMARgin \n
			:param user_margin: Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:ENPMode
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:ENPMode
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:ENPower \n
			:return: exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_pow: float) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(exp_nom_pow = 1.0) \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:ENPMode
			- CONFigure:LTE:SIGN<i>:ENPower
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:ENPMode
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:ENPower \n
			:param exp_nom_pow: The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(exp_nom_pow)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: value: int = driver.configure.rfSettings.get_foffset() \n
		Specifies a positive or negative frequency offset to be added to the carrier center frequency (method RsCmwLteMeas.
		Configure.RfSettings.Cc.Frequency.set) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:FOFFset:UL
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:FOFFset:UL
			- CONFigure:LTE:SIGN<i>:FOFFset:UL:UCSPecific \n
			:return: offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, offset: int) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.rfSettings.set_foffset(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the carrier center frequency (method RsCmwLteMeas.
		Configure.RfSettings.Cc.Frequency.set) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:FOFFset:UL
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:FOFFset:UL
			- CONFigure:LTE:SIGN<i>:FOFFset:UL:UCSPecific \n
			:param offset: Range: -100 kHz to 100 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:LTE:MEASurement<Instance>:RFSettings:FOFFset {param}')

	def get_ml_offset(self) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: value: float = driver.configure.rfSettings.get_ml_offset() \n
		Varies the input level of the mixer in the analyzer path.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:MLOFfset
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:MLOFfset \n
			:return: mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:MEASurement<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_float(response)

	def set_ml_offset(self, mix_lev_offset: float) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.rfSettings.set_ml_offset(mix_lev_offset = 1.0) \n
		Varies the input level of the mixer in the analyzer path.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:LTE:SIGN<i>:MLOFfset
			- CONFigure:LTE:SIGN<i>:RFSettings:SCC<c>:MLOFfset \n
			:param mix_lev_offset: Range: -10 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:RFSettings:MLOFfset {param}')

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
