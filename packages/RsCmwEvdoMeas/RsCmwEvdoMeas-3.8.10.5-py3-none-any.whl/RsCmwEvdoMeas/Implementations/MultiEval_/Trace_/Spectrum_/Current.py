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
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:SPECtrum:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.spectrum.current.read() \n
		Returns the power spectrum traces across the frequency span (8 MHz or 16 MHz for single-carrier configurations, 16 MHz
		for multi-carrier configurations; see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.wbFilter) . \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_spectrum: float Frequency-dependent power values. Each of the traces contains 1667 values. Range: -100 dB to +57 dB , Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:SPECtrum:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:SPECtrum:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.spectrum.current.fetch() \n
		Returns the power spectrum traces across the frequency span (8 MHz or 16 MHz for single-carrier configurations, 16 MHz
		for multi-carrier configurations; see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.wbFilter) . \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_spectrum: float Frequency-dependent power values. Each of the traces contains 1667 values. Range: -100 dB to +57 dB , Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:SPECtrum:CURRent?', suppressed)
		return response
