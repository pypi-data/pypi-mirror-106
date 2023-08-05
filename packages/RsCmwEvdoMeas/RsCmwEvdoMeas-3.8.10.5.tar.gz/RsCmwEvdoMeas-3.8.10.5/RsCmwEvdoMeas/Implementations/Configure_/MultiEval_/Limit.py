from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 30 total commands, 5 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_evm'):
			from .Limit_.Evm import Evm
			self._evm = Evm(self._core, self._base)
		return self._evm

	@property
	def merr(self):
		"""merr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_merr'):
			from .Limit_.Merr import Merr
			self._merr = Merr(self._core, self._base)
		return self._merr

	@property
	def perr(self):
		"""perr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_perr'):
			from .Limit_.Perr import Perr
			self._perr = Perr(self._core, self._base)
		return self._perr

	@property
	def acp(self):
		"""acp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .Limit_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def obw(self):
		"""obw commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_obw'):
			from .Limit_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_offset() \n
		Defines an upper limit for the I/Q origin offset. \n
			:return: iq_offset: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.set_iq_offset(iq_offset = 1.0) \n
		Defines an upper limit for the I/Q origin offset. \n
			:param iq_offset: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:IQOFfset {param}')

	def get_iq_imbalance(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_imbalance() \n
		Defines an upper limit for the I/Q imbalance. \n
			:return: iq_imbalance: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_imbalance(self, iq_imbalance: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: driver.configure.multiEval.limit.set_iq_imbalance(iq_imbalance = 1.0) \n
		Defines an upper limit for the I/Q imbalance. \n
			:param iq_imbalance: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_imbalance)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cf_error() \n
		Defines an upper limit for the carrier frequency error. \n
			:return: cfreq_error: Range: 0 Hz to 1000 Hz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, cfreq_error: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CFERror \n
		Snippet: driver.configure.multiEval.limit.set_cf_error(cfreq_error = 1.0) \n
		Defines an upper limit for the carrier frequency error. \n
			:param cfreq_error: Range: 0 Hz to 1000 Hz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(cfreq_error)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CFERror {param}')

	def get_tt_error(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:TTERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_tt_error() \n
		Defines an upper limit for the transmit time error. \n
			:return: trans_time_err: Range: 0 µs to 10 µs, Unit: µs Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:TTERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_tt_error(self, trans_time_err: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:TTERror \n
		Snippet: driver.configure.multiEval.limit.set_tt_error(trans_time_err = 1.0) \n
		Defines an upper limit for the transmit time error. \n
			:param trans_time_err: Range: 0 µs to 10 µs, Unit: µs Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(trans_time_err)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:TTERror {param}')

	def get_wquality(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:WQUality \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_wquality() \n
		Defines a lower limit for the waveform quality. For an ideal transmitter, the waveform quality equals 1. \n
			:return: wav_quality: Range: 0 to 1 Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:WQUality?')
		return Conversions.str_to_float_or_bool(response)

	def set_wquality(self, wav_quality: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:WQUality \n
		Snippet: driver.configure.multiEval.limit.set_wquality(wav_quality = 1.0) \n
		Defines a lower limit for the waveform quality. For an ideal transmitter, the waveform quality equals 1. \n
			:param wav_quality: Range: 0 to 1 Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(wav_quality)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:WQUality {param}')

	def get_max_power(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MAXPower \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_max_power() \n
		Defines an upper limit for the AT power. \n
			:return: abs_max_power: Range: -127.9 dBm to 0 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MAXPower?')
		return Conversions.str_to_float_or_bool(response)

	def set_max_power(self, abs_max_power: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MAXPower \n
		Snippet: driver.configure.multiEval.limit.set_max_power(abs_max_power = 1.0) \n
		Defines an upper limit for the AT power. \n
			:param abs_max_power: Range: -127.9 dBm to 0 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(abs_max_power)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MAXPower {param}')

	def get_min_power(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MINPower \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_min_power() \n
		Defines a lower limit for the AT power. \n
			:return: abs_min_power: Range: -128 dBm to -0.1 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MINPower?')
		return Conversions.str_to_float_or_bool(response)

	def set_min_power(self, abs_min_power: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MINPower \n
		Snippet: driver.configure.multiEval.limit.set_min_power(abs_min_power = 1.0) \n
		Defines a lower limit for the AT power. \n
			:param abs_min_power: Range: -128 dBm to -0.1 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(abs_min_power)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MINPower {param}')

	def get_cdp(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CDP \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cdp() \n
		Defines an upper limit for the code domain power of inactive channels. \n
			:return: cdp_user_limit: Range: -70 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CDP?')
		return Conversions.str_to_float_or_bool(response)

	def set_cdp(self, cdp_user_limit: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CDP \n
		Snippet: driver.configure.multiEval.limit.set_cdp(cdp_user_limit = 1.0) \n
		Defines an upper limit for the code domain power of inactive channels. \n
			:param cdp_user_limit: Range: -70 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_or_bool_value_to_str(cdp_user_limit)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CDP {param}')

	def get_cde(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CDE \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cde() \n
		Defines an upper limit for the code domain error. \n
			:return: cde_user_limit: Range: -70 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CDE?')
		return Conversions.str_to_float_or_bool(response)

	def set_cde(self, cde_user_limit: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CDE \n
		Snippet: driver.configure.multiEval.limit.set_cde(cde_user_limit = 1.0) \n
		Defines an upper limit for the code domain error. \n
			:param cde_user_limit: Range: -70 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_or_bool_value_to_str(cde_user_limit)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CDE {param}')

	def get_cp(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CP \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cp() \n
		Defines an upper limit for the channel power. \n
			:return: cp_user_limit: Range: -60 dB to 0 dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CP?')
		return Conversions.str_to_float_or_bool(response)

	def set_cp(self, cp_user_limit: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:CP \n
		Snippet: driver.configure.multiEval.limit.set_cp(cp_user_limit = 1.0) \n
		Defines an upper limit for the channel power. \n
			:param cp_user_limit: Range: -60 dB to 0 dB
		"""
		param = Conversions.decimal_or_bool_value_to_str(cp_user_limit)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:CP {param}')

	def get_dwcp(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:DWCP \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_dwcp() \n
		Specifies the data Walsh code channel power limit. \n
			:return: dwcp_user_limit: Range: -60 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:DWCP?')
		return Conversions.str_to_float_or_bool(response)

	def set_dwcp(self, dwcp_user_limit: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:DWCP \n
		Snippet: driver.configure.multiEval.limit.set_dwcp(dwcp_user_limit = 1.0) \n
		Specifies the data Walsh code channel power limit. \n
			:param dwcp_user_limit: Range: -60 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_or_bool_value_to_str(dwcp_user_limit)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:DWCP {param}')

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
