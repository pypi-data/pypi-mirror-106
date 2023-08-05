from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:ACP:CURRent:ABSolute \n
		Snippet: value: List[float] = driver.multiEval.trace.acp.current.absolute.read() \n
		Returns the adjacent channel absolute power measured in dBm at a series of frequencies. The frequencies are determined by
		the offset values defined via the commands method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.lower and method
		RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.upper. All defined offset values are considered (irrespective of their
		activation status) . The current, average and maximum traces can be retrieved. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:ACP:CURRent:ABSolute?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:ACP:CURRent:ABSolute \n
		Snippet: value: List[float] = driver.multiEval.trace.acp.current.absolute.fetch() \n
		Returns the adjacent channel absolute power measured in dBm at a series of frequencies. The frequencies are determined by
		the offset values defined via the commands method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.lower and method
		RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.upper. All defined offset values are considered (irrespective of their
		activation status) . The current, average and maximum traces can be retrieved. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:ACP:CURRent:ABSolute?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:TRACe:ACP:CURRent:ABSolute \n
		Snippet: value: List[float] = driver.multiEval.trace.acp.current.absolute.calculate() \n
		Returns the adjacent channel absolute power measured in dBm at a series of frequencies. The frequencies are determined by
		the offset values defined via the commands method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.lower and method
		RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.upper. All defined offset values are considered (irrespective of their
		activation status) . The current, average and maximum traces can be retrieved. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:TRACe:ACP:CURRent:ABSolute?', suppressed)
		return response
