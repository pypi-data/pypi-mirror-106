from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: List[float]: float Occupied bandwidth Range: 0 MHz to 16 MHz (SDEViation 0 MHz to 8 MHz) , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Obw', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Obw: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:OBW:SDEViation \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.obw.standardDev.fetch() \n
		Returns occupied bandwidth (OBW) results in list mode. To define the statistical length for AVERage, MAXimum and to
		enable the calculation of the results, use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.
		set. The ranges indicated below apply to all results except standard deviation results. The minimum for standard
		deviation results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly
		stated. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {.
		..}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:OBW:SDEViation?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: List[enums.ResultStatus2]: float Occupied bandwidth Range: 0 MHz to 16 MHz (SDEViation 0 MHz to 8 MHz) , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Obw', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Obw: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:OBW:SDEViation \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.obw.standardDev.calculate() \n
		Returns occupied bandwidth (OBW) results in list mode. To define the statistical length for AVERage, MAXimum and to
		enable the calculation of the results, use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.
		set. The ranges indicated below apply to all results except standard deviation results. The minimum for standard
		deviation results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly
		stated. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {.
		..}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:OBW:SDEViation?', self.__class__.CalculateStruct())
