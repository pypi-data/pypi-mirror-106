from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.ResultStateA]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:CP:RRI:STATe \n
		Snippet: value: List[enums.ResultStateA] = driver.multiEval.listPy.cp.rri.state.fetch() \n
		Returns the state of a particular reverse link channel (ACK/DSC, auxiliary pilot, data, DRC, PILOT, RRI) in the channel
		power measurement for all active segments. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: rri: INVisible | ACTive | IACTive Comma-separated list of values, one per active segment."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:RRI:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStateA)
