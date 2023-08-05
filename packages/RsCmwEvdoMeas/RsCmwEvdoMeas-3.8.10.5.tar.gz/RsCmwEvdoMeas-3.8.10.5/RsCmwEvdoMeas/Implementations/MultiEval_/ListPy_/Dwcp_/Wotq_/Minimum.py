from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: No parameter help available
			- W_12_Q: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('W_12_Q', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.W_12_Q: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:DWCP:WOTQ:MINimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.dwcp.wotq.minimum.fetch() \n
		Returns the scalar channel power for the data channel results for all active list mode segments. WOT represents W12
		(Walsh code one-two) and WTF represents W24 (Walsh code two-four) . The values described below are returned by FETCh
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:DWCP:WOTQ:MINimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: No parameter help available
			- W_12_Q: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('W_12_Q', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.W_12_Q: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:DWCP:WOTQ:MINimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.dwcp.wotq.minimum.calculate() \n
		Returns the scalar channel power for the data channel results for all active list mode segments. WOT represents W12
		(Walsh code one-two) and WTF represents W24 (Walsh code two-four) . The values described below are returned by FETCh
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:DWCP:WOTQ:MINimum?', self.__class__.CalculateStruct())
