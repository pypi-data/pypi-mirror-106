from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- W_24_I: float: No parameter help available
			- W_24_Q: float: No parameter help available
			- W_12_I: float: No parameter help available
			- W_12_Q: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('W_24_I'),
			ArgStruct.scalar_float('W_24_Q'),
			ArgStruct.scalar_float('W_12_I'),
			ArgStruct.scalar_float('W_12_Q')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: int = None
			self.W_24_I: float = None
			self.W_24_Q: float = None
			self.W_12_I: float = None
			self.W_12_Q: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:DWCP:MINimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.dwcp.minimum.fetch(segment = repcap.Segment.Default) \n
		Returns the scalar channel power for the data channel results for the segment <no> in list mode. The result is extended
		to the W24 and W12 I/Q values of the data channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is
		returned in list mode. To define the statistical length for AVERage, MAXimum, MINimum calculation and to enable the
		calculation of the results, use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The
		values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:DWCP:MINimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- W_24_I: enums.ResultStatus2: No parameter help available
			- W_24_Q: enums.ResultStatus2: No parameter help available
			- W_12_I: enums.ResultStatus2: No parameter help available
			- W_12_Q: enums.ResultStatus2: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('W_24_I', enums.ResultStatus2),
			ArgStruct.scalar_enum('W_24_Q', enums.ResultStatus2),
			ArgStruct.scalar_enum('W_12_I', enums.ResultStatus2),
			ArgStruct.scalar_enum('W_12_Q', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: int = None
			self.W_24_I: enums.ResultStatus2 = None
			self.W_24_Q: enums.ResultStatus2 = None
			self.W_12_I: enums.ResultStatus2 = None
			self.W_12_Q: enums.ResultStatus2 = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:DWCP:MINimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.dwcp.minimum.calculate(segment = repcap.Segment.Default) \n
		Returns the scalar channel power for the data channel results for the segment <no> in list mode. The result is extended
		to the W24 and W12 I/Q values of the data channel. Only available if subtype 2 or 3 is selected. Otherwise NAV is
		returned in list mode. To define the statistical length for AVERage, MAXimum, MINimum calculation and to enable the
		calculation of the results, use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The
		values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:DWCP:MINimum?', self.__class__.CalculateStruct())
