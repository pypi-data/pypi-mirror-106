from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- At_Power_Narrow: float: float Access terminal power, measured with a filter bandwidth of 1.23 MHz. Range: -100 dBm to 50 dBm, Unit: dBm
			- At_Power_Wide: float: float Access terminal power, measured with the wideband filter. Range: -100 dBm to 50 dBm, Unit: dBm
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Code_Ch_Filter: float: float Code channel filter match ratio, i.e. percentage of measurement intervals matching the specified code channel filter, see 'Multi-Evaluation: Code Channel Filter'. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('At_Power_Narrow'),
			ArgStruct.scalar_float('At_Power_Wide'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Code_Ch_Filter')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.At_Power_Narrow: float = None
			self.At_Power_Wide: float = None
			self.Out_Of_Tol_Count: float = None
			self.Code_Ch_Filter: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:ACP:AVERage \n
		Snippet: value: ResultData = driver.multiEval.acp.average.read() \n
		Return the out of tolerance result, the code channel filter match ratio result and the AT power results. For the AT power
		results, the current, average and maximum values can be retrieved. The out of tolerance and code channel filter match
		ratio results retrieved via the CURRent, AVERage and MAXimum command are identical. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:EVDO:MEASurement<Instance>:MEValuation:ACP:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:ACP:AVERage \n
		Snippet: value: ResultData = driver.multiEval.acp.average.fetch() \n
		Return the out of tolerance result, the code channel filter match ratio result and the AT power results. For the AT power
		results, the current, average and maximum values can be retrieved. The out of tolerance and code channel filter match
		ratio results retrieved via the CURRent, AVERage and MAXimum command are identical. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:ACP:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- At_Power_Narrow: float: float Access terminal power, measured with a filter bandwidth of 1.23 MHz. Range: -100 dBm to 50 dBm, Unit: dBm
			- At_Power_Wide: float: float Access terminal power, measured with the wideband filter. Range: -100 dBm to 50 dBm, Unit: dBm
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %
			- Code_Ch_Filter: float: float Code channel filter match ratio, i.e. percentage of measurement intervals matching the specified code channel filter, see 'Multi-Evaluation: Code Channel Filter'. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('At_Power_Narrow'),
			ArgStruct.scalar_float('At_Power_Wide'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Code_Ch_Filter')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.At_Power_Narrow: float = None
			self.At_Power_Wide: float = None
			self.Out_Of_Tol_Count: float = None
			self.Code_Ch_Filter: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:ACP:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.acp.average.calculate() \n
		Return the out of tolerance result, the code channel filter match ratio result and the AT power results. For the AT power
		results, the current, average and maximum values can be retrieved. The out of tolerance and code channel filter match
		ratio results retrieved via the CURRent, AVERage and MAXimum command are identical. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:ACP:AVERage?', self.__class__.CalculateStruct())
