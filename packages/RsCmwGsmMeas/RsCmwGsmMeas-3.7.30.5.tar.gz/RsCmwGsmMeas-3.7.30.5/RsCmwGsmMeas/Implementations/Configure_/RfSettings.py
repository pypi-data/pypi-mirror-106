from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:RFSettings:EATTenuation:INPut. \n
			:return: external_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, external_att: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(external_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:RFSettings:EATTenuation:INPut. \n
			:param external_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(external_att)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:RFSettings:UMARgin. \n
			:return: user_margin: numeric Range: 0 dB to (55 dB + External Attenuation - Expected Nominal Power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:RFSettings:UMARgin. \n
			:param user_margin: numeric Range: 0 dB to (55 dB + External Attenuation - Expected Nominal Power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:ENPMode
			- CONFigure:GSM:SIGN<i>:RFSettings:ENPower \n
			:return: exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_power: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(exp_nom_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:ENPMode
			- CONFigure:GSM:SIGN<i>:RFSettings:ENPower \n
			:param exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(exp_nom_power)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.get_frequency() \n
		Selects the center frequency of the RF analyzer. If the center frequency is valid for the current frequency band, the
		corresponding channel number is also calculated and set.
			INTRO_CMD_HELP: See also: \n
			- 'GSM Frequency Bands and Channels'
			- method RsCmwGsmMeas.Configure.band
			- method RsCmwGsmMeas.Configure.channel
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:ENABle
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:MAIO
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:HSN
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:SEQuence
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:return: frequency: numeric Range: 70 MHz to 6 GHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.rfSettings.set_frequency(frequency = 1.0) \n
		Selects the center frequency of the RF analyzer. If the center frequency is valid for the current frequency band, the
		corresponding channel number is also calculated and set.
			INTRO_CMD_HELP: See also: \n
			- 'GSM Frequency Bands and Channels'
			- method RsCmwGsmMeas.Configure.band
			- method RsCmwGsmMeas.Configure.channel
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:ENABle
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:MAIO
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:HSN
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:SEQuence
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param frequency: numeric Range: 70 MHz to 6 GHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_foffset(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: value: int = driver.configure.rfSettings.get_foffset() \n
		Specifies a positive or negative frequency offset to be added to the center frequency of the configured channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:FOFFset:UL
			- CONFigure:GSM:SIGN<i>:CONNection:RFOFfset \n
			:return: offset: numeric Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:GSM:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_int(response)

	def set_foffset(self, offset: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.rfSettings.set_foffset(offset = 1) \n
		Specifies a positive or negative frequency offset to be added to the center frequency of the configured channel.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:FOFFset:UL
			- CONFigure:GSM:SIGN<i>:CONNection:RFOFfset \n
			:param offset: numeric Range: -100000 Hz to 100000 Hz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:FOFFset {param}')

	def get_ml_offset(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: value: float = driver.configure.rfSettings.get_ml_offset() \n
		Varies the input level of the mixer in the analyzer path. For the combined signal path scenario,
		useCONFigure:GSM:SIGN<i>:RFSettings:MLOFfset. \n
			:return: mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:RFSettings:MLOFfset?')
		return Conversions.str_to_float(response)

	def set_ml_offset(self, mix_lev_offset: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:RFSettings:MLOFfset \n
		Snippet: driver.configure.rfSettings.set_ml_offset(mix_lev_offset = 1.0) \n
		Varies the input level of the mixer in the analyzer path. For the combined signal path scenario,
		useCONFigure:GSM:SIGN<i>:RFSettings:MLOFfset. \n
			:param mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:RFSettings:MLOFfset {param}')
