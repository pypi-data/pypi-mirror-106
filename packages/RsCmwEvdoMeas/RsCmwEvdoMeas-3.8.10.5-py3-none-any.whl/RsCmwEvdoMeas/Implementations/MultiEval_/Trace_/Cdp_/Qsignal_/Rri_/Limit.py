from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CDP:QSIGnal:RRI:LIMit \n
		Snippet: value: List[float] = driver.multiEval.trace.cdp.qsignal.rri.limit.fetch() \n
		Return limit check results for the code domain power (CDP) I-signal and Q-signal bar graphs. For a physical layer subtype
		2 or 3 measurement, the bar graphs contain only RRI results. For a physical layer subtype 0/1 measurement the bar graphs
		contain also pilot results, see method RsCmwEvdoMeas.MultiEval.Trace.Cdp.Qsignal.Pilot.Limit.fetch. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qsig_rri_limit: float Return the exceeded limits as float values. The number of results depends on the physical layer subtype (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3. Range: -70 dB to 0 dB , Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:RRI:LIMit?', suppressed)
		return response
