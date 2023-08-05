from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:CP:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.cp.maximum.read() \n
		Returns the scalar channel power for the data channel. The result is extended to the W24 and W12 I/Q values of the data
		channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is returned. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: data: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:CP:MAXimum?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:CP:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.cp.maximum.fetch() \n
		Returns the scalar channel power for the data channel. The result is extended to the W24 and W12 I/Q values of the data
		channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is returned. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: data: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:CP:MAXimum?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:CP:MAXimum \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.cp.maximum.calculate() \n
		Returns the scalar channel power for the data channel. The result is extended to the W24 and W12 I/Q values of the data
		channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is returned. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: data: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:CP:MAXimum?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
