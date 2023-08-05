from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Down:
	"""Down commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("down", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_state'):
			from .Down_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def read(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: READ:EVDO:MEASurement<instance>:OLTR:SEQuence<Sequence>:TRACe:DOWN \n
		Snippet: value: List[float] = driver.oltr.sequence.trace.down.read(sequence = repcap.Sequence.Default) \n
		Returns the values of the OLTR traces. For each sequence, DOWN/UP commands return the results of the 100 ms interval
		following the power up/down step. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:EVDO:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:DOWN?', suppressed)
		return response

	def fetch(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:OLTR:SEQuence<Sequence>:TRACe:DOWN \n
		Snippet: value: List[float] = driver.oltr.sequence.trace.down.fetch(sequence = repcap.Sequence.Default) \n
		Returns the values of the OLTR traces. For each sequence, DOWN/UP commands return the results of the 100 ms interval
		following the power up/down step. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:DOWN?', suppressed)
		return response

	def clone(self) -> 'Down':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Down(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
