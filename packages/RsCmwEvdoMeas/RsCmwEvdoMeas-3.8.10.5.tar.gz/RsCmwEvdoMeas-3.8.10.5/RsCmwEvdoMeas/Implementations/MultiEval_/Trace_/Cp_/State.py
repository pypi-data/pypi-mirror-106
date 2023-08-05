from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Rri: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power
			- Pilot: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power
			- Ack_Dsc: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power
			- Aux_Pilot: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power
			- Drc: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power
			- Data: enums.ResultStateA: INVisible | ACTive | IACTive The number of results depends on the physical layer subtype (see [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:PLSubtype CMDLINK]) : SF=15 for subtype 0/1 and SF=31 for subtypes 2 and 3 (only NAV values) . INV: No channel power available ACTive: Active channel power INACtive: Inactive channel power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Rri', enums.ResultStateA),
			ArgStruct.scalar_enum('Pilot', enums.ResultStateA),
			ArgStruct.scalar_enum('Ack_Dsc', enums.ResultStateA),
			ArgStruct.scalar_enum('Aux_Pilot', enums.ResultStateA),
			ArgStruct.scalar_enum('Drc', enums.ResultStateA),
			ArgStruct.scalar_enum('Data', enums.ResultStateA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rri: enums.ResultStateA = None
			self.Pilot: enums.ResultStateA = None
			self.Ack_Dsc: enums.ResultStateA = None
			self.Aux_Pilot: enums.ResultStateA = None
			self.Drc: enums.ResultStateA = None
			self.Data: enums.ResultStateA = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:CP:STATe \n
		Snippet: value: FetchStruct = driver.multiEval.trace.cp.state.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:CP:STATe?', self.__class__.FetchStruct())
