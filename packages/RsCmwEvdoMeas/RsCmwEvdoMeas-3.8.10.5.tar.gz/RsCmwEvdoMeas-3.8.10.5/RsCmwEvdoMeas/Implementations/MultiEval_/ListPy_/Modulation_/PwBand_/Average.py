from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:MODulation:PWBand:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.pwBand.average.fetch() \n
		Returns AT narrowband and wideband power (statistical) values for all active list mode segments. The narrowband filter is
		1.23 MHz, the wideband filter is 8 MHz wide. The values described below are returned by FETCh commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: ms_power_wideband: float Comma-separated list of values, one per active segment. Range: -100 dBm to 50 dBm , Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:MODulation:PWBand:AVERage?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:MODulation:PWBand:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.pwBand.average.calculate() \n
		Returns AT narrowband and wideband power (statistical) values for all active list mode segments. The narrowband filter is
		1.23 MHz, the wideband filter is 8 MHz wide. The values described below are returned by FETCh commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: ms_power_wideband: float Comma-separated list of values, one per active segment. Range: -100 dBm to 50 dBm , Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:MODulation:PWBand:AVERage?', suppressed)
		return response
