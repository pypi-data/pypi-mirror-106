from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	@property
	def dcarrier(self):
		"""dcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcarrier'):
			from .RfSettings_.Dcarrier import Dcarrier
			self._dcarrier = Dcarrier(self._core, self._base)
		return self._dcarrier

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .RfSettings_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, useCONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:EATTenuation:INPut. \n
			:return: rf_input_ext_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, useCONFigure:WCDMa:SIGN<i>:RFSettings:CARRier<c>:EATTenuation:INPut. \n
			:param rf_input_ext_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. For the combined signal path scenario, useCONFigure:WCDMa:SIGN<i>:RFSettings:MARGin. \n
			:return: user_margin: numeric Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. For the combined signal path scenario, useCONFigure:WCDMa:SIGN<i>:RFSettings:MARGin. \n
			:param user_margin: numeric Range: 0 dB to (55 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WCDMa:SIGN<i>:RFSettings:ENPMode
			- CONFigure:WCDMa:SIGN<i>:RFSettings:ENPower \n
			:return: exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_power: float) -> None:
		"""SCPI: CONFigure:WCDMa:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(exp_nom_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:WCDMa:SIGN<i>:RFSettings:ENPMode
			- CONFigure:WCDMa:SIGN<i>:RFSettings:ENPower \n
			:param exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(exp_nom_power)
		self._core.io.write(f'CONFigure:WCDMa:MEASurement<Instance>:RFSettings:ENPower {param}')

	def clone(self) -> 'RfSettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
