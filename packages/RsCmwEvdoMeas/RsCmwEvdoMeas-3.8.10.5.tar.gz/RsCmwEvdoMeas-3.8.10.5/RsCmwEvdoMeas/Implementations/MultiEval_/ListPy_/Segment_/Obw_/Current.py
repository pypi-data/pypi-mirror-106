from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 16 MHz , Unit: MHz
			- Lower_Freq: float: float Lower edge of the selected carrier's or carrier group's occupied bandwidth. For single-carrier configurations, the lower and upper edges are returned as frequency offsets related to the carrier's center frequency. For multi-carrier configurations, absolute frequency values are returned. Range: - 16 MHz to 6000 MHz , Unit: MHz
			- Upper_Freq: float: float Upper edge of the selected carrier's or carrier group's occupied bandwidth. For single-carrier configurations, the lower and upper edges are returned as frequency offsets related to the carrier's center frequency. For multi-carrier configurations, absolute frequency values are returned. Range: - 16 MHz to 6000 MHz , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Lower_Freq'),
			ArgStruct.scalar_float('Upper_Freq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: float = None
			self.Lower_Freq: float = None
			self.Upper_Freq: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:OBW:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.obw.current.fetch(segment = repcap.Segment.Default) \n
		Returns occupied bandwidth (OBW) results for the segment <no> in list mode. To enable the calculation of the results, use
		the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. For single-carrier configurations (i.
		e. only carrier 0 is active) the <Number> suffix can be omitted to obtain the OBW results.
		For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results
		instead, one value for each result listed below. For details, refer to 'Multi-Evaluation Measurement Results'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: enums.ResultStatus2: float Occupied bandwidth Range: 0 MHz to 16 MHz , Unit: MHz
			- Lower_Freq: float: float Lower edge of the selected carrier's or carrier group's occupied bandwidth. For single-carrier configurations, the lower and upper edges are returned as frequency offsets related to the carrier's center frequency. For multi-carrier configurations, absolute frequency values are returned. Range: - 16 MHz to 6000 MHz , Unit: MHz
			- Upper_Freq: float: float Upper edge of the selected carrier's or carrier group's occupied bandwidth. For single-carrier configurations, the lower and upper edges are returned as frequency offsets related to the carrier's center frequency. For multi-carrier configurations, absolute frequency values are returned. Range: - 16 MHz to 6000 MHz , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Obw', enums.ResultStatus2),
			ArgStruct.scalar_float('Lower_Freq'),
			ArgStruct.scalar_float('Upper_Freq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: enums.ResultStatus2 = None
			self.Lower_Freq: float = None
			self.Upper_Freq: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:OBW:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.obw.current.calculate(segment = repcap.Segment.Default) \n
		Returns occupied bandwidth (OBW) results for the segment <no> in list mode. To enable the calculation of the results, use
		the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. For single-carrier configurations (i.
		e. only carrier 0 is active) the <Number> suffix can be omitted to obtain the OBW results.
		For multi-carrier configurations the <Number> suffixes are used as follows:
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- For an active and isolated carrier i, use <Number> = i+1 to get its OBW results (i = 0, 1, 2)
			- Use <Number> = 4 to display the OBW results of the 'Overall Carrier'
			- If all active carriers are adjacent, use <Number>=4 to get the group (overall) OBW results
			- If three carriers are active and exactly two carriers i,j with 0≤i<j≤2 are adjacent, use <Number> = i+1 for the joint OBW results of adjacent carriers.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results
		instead, one value for each result listed below. For details, refer to 'Multi-Evaluation Measurement Results'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:CURRent?', self.__class__.CalculateStruct())
