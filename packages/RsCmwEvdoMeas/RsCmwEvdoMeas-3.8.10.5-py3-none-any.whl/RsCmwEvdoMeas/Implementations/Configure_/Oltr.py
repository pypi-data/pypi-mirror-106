from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oltr:
	"""Oltr commands group definition. 11 total commands, 4 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("oltr", core, parent)

	@property
	def pstep(self):
		"""pstep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pstep'):
			from .Oltr_.Pstep import Pstep
			self._pstep = Pstep(self._core, self._base)
		return self._pstep

	@property
	def rpInterval(self):
		"""rpInterval commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rpInterval'):
			from .Oltr_.RpInterval import RpInterval
			self._rpInterval = RpInterval(self._core, self._base)
		return self._rpInterval

	@property
	def ginterval(self):
		"""ginterval commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ginterval'):
			from .Oltr_.Ginterval import Ginterval
			self._ginterval = Ginterval(self._core, self._base)
		return self._ginterval

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Oltr_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:TOUT \n
		Snippet: value: float = driver.configure.oltr.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:TOUT \n
		Snippet: driver.configure.oltr.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.oltr.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:MOEXception \n
		Snippet: value: bool = driver.configure.oltr.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:MOEXception \n
		Snippet: driver.configure.oltr.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:MOEXception {param}')

	def get_sequence(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:SEQuence \n
		Snippet: value: int = driver.configure.oltr.get_sequence() \n
		Sets/gets the number of measurement sequences within a single OLTR measurement. Each sequence consists of power UP or
		power DOWN step, followed by a power step in the opposite direction (see method RsCmwEvdoMeas.Configure.Oltr.Pstep.
		direction. \n
			:return: no_of_meas_seq: numeric Range: 1 to 5
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:SEQuence?')
		return Conversions.str_to_int(response)

	def set_sequence(self, no_of_meas_seq: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:SEQuence \n
		Snippet: driver.configure.oltr.set_sequence(no_of_meas_seq = 1) \n
		Sets/gets the number of measurement sequences within a single OLTR measurement. Each sequence consists of power UP or
		power DOWN step, followed by a power step in the opposite direction (see method RsCmwEvdoMeas.Configure.Oltr.Pstep.
		direction. \n
			:param no_of_meas_seq: numeric Range: 1 to 5
		"""
		param = Conversions.decimal_value_to_str(no_of_meas_seq)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:SEQuence {param}')

	def clone(self) -> 'Oltr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oltr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
