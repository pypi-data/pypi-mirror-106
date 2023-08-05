from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Rri: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Pilot: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Ack_Dsc: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Aux_Pilot: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Drc: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Data: float: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Rri'),
			ArgStruct.scalar_float('Pilot'),
			ArgStruct.scalar_float('Ack_Dsc'),
			ArgStruct.scalar_float('Aux_Pilot'),
			ArgStruct.scalar_float('Drc'),
			ArgStruct.scalar_float('Data')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rri: float = None
			self.Pilot: float = None
			self.Ack_Dsc: float = None
			self.Aux_Pilot: float = None
			self.Drc: float = None
			self.Data: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:CP:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.trace.cp.maximum.read() \n
		Returns the channel power of the reverse link physical channels of both the I and Q signal. The slots for the pilot and
		the RRI channel are evaluated within the same measurement slot. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:CP:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CP:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.trace.cp.maximum.fetch() \n
		Returns the channel power of the reverse link physical channels of both the I and Q signal. The slots for the pilot and
		the RRI channel are evaluated within the same measurement slot. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CP:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Rri: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Pilot: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Ack_Dsc: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Aux_Pilot: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Drc: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB
			- Data: enums.ResultStatus2: float RMS channel power values for the physical channels. Depending on the subtype 0/1 or 2, some channels exist or not. If not available, no power measurement is possible therefore NAV is returned. Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Rri', enums.ResultStatus2),
			ArgStruct.scalar_enum('Pilot', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ack_Dsc', enums.ResultStatus2),
			ArgStruct.scalar_enum('Aux_Pilot', enums.ResultStatus2),
			ArgStruct.scalar_enum('Drc', enums.ResultStatus2),
			ArgStruct.scalar_enum('Data', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rri: enums.ResultStatus2 = None
			self.Pilot: enums.ResultStatus2 = None
			self.Ack_Dsc: enums.ResultStatus2 = None
			self.Aux_Pilot: enums.ResultStatus2 = None
			self.Drc: enums.ResultStatus2 = None
			self.Data: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:TRACe:CP:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.trace.cp.maximum.calculate() \n
		Returns the channel power of the reverse link physical channels of both the I and Q signal. The slots for the pilot and
		the RRI channel are evaluated within the same measurement slot. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:TRACe:CP:MAXimum?', self.__class__.CalculateStruct())
