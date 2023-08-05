from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import repcap


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
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 16 MHz , Unit: Hz
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK] exceeding the specified limit, see 'Limits (Spectrum) '. Range: 0 % to 100 %
			- Code_Ch_Filter: float: float Code channel filter match ratio, i.e. percentage of measurement intervals matching the specified code channel filter, see 'Common Elements of Views'. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Code_Ch_Filter')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw: float = None
			self.Out_Of_Tol_Count: float = None
			self.Code_Ch_Filter: float = None

	def read(self, obw=repcap.Obw.Default) -> ResultData:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:OBW<Number>:AVERage \n
		Snippet: value: ResultData = driver.multiEval.obw.average.read(obw = repcap.Obw.Default) \n
		Return the current, average and maximum occupied bandwidth value result and the 'out of tolerance' result, the percentage
		of measurement intervals of the statistic counts exceeding the specified limits. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below.
		For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to obtain the OBW
		results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		return self._core.io.query_struct(f'READ:EVDO:MEASurement<Instance>:MEValuation:OBW{obw_cmd_val}:AVERage?', self.__class__.ResultData())

	def fetch(self, obw=repcap.Obw.Default) -> ResultData:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:OBW<Number>:AVERage \n
		Snippet: value: ResultData = driver.multiEval.obw.average.fetch(obw = repcap.Obw.Default) \n
		Return the current, average and maximum occupied bandwidth value result and the 'out of tolerance' result, the percentage
		of measurement intervals of the statistic counts exceeding the specified limits. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below.
		For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to obtain the OBW
		results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:OBW{obw_cmd_val}:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 16 MHz , Unit: Hz
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK] exceeding the specified limit, see 'Limits (Spectrum) '. Range: 0 % to 100 %
			- Code_Ch_Filter: float: float Code channel filter match ratio, i.e. percentage of measurement intervals matching the specified code channel filter, see 'Common Elements of Views'. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Code_Ch_Filter')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw: float = None
			self.Out_Of_Tol_Count: float = None
			self.Code_Ch_Filter: float = None

	def calculate(self, obw=repcap.Obw.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:OBW<Number>:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.obw.average.calculate(obw = repcap.Obw.Default) \n
		Return the current, average and maximum occupied bandwidth value result and the 'out of tolerance' result, the percentage
		of measurement intervals of the statistic counts exceeding the specified limits. The values described below are returned
		by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below.
		For single-carrier configurations (i.e. only carrier 0 is active) the <Number> suffix can be omitted to obtain the OBW
		results. For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers. \n
			:param obw: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Obw')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		obw_cmd_val = self._base.get_repcap_cmd_value(obw, repcap.Obw)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:OBW{obw_cmd_val}:AVERage?', self.__class__.CalculateStruct())
