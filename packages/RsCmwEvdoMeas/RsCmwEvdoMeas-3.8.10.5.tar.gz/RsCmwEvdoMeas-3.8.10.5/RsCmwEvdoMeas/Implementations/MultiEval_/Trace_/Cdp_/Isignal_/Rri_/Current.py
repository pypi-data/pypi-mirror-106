from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.cdp.isignal.rri.current.read() \n
		Return values of the code domain power (CDP) I-Signal and Q-Signal bar graphs. The results of the current, average,
		maximum and minimum bar graphs can be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain
		only RRI results. For a physical layer subtype 0/1 measurement the bar graphs contain also pilot results, see method
		RsCmwEvdoMeas.MultiEval.Trace.Cdp.Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and
		READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: isig_rri_curr_cdp: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: - 70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.cdp.isignal.rri.current.fetch() \n
		Return values of the code domain power (CDP) I-Signal and Q-Signal bar graphs. The results of the current, average,
		maximum and minimum bar graphs can be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain
		only RRI results. For a physical layer subtype 0/1 measurement the bar graphs contain also pilot results, see method
		RsCmwEvdoMeas.MultiEval.Trace.Cdp.Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and
		READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: isig_rri_curr_cdp: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: - 70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.cdp.isignal.rri.current.calculate() \n
		Return values of the code domain power (CDP) I-Signal and Q-Signal bar graphs. The results of the current, average,
		maximum and minimum bar graphs can be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain
		only RRI results. For a physical layer subtype 0/1 measurement the bar graphs contain also pilot results, see method
		RsCmwEvdoMeas.MultiEval.Trace.Cdp.Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and
		READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: isig_rri_curr_cdp: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: - 70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDP:ISIGnal:RRI:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
