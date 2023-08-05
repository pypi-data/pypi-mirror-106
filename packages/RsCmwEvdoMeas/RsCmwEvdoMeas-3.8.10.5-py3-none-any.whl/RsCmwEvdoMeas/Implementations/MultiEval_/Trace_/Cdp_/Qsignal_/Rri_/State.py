from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.ResultStateB]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CDP:QSIGnal:RRI:STATe \n
		Snippet: value: List[enums.ResultStateB] = driver.multiEval.trace.cdp.qsignal.rri.state.fetch() \n
		Return the states of the code domain power (CDP) I-signal and Q-signal bar graphs. For a physical layer subtype 2 or 3
		measurement, the bar graphs contain only RRI results. For a physical layer subtype 0/1 measurement the bar graphs contain
		also pilot results, see method RsCmwEvdoMeas.MultiEval.Trace.Cdp.Qsignal.Pilot.State.fetch. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsig_rri_state: NAV | ACTive | INACtive The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . NAV: No channel available ACTive: Active code channel INACtive: Inactive code channel"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:RRI:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStateB)
