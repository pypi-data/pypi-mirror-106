from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- SOURce:EVDO:SIGN<i>:RFSettings:RX:EATTenuation
			- CONFigure:EVDO:SIGN<i>:RFSettings:EATTenuation \n
			:return: rf_input_ext_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rf_input_ext_att: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(rf_input_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- SOURce:EVDO:SIGN<i>:RFSettings:RX:EATTenuation
			- CONFigure:EVDO:SIGN<i>:RFSettings:EATTenuation \n
			:param rf_input_ext_att: numeric Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(rf_input_ext_att)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. \n
			:return: user_margin: numeric Range: 0 dB to (55 dB + External Attenuation - Expected Nominal Power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the measurement adds to the expected nominal power to determine the reference power. The reference
		power minus the external input attenuation must be within the power range of the selected input connector. Refer to the
		data sheet. \n
			:param user_margin: numeric Range: 0 dB to (55 dB + External Attenuation - Expected Nominal Power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:RFPower:EPMode
			- CONFigure:EVDO:SIGN<i>:RFPower:MANual
			- CONFigure:EVDO:SIGN<i>:RFPower:EXPected \n
			:return: exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nom_power: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(exp_nom_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:RFPower:EPMode
			- CONFigure:EVDO:SIGN<i>:RFPower:MANual
			- CONFigure:EVDO:SIGN<i>:RFPower:EXPected \n
			:param exp_nom_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(exp_nom_power)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.get_frequency() \n
		Selects the center frequency of the RF analyzer. If the center frequency is valid for the current band class, the
		corresponding channel number is also calculated and set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:RFSettings:FREQuency
			- CONFigure:EVDO:SIGN<i>:RFSettings:RLFRequency or
			- CONFigure:EVDO:SIGN<i>:RFSettings:CHANnel
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:return: frequency: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.rfSettings.set_frequency(frequency = 1.0) \n
		Selects the center frequency of the RF analyzer. If the center frequency is valid for the current band class, the
		corresponding channel number is also calculated and set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:RFSettings:FREQuency
			- CONFigure:EVDO:SIGN<i>:RFSettings:RLFRequency or
			- CONFigure:EVDO:SIGN<i>:RFSettings:CHANnel
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param frequency: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:CHANnel \n
		Snippet: value: int = driver.configure.rfSettings.get_channel() \n
		Selects the channel number. The channel number must be valid for the current band class, for dependencies see 'Band
		Classes'. The corresponding center frequency (method RsCmwEvdoMeas.Configure.RfSettings.frequency) is calculated and set.
		For the combined signal path scenario, useCONFigure:EVDO:SIGN<i>:RFSettings:CHANnel. \n
			:return: channel: integer Range: depends on selected band class
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:CHANnel \n
		Snippet: driver.configure.rfSettings.set_channel(channel = 1) \n
		Selects the channel number. The channel number must be valid for the current band class, for dependencies see 'Band
		Classes'. The corresponding center frequency (method RsCmwEvdoMeas.Configure.RfSettings.frequency) is calculated and set.
		For the combined signal path scenario, useCONFigure:EVDO:SIGN<i>:RFSettings:CHANnel. \n
			:param channel: integer Range: depends on selected band class
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:CHANnel {param}')

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:FOFFset \n
		Snippet: value: float = driver.configure.rfSettings.get_foffset() \n
		Selects a positive or negative offset frequency to be added to the center frequency (method RsCmwEvdoMeas.Configure.
		RfSettings.frequency) . For the combined signal path scenario, useCONFigure:EVDO:SIGN<i>:RFSettings:FOFFset. \n
			:return: freq_offset: numeric Range: -50 kHz to 50 kHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, freq_offset: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.rfSettings.set_foffset(freq_offset = 1.0) \n
		Selects a positive or negative offset frequency to be added to the center frequency (method RsCmwEvdoMeas.Configure.
		RfSettings.frequency) . For the combined signal path scenario, useCONFigure:EVDO:SIGN<i>:RFSettings:FOFFset. \n
			:param freq_offset: numeric Range: -50 kHz to 50 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq_offset)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:FOFFset {param}')

	# noinspection PyTypeChecker
	def get_bclass(self) -> enums.BandClass:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:BCLass \n
		Snippet: value: enums.BandClass = driver.configure.rfSettings.get_bclass() \n
		Selects the band class (BC) . If the current center frequency (method RsCmwEvdoMeas.Configure.RfSettings.frequency) is
		valid for this band class, the corresponding channel number (method RsCmwEvdoMeas.Configure.RfSettings.channel) is also
		calculated and set. See also 'Band Classes' For the combined signal path scenario,
		useCONFigure:EVDO:SIGN<i>:RFSettings:BCLass. \n
			:return: band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:RFSettings:BCLass?')
		return Conversions.str_to_scalar_enum(response, enums.BandClass)

	def set_bclass(self, band_class: enums.BandClass) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:RFSettings:BCLass \n
		Snippet: driver.configure.rfSettings.set_bclass(band_class = enums.BandClass.AWS) \n
		Selects the band class (BC) . If the current center frequency (method RsCmwEvdoMeas.Configure.RfSettings.frequency) is
		valid for this band class, the corresponding channel number (method RsCmwEvdoMeas.Configure.RfSettings.channel) is also
		calculated and set. See also 'Band Classes' For the combined signal path scenario,
		useCONFigure:EVDO:SIGN<i>:RFSettings:BCLass. \n
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		param = Conversions.enum_scalar_to_str(band_class, enums.BandClass)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:RFSettings:BCLass {param}')
