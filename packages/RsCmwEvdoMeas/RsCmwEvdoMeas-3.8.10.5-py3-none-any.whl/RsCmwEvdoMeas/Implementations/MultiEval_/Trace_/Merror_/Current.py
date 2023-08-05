from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:MERRor:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.current.read() \n
		Returns the values of the RMS magnitude error traces. A trace covers a time interval of 833 μs (one half-slot) and
		contains one value per chip. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_merr: float Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:MERRor:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.current.fetch() \n
		Returns the values of the RMS magnitude error traces. A trace covers a time interval of 833 μs (one half-slot) and
		contains one value per chip. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_merr: float Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent?', suppressed)
		return response
