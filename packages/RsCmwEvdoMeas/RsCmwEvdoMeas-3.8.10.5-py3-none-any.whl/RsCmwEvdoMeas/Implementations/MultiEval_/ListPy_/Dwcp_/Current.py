from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- W_24_I: List[float]: No parameter help available
			- W_24_Q: List[float]: No parameter help available
			- W_12_I: List[float]: No parameter help available
			- W_12_Q: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('W_24_I', DataType.FloatList, None, False, True, 1),
			ArgStruct('W_24_Q', DataType.FloatList, None, False, True, 1),
			ArgStruct('W_12_I', DataType.FloatList, None, False, True, 1),
			ArgStruct('W_12_Q', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: List[int] = None
			self.W_24_I: List[float] = None
			self.W_24_Q: List[float] = None
			self.W_12_I: List[float] = None
			self.W_12_Q: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:DWCP:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.dwcp.current.fetch() \n
		Returns the scalar channel power for the data channel results in list mode. The result is extended to the W24 and W12 I/Q
		values of the data channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is returned in list mode.
		To define the statistical length for AVERage, MAXimum, MINimum calculation and enable the calculation of the results use
		the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The values listed below in curly
		brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments
		n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:DWCP:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- W_24_I: List[enums.ResultStatus2]: No parameter help available
			- W_24_Q: List[enums.ResultStatus2]: No parameter help available
			- W_12_I: List[enums.ResultStatus2]: No parameter help available
			- W_12_Q: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('W_24_I', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('W_24_Q', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('W_12_I', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('W_12_Q', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: List[int] = None
			self.W_24_I: List[enums.ResultStatus2] = None
			self.W_24_Q: List[enums.ResultStatus2] = None
			self.W_12_I: List[enums.ResultStatus2] = None
			self.W_12_Q: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:DWCP:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.dwcp.current.calculate() \n
		Returns the scalar channel power for the data channel results in list mode. The result is extended to the W24 and W12 I/Q
		values of the data channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is returned in list mode.
		To define the statistical length for AVERage, MAXimum, MINimum calculation and enable the calculation of the results use
		the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The values listed below in curly
		brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments
		n is determined by method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:DWCP:CURRent?', self.__class__.CalculateStruct())
