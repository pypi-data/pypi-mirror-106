from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
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
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 16 MHz (SDEViation 0 MHz to 8 MHz) , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:OBW:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.obw.maximum.fetch(segment = repcap.Segment.Default) \n
		In list mode, returns the occupied bandwidth (OBW) result for segment <no>. To define the statistical length for AVERage,
		MAXimum calculation and to enable the calculation of the results, use the command method RsCmwEvdoMeas.Configure.
		MultiEval.ListPy.Segment.Modulation.set. The ranges indicated below apply to all results except standard deviation
		results. The minimum for standard deviation results equals 0. The maximum equals the width of the indicated range divided
		by two. Exceptions are explicitly stated. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:MAXimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: enums.ResultStatus2: float Occupied bandwidth Range: 0 MHz to 16 MHz (SDEViation 0 MHz to 8 MHz) , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Obw', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: enums.ResultStatus2 = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:OBW:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.obw.maximum.calculate(segment = repcap.Segment.Default) \n
		In list mode, returns the occupied bandwidth (OBW) result for segment <no>. To define the statistical length for AVERage,
		MAXimum calculation and to enable the calculation of the results, use the command method RsCmwEvdoMeas.Configure.
		MultiEval.ListPy.Segment.Modulation.set. The ranges indicated below apply to all results except standard deviation
		results. The minimum for standard deviation results equals 0. The maximum equals the width of the indicated range divided
		by two. Exceptions are explicitly stated. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:MAXimum?', self.__class__.CalculateStruct())
