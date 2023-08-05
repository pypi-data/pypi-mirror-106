from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rri: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Pilot: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Ack_Dsc: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Aux_Pilot: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Drc: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Data: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Rri'),
			ArgStruct.scalar_float('Pilot'),
			ArgStruct.scalar_float('Ack_Dsc'),
			ArgStruct.scalar_float('Aux_Pilot'),
			ArgStruct.scalar_float('Drc'),
			ArgStruct.scalar_float('Data')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Rri: float = None
			self.Pilot: float = None
			self.Ack_Dsc: float = None
			self.Aux_Pilot: float = None
			self.Drc: float = None
			self.Data: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CP:AVERage \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.cp.average.fetch(segment = repcap.Segment.Default) \n
		Returns channel power (CP) results for the segment <no> in list mode. To define the statistical length for AVERage,
		MAXimum, MINimum calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.
		MultiEval.ListPy.Segment.Modulation.set. The values described below are returned by FETCh commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:AVERage?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rri: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Pilot: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Ack_Dsc: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Aux_Pilot: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Drc: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Data: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Rri', enums.ResultStatus2),
			ArgStruct.scalar_enum('Pilot', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ack_Dsc', enums.ResultStatus2),
			ArgStruct.scalar_enum('Aux_Pilot', enums.ResultStatus2),
			ArgStruct.scalar_enum('Drc', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Rri: enums.ResultStatus2 = None
			self.Pilot: enums.ResultStatus2 = None
			self.Ack_Dsc: enums.ResultStatus2 = None
			self.Aux_Pilot: enums.ResultStatus2 = None
			self.Drc: enums.ResultStatus2 = None
			self.Data: enums.ResultStatus2 = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CP:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.cp.average.calculate(segment = repcap.Segment.Default) \n
		Returns channel power (CP) results for the segment <no> in list mode. To define the statistical length for AVERage,
		MAXimum, MINimum calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.
		MultiEval.ListPy.Segment.Modulation.set. The values described below are returned by FETCh commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:AVERage?', self.__class__.CalculateStruct())
