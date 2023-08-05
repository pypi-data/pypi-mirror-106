from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oltr:
	"""Oltr commands group definition. 15 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("oltr", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Oltr_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Oltr_.Sequence import Sequence
			self._sequence = Sequence(self._core, self._base)
		return self._sequence

	def initiate(self) -> None:
		"""SCPI: INITiate:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:EVDO:MEASurement<Instance>:OLTR')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwEvdoMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:EVDO:MEASurement<Instance>:OLTR')

	def abort(self) -> None:
		"""SCPI: ABORt:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:EVDO:MEASurement<Instance>:OLTR')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwEvdoMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:EVDO:MEASurement<Instance>:OLTR')

	def stop(self) -> None:
		"""SCPI: STOP:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:EVDO:MEASurement<Instance>:OLTR')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:EVDO:MEASurement<instance>:OLTR \n
		Snippet: driver.oltr.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwEvdoMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:EVDO:MEASurement<Instance>:OLTR')

	def clone(self) -> 'Oltr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oltr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
