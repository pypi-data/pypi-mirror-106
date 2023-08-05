from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


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
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rri: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Pilot: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Ack_Dsc: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Aux_Pilot: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Drc: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel
			- Data: enums.ResultStateA: INVisible | ACTive | IACTive 'INV': No channel available 'ACTive': Active channel 'IACtive': Inactive channel"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliabiltiy'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Rri', enums.ResultStateA),
			ArgStruct.scalar_enum('Pilot', enums.ResultStateA),
			ArgStruct.scalar_enum('Ack_Dsc', enums.ResultStateA),
			ArgStruct.scalar_enum('Aux_Pilot', enums.ResultStateA),
			ArgStruct.scalar_enum('Drc', enums.ResultStateA),
			ArgStruct.scalar_enum('Data', enums.ResultStateA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: int = None
			self.Seg_Reliability: int = None
			self.Rri: enums.ResultStateA = None
			self.Pilot: enums.ResultStateA = None
			self.Ack_Dsc: enums.ResultStateA = None
			self.Aux_Pilot: enums.ResultStateA = None
			self.Drc: enums.ResultStateA = None
			self.Data: enums.ResultStateA = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:CP:STATe \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.cp.state.fetch(segment = repcap.Segment.Default) \n
		Return the states of the channels for power measurement (CP) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:STATe?', self.__class__.FetchStruct())
