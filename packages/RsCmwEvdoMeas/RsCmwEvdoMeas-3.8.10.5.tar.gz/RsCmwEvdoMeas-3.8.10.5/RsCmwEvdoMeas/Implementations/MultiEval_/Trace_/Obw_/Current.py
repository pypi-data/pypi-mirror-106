from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self, obw=repcap.Obw.Default) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:OBW<Number>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.obw.current.read(obw = repcap.Obw.Default) \n
		For the carrier or carrier group addressed by the <Number> suffix, returns the lower and upper edge of the occupied
		bandwidth (OBW) . For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to
		obtain the OBW results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: curr_obw: No help available"""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:OBW{obw_cmd_val}:CURRent?', suppressed)
		return response

	def fetch(self, obw=repcap.Obw.Default) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:OBW<Number>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.obw.current.fetch(obw = repcap.Obw.Default) \n
		For the carrier or carrier group addressed by the <Number> suffix, returns the lower and upper edge of the occupied
		bandwidth (OBW) . For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to
		obtain the OBW results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: curr_obw: No help available"""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:OBW{obw_cmd_val}:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, obw=repcap.Obw.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:TRACe:OBW<Number>:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.obw.current.calculate(obw = repcap.Obw.Default) \n
		For the carrier or carrier group addressed by the <Number> suffix, returns the lower and upper edge of the occupied
		bandwidth (OBW) . For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to
		obtain the OBW results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: curr_obw: No help available"""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:TRACe:OBW{obw_cmd_val}:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
