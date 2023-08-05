from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:MODulation:TERRor:SDEViation \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.terror.standardDev.fetch() \n
		Returns transmit time error (statistical) values for all active list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: trans_time_error: float Comma-separated list of values, one per active segment. Range: -100 µs to 100 µs, Unit: µs"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:MODulation:TERRor:SDEViation?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:MODulation:TERRor:SDEViation \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.terror.standardDev.calculate() \n
		Returns transmit time error (statistical) values for all active list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: trans_time_error: float Comma-separated list of values, one per active segment. Range: -100 µs to 100 µs, Unit: µs"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:MODulation:TERRor:SDEViation?', suppressed)
		return response
