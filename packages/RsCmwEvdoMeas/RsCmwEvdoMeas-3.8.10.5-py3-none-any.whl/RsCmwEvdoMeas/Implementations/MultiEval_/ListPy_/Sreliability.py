from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sreliability:
	"""Sreliability commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sreliability", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SRELiability \n
		Snippet: value: List[int] = driver.multiEval.listPy.sreliability.fetch() \n
		Returns the segment reliabilities for all active list mode segments. A common reliability indicator of zero indicates
		that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of
		the measured segments. If you get a non-zero common reliability indicator, you can use this command to retrieve the
		individual reliability values of all measured segments for further analysis. The values described below are returned by
		FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: seg_reliability: decimal Comma-separated list of values, one per active segment. The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SRELiability?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SRELiability \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.listPy.sreliability.calculate() \n
		Returns the segment reliabilities for all active list mode segments. A common reliability indicator of zero indicates
		that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of
		the measured segments. If you get a non-zero common reliability indicator, you can use this command to retrieve the
		individual reliability values of all measured segments for further analysis. The values described below are returned by
		FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: seg_reliability: decimal Comma-separated list of values, one per active segment. The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SRELiability?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
