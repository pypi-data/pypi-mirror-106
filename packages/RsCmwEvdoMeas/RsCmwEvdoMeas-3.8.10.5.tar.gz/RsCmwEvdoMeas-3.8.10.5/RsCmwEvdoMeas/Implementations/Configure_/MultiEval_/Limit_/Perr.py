from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perr:
	"""Perr commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("perr", core, parent)

	def get_peak(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:PERR:PEAK \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.perr.get_peak() \n
		Defines a symmetric limit for the peak values of the phase error. The limit check fails if the absolute value of the
		measured phase error exceeds the specified value. \n
			:return: perr_peak: Range: 0 deg to 180 deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:PERR:PEAK?')
		return Conversions.str_to_float_or_bool(response)

	def set_peak(self, perr_peak: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:PERR:PEAK \n
		Snippet: driver.configure.multiEval.limit.perr.set_peak(perr_peak = 1.0) \n
		Defines a symmetric limit for the peak values of the phase error. The limit check fails if the absolute value of the
		measured phase error exceeds the specified value. \n
			:param perr_peak: Range: 0 deg to 180 deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(perr_peak)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:PERR:PEAK {param}')

	def get_rms(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:PERR:RMS \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.perr.get_rms() \n
		Defines a symmetric limit for the RMS values of the phase error. The limit check fails if the absolute value of the
		measured phase error exceeds the specified value. \n
			:return: perr_rms: Range: 0 deg to 180 deg, Unit: deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:PERR:RMS?')
		return Conversions.str_to_float_or_bool(response)

	def set_rms(self, perr_rms: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:PERR:RMS \n
		Snippet: driver.configure.multiEval.limit.perr.set_rms(perr_rms = 1.0) \n
		Defines a symmetric limit for the RMS values of the phase error. The limit check fails if the absolute value of the
		measured phase error exceeds the specified value. \n
			:param perr_rms: Range: 0 deg to 180 deg, Unit: deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(perr_rms)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:PERR:RMS {param}')
