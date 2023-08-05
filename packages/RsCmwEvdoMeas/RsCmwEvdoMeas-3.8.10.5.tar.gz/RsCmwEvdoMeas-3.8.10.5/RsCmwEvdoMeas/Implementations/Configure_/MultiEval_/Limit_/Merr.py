from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Merr:
	"""Merr commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("merr", core, parent)

	def get_peak(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MERR:PEAK \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.merr.get_peak() \n
		Defines an upper limit for the peak values of the magnitude error. \n
			:return: merr_peak: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MERR:PEAK?')
		return Conversions.str_to_float_or_bool(response)

	def set_peak(self, merr_peak: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MERR:PEAK \n
		Snippet: driver.configure.multiEval.limit.merr.set_peak(merr_peak = 1.0) \n
		Defines an upper limit for the peak values of the magnitude error. \n
			:param merr_peak: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(merr_peak)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MERR:PEAK {param}')

	def get_rms(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MERR:RMS \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.merr.get_rms() \n
		Defines an upper limit for the RMS values of the magnitude error. \n
			:return: merr_rms: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MERR:RMS?')
		return Conversions.str_to_float_or_bool(response)

	def set_rms(self, merr_rms: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:MERR:RMS \n
		Snippet: driver.configure.multiEval.limit.merr.set_rms(merr_rms = 1.0) \n
		Defines an upper limit for the RMS values of the magnitude error. \n
			:param merr_rms: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(merr_rms)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:MERR:RMS {param}')
