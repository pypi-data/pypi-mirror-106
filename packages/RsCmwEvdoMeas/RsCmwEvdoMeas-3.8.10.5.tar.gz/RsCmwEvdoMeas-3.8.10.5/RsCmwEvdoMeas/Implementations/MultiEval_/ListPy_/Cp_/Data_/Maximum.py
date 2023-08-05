from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:CP:DATA:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.cp.data.maximum.fetch() \n
		Returns the RMS power (statistical values) of the data channel for all active list mode segments. The values described
		below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: data: float Comma-separated list of values, one per active segment. Range: -60 dB to +10 dB , Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:DATA:MAXimum?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:CP:DATA:MAXimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.listPy.cp.data.maximum.calculate() \n
		Returns the RMS power (statistical values) of the data channel for all active list mode segments. The values described
		below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: data: float Comma-separated list of values, one per active segment. Range: -60 dB to +10 dB , Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:DATA:MAXimum?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
