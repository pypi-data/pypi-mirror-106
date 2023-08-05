from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Acp: List[float]: No parameter help available
			- Ms_Power_Wide: List[float]: No parameter help available
			- Ms_Power_Narrow: List[float]: No parameter help available
			- Out_Of_Tol_Count: List[float]: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Cur_Stat_Count: List[int]: decimal Number of evaluated valid slots in this segment."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Acp', DataType.FloatList, None, False, True, 41),
			ArgStruct('Ms_Power_Wide', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Narrow', DataType.FloatList, None, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Acp: List[float] = None
			self.Ms_Power_Wide: List[float] = None
			self.Ms_Power_Narrow: List[float] = None
			self.Out_Of_Tol_Count: List[float] = None
			self.Cur_Stat_Count: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:AVERage \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.acp.extended.average.fetch() \n
		Returns all ACP value results in list mode. To define the statistical length for AVERage, MAXimum, MINimum calculation
		and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.
		Spectrum.set. The ranges indicated below apply to all results except standard deviation results. The minimum for standard
		deviation results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly
		stated. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {.
		..}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. For the out of tolerance and code channel filter match
		ratio, results retrieved via the CURRent, AVERage and MAXimum commands are identical. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:AVERage?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Acp: List[float]: No parameter help available
			- Ms_Power_Wide: List[enums.ResultStatus2]: No parameter help available
			- Ms_Power_Narrow: List[enums.ResultStatus2]: No parameter help available
			- Out_Of_Tol_Count: List[enums.ResultStatus2]: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Cur_Stat_Count: List[enums.ResultStatus2]: decimal Number of evaluated valid slots in this segment."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Acp', DataType.FloatList, None, False, True, 41),
			ArgStruct('Ms_Power_Wide', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Ms_Power_Narrow', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Acp: List[float] = None
			self.Ms_Power_Wide: List[enums.ResultStatus2] = None
			self.Ms_Power_Narrow: List[enums.ResultStatus2] = None
			self.Out_Of_Tol_Count: List[enums.ResultStatus2] = None
			self.Cur_Stat_Count: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.acp.extended.average.calculate() \n
		Returns all ACP value results in list mode. To define the statistical length for AVERage, MAXimum, MINimum calculation
		and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.
		Spectrum.set. The ranges indicated below apply to all results except standard deviation results. The minimum for standard
		deviation results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly
		stated. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {.
		..}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. For the out of tolerance and code channel filter match
		ratio, results retrieved via the CURRent, AVERage and MAXimum commands are identical. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:AVERage?', self.__class__.CalculateStruct())
