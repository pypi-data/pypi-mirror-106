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
			- Rri: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Pilot: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Ack_Dsc: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Aux_Pilot: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Drc: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Data: List[float]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rri', DataType.FloatList, None, False, True, 1),
			ArgStruct('Pilot', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ack_Dsc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Aux_Pilot', DataType.FloatList, None, False, True, 1),
			ArgStruct('Drc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Data', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: List[int] = None
			self.Rri: List[float] = None
			self.Pilot: List[float] = None
			self.Ack_Dsc: List[float] = None
			self.Aux_Pilot: List[float] = None
			self.Drc: List[float] = None
			self.Data: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:CP:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.cp.current.fetch() \n
		Returns the channel power (CP) value results in list mode. To define the statistical length for AVERage, MAXimum, MINimum
		calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.
		Segment.Modulation.set. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.
		ListPy.count. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rri: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Pilot: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Ack_Dsc: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Aux_Pilot: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Drc: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB
			- Data: List[enums.ResultStatus2]: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Range: -60 dB to +10 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rri', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Pilot', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Ack_Dsc', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Aux_Pilot', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Drc', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Data', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: List[int] = None
			self.Rri: List[enums.ResultStatus2] = None
			self.Pilot: List[enums.ResultStatus2] = None
			self.Ack_Dsc: List[enums.ResultStatus2] = None
			self.Aux_Pilot: List[enums.ResultStatus2] = None
			self.Drc: List[enums.ResultStatus2] = None
			self.Data: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:CP:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.cp.current.calculate() \n
		Returns the channel power (CP) value results in list mode. To define the statistical length for AVERage, MAXimum, MINimum
		calculation and enable the calculation of the results use the command method RsCmwEvdoMeas.Configure.MultiEval.ListPy.
		Segment.Modulation.set. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {..
		.}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwEvdoMeas.Configure.MultiEval.
		ListPy.count. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:CURRent?', self.__class__.CalculateStruct())
