from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	def get_setting(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:SETTing \n
		Snippet: value: int = driver.configure.multiEval.carrier.get_setting() \n
			INTRO_CMD_HELP: Selects a carrier for the following carrier settings: \n
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.enable
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.foffset
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.frequency
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:CARRier:SETTing or
			- CONFigure:EVDO:SIGN<i>:PILot:SETTing \n
			:return: set_carrier: numeric Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:SETTing?')
		return Conversions.str_to_int(response)

	def set_setting(self, set_carrier: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:SETTing \n
		Snippet: driver.configure.multiEval.carrier.set_setting(set_carrier = 1) \n
			INTRO_CMD_HELP: Selects a carrier for the following carrier settings: \n
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.enable
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.foffset
			- method RsCmwEvdoMeas.Configure.MultiEval.Carrier.frequency
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:CARRier:SETTing or
			- CONFigure:EVDO:SIGN<i>:PILot:SETTing \n
			:param set_carrier: numeric Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(set_carrier)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:SETTing {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:ENABle \n
		Snippet: value: bool = driver.configure.multiEval.carrier.get_enable() \n
		Defines whether a carrier is measured (ON) or not (OFF) . The related carrier has to be pre-set using the method
		RsCmwEvdoMeas.Configure.MultiEval.Carrier.setting command. All carriers can be queried, but carrier 0 cannot be set (fix
		set to ON) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:NETWork:PILot:AN:ACTive
			- CONFigure:EVDO:SIGN<i>:NETWork:PILot:AT:ASSigned \n
			:return: cenable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, cenable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:ENABle \n
		Snippet: driver.configure.multiEval.carrier.set_enable(cenable = False) \n
		Defines whether a carrier is measured (ON) or not (OFF) . The related carrier has to be pre-set using the method
		RsCmwEvdoMeas.Configure.MultiEval.Carrier.setting command. All carriers can be queried, but carrier 0 cannot be set (fix
		set to ON) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:NETWork:PILot:AN:ACTive
			- CONFigure:EVDO:SIGN<i>:NETWork:PILot:AT:ASSigned \n
			:param cenable: OFF | ON
		"""
		param = Conversions.bool_to_str(cenable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:ENABle {param}')

	def get_select(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:SELect \n
		Snippet: value: int = driver.configure.multiEval.carrier.get_select() \n
			INTRO_CMD_HELP: Defines the selected carrier, also displayed at the GUI. The GUI displays the results for this carrier (if the carrier is enabled) . Results retrieved via remote command and the following remote commands are also related to this carrier: \n
			- method RsCmwEvdoMeas.Configure.MultiEval.drc
			- method RsCmwEvdoMeas.Configure.MultiEval.data
			- method RsCmwEvdoMeas.Configure.MultiEval.apilot
			- method RsCmwEvdoMeas.Configure.MultiEval.ackDsc
			- method RsCmwEvdoMeas.Configure.MultiEval.dmodulation
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.upper
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Foffsets.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Foffsets.upper
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP:EXTended
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP:EXTended
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Rbw.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Rbw.upper
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Rbw.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Rbw.upper \n
			:return: selected_carrier: integer Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:SELect?')
		return Conversions.str_to_int(response)

	def set_select(self, selected_carrier: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:SELect \n
		Snippet: driver.configure.multiEval.carrier.set_select(selected_carrier = 1) \n
			INTRO_CMD_HELP: Defines the selected carrier, also displayed at the GUI. The GUI displays the results for this carrier (if the carrier is enabled) . Results retrieved via remote command and the following remote commands are also related to this carrier: \n
			- method RsCmwEvdoMeas.Configure.MultiEval.drc
			- method RsCmwEvdoMeas.Configure.MultiEval.data
			- method RsCmwEvdoMeas.Configure.MultiEval.apilot
			- method RsCmwEvdoMeas.Configure.MultiEval.ackDsc
			- method RsCmwEvdoMeas.Configure.MultiEval.dmodulation
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.upper
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Foffsets.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Foffsets.upper
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP:EXTended
			- CONFigure:EVDO:MEAS<i>:MEValuation:LIMit:ACP:EXTended
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Rbw.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Rbw.upper
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Rbw.lower
			- method RsCmwEvdoMeas.Configure.MultiEval.Acp.Extended.Rbw.upper \n
			:param selected_carrier: integer Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(selected_carrier)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:SELect {param}')

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:FOFFset \n
		Snippet: value: float = driver.configure.multiEval.carrier.get_foffset() \n
		Gets/sets the frequency offset of a selected carrier relative to carrier 0. The related carrier has to be pre-set using
		the method RsCmwEvdoMeas.Configure.MultiEval.Carrier.setting command. All carriers can be queried, but carrier 0 cannot
		be set. This command is relevant only for standalone mode. While the combined signal path scenario is active, the command
		for carrier frequency offset is not used. \n
			:return: cf_offset: numeric The offset relative to carrier 0. The maximum distance between carriers is restricted to 8 MHz. Range: - 8 MHz to + 8 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, cf_offset: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:FOFFset \n
		Snippet: driver.configure.multiEval.carrier.set_foffset(cf_offset = 1.0) \n
		Gets/sets the frequency offset of a selected carrier relative to carrier 0. The related carrier has to be pre-set using
		the method RsCmwEvdoMeas.Configure.MultiEval.Carrier.setting command. All carriers can be queried, but carrier 0 cannot
		be set. This command is relevant only for standalone mode. While the combined signal path scenario is active, the command
		for carrier frequency offset is not used. \n
			:param cf_offset: numeric The offset relative to carrier 0. The maximum distance between carriers is restricted to 8 MHz. Range: - 8 MHz to + 8 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(cf_offset)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:FOFFset {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:FREQuency \n
		Snippet: value: float = driver.configure.multiEval.carrier.get_frequency() \n
		Gets/sets the frequency of a selected carrier. The related carrier has to be pre-set using the method RsCmwEvdoMeas.
		Configure.MultiEval.Carrier.setting command. All carriers can be queried, but only carrier 0 can be set. The frequencies
		of the other carriers are set implicitly via method RsCmwEvdoMeas.Configure.MultiEval.Carrier.foffset.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:CARRier:CHANnel or
			- CONFigure:EVDO:SIGN<i>:CARRier:RLFRequency
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:return: cfrequency: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, cfrequency: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:FREQuency \n
		Snippet: driver.configure.multiEval.carrier.set_frequency(cfrequency = 1.0) \n
		Gets/sets the frequency of a selected carrier. The related carrier has to be pre-set using the method RsCmwEvdoMeas.
		Configure.MultiEval.Carrier.setting command. All carriers can be queried, but only carrier 0 can be set. The frequencies
		of the other carriers are set implicitly via method RsCmwEvdoMeas.Configure.MultiEval.Carrier.foffset.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:EVDO:SIGN<i>:CARRier:CHANnel or
			- CONFigure:EVDO:SIGN<i>:CARRier:RLFRequency
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param cfrequency: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(cfrequency)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_wb_filter(self) -> enums.WbFilter:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:WBFilter \n
		Snippet: value: enums.WbFilter = driver.configure.multiEval.carrier.get_wb_filter() \n
		Selects the bandwidth of the wideband filter, used to measure the 'AT Power (wideband) ' of a single-carrier
		configuration. For a multi-carrier configuration, the bandwidth can only be queried (equals 16 MHz) . \n
			:return: wb_filter: F8M0 | F16M0 F8M0: 8 MHz filter bandwidth F16M0: 16 MHz filter bandwidth
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:WBFilter?')
		return Conversions.str_to_scalar_enum(response, enums.WbFilter)

	def set_wb_filter(self, wb_filter: enums.WbFilter) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:CARRier:WBFilter \n
		Snippet: driver.configure.multiEval.carrier.set_wb_filter(wb_filter = enums.WbFilter.F16M0) \n
		Selects the bandwidth of the wideband filter, used to measure the 'AT Power (wideband) ' of a single-carrier
		configuration. For a multi-carrier configuration, the bandwidth can only be queried (equals 16 MHz) . \n
			:param wb_filter: F8M0 | F16M0 F8M0: 8 MHz filter bandwidth F16M0: 16 MHz filter bandwidth
		"""
		param = Conversions.enum_scalar_to_str(wb_filter, enums.WbFilter)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:CARRier:WBFilter {param}')
