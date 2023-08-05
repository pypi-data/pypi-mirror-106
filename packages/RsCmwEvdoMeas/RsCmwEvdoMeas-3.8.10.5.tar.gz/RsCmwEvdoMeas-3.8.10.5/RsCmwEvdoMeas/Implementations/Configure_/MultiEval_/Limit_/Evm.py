from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evm", core, parent)

	def get_peak(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:EVM:PEAK \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.evm.get_peak() \n
		Defines an upper limit for the peak values of the error vector magnitude (EVM) . \n
			:return: evm_peak: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:EVM:PEAK?')
		return Conversions.str_to_float_or_bool(response)

	def set_peak(self, evm_peak: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:EVM:PEAK \n
		Snippet: driver.configure.multiEval.limit.evm.set_peak(evm_peak = 1.0) \n
		Defines an upper limit for the peak values of the error vector magnitude (EVM) . \n
			:param evm_peak: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_peak)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:EVM:PEAK {param}')

	def get_rms(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:EVM:RMS \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.evm.get_rms() \n
		Defines an upper limit for the RMS values of the error vector magnitude (EVM) . \n
			:return: evm_rms: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:EVM:RMS?')
		return Conversions.str_to_float_or_bool(response)

	def set_rms(self, evm_rms: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:EVM:RMS \n
		Snippet: driver.configure.multiEval.limit.evm.set_rms(evm_rms = 1.0) \n
		Defines an upper limit for the RMS values of the error vector magnitude (EVM) . \n
			:param evm_rms: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(evm_rms)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:EVM:RMS {param}')
