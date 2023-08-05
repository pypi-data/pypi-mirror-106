from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.cde.qsignal.rri.average.read() \n
		Return values of the code domain error (CDE) I-Signal and Q-Signal bar graphs. Current, average and maximum results can
		be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain only RRI results. For a physical
		layer subtype 0/1 measurement the bar graphs contain also pilot results, see method RsCmwEvdoMeas.MultiEval.Trace.Cde.
		Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsig_rri_aver_cde: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.cde.qsignal.rri.average.fetch() \n
		Return values of the code domain error (CDE) I-Signal and Q-Signal bar graphs. Current, average and maximum results can
		be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain only RRI results. For a physical
		layer subtype 0/1 measurement the bar graphs contain also pilot results, see method RsCmwEvdoMeas.MultiEval.Trace.Cde.
		Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsig_rri_aver_cde: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.cde.qsignal.rri.average.calculate() \n
		Return values of the code domain error (CDE) I-Signal and Q-Signal bar graphs. Current, average and maximum results can
		be retrieved. For a physical layer subtype 2 or 3 measurement, the bar graphs contain only RRI results. For a physical
		layer subtype 0/1 measurement the bar graphs contain also pilot results, see method RsCmwEvdoMeas.MultiEval.Trace.Cde.
		Isignal.Pilot.Current.fetch etc. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsig_rri_aver_cde: float The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDE:QSIGnal:RRI:AVERage?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
