from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
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
			- Reliabiltiy: int: decimal 'Conventions and General Information'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rri: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Pilot: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Ack_Dsc: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Aux_Pilot: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Drc: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Data: List[enums.ResultStateA]: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rri', DataType.EnumList, enums.ResultStateA, False, True, 1),
			ArgStruct('Pilot', DataType.EnumList, enums.ResultStateA, False, True, 1),
			ArgStruct('Ack_Dsc', DataType.EnumList, enums.ResultStateA, False, True, 1),
			ArgStruct('Aux_Pilot', DataType.EnumList, enums.ResultStateA, False, True, 1),
			ArgStruct('Drc', DataType.EnumList, enums.ResultStateA, False, True, 1),
			ArgStruct('Data', DataType.EnumList, enums.ResultStateA, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: List[int] = None
			self.Rri: List[enums.ResultStateA] = None
			self.Pilot: List[enums.ResultStateA] = None
			self.Ack_Dsc: List[enums.ResultStateA] = None
			self.Aux_Pilot: List[enums.ResultStateA] = None
			self.Drc: List[enums.ResultStateA] = None
			self.Data: List[enums.ResultStateA] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:CP:STATe \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.cp.state.fetch() \n
		Return the states of the channels for power measurement (CP) . The values listed below in curly brackets {} are returned
		for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined by method
		RsCmwEvdoMeas.Configure.MultiEval.ListPy.count. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:CP:STATe?', self.__class__.FetchStruct())
