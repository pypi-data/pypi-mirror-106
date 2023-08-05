from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Current_Acp: List[float]: No parameter help available
			- Ms_Power_Wide: float: No parameter help available
			- Ms_Power_Narrow: float: No parameter help available
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Cur_Stat_Count: int: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct('Current_Acp', DataType.FloatList, None, False, False, 21),
			ArgStruct.scalar_float('Ms_Power_Wide'),
			ArgStruct.scalar_float('Ms_Power_Narrow'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_int('Cur_Stat_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Current_Acp: List[float] = None
			self.Ms_Power_Wide: float = None
			self.Ms_Power_Narrow: float = None
			self.Out_Of_Tol_Count: float = None
			self.Cur_Stat_Count: int = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:ACP:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.acp.maximum.fetch(segment = repcap.Segment.Default) \n
		Returns all ACP value results for the segment <no> in list mode. To define the statistical length for AVERage, MAXimum,
		MINimum calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.
		ListPy.Segment.Spectrum.set. The ranges indicated below apply to all results except standard deviation results.
		The minimum for standard deviation results equals 0. The maximum equals the width of the indicated range divided by two.
		Exceptions are explicitly stated. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. For the out of tolerance and code channel
		filter match ratio, results retrieved via the CURRent, AVERage and MAXimum command are identical. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACP:MAXimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Current_Acp: List[enums.ResultStatus2]: No parameter help available
			- Ms_Power_Wide: enums.ResultStatus2: No parameter help available
			- Ms_Power_Narrow: enums.ResultStatus2: No parameter help available
			- Out_Of_Tol_Count: enums.ResultStatus2: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Cur_Stat_Count: enums.ResultStatus2: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct('Current_Acp', DataType.EnumList, enums.ResultStatus2, False, False, 21),
			ArgStruct.scalar_enum('Ms_Power_Wide', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ms_Power_Narrow', enums.ResultStatus2),
			ArgStruct.scalar_enum('Out_Of_Tol_Count', enums.ResultStatus2),
			ArgStruct.scalar_enum('Cur_Stat_Count', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Current_Acp: List[enums.ResultStatus2] = None
			self.Ms_Power_Wide: enums.ResultStatus2 = None
			self.Ms_Power_Narrow: enums.ResultStatus2 = None
			self.Out_Of_Tol_Count: enums.ResultStatus2 = None
			self.Cur_Stat_Count: enums.ResultStatus2 = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:ACP:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.acp.maximum.calculate(segment = repcap.Segment.Default) \n
		Returns all ACP value results for the segment <no> in list mode. To define the statistical length for AVERage, MAXimum,
		MINimum calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.
		ListPy.Segment.Spectrum.set. The ranges indicated below apply to all results except standard deviation results.
		The minimum for standard deviation results equals 0. The maximum equals the width of the indicated range divided by two.
		Exceptions are explicitly stated. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. For the out of tolerance and code channel
		filter match ratio, results retrieved via the CURRent, AVERage and MAXimum command are identical. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACP:MAXimum?', self.__class__.CalculateStruct())
