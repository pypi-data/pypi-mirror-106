from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cp:
	"""Cp commands group definition. 63 total commands, 11 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cp", core, parent)

	@property
	def rri(self):
		"""rri commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rri'):
			from .Cp_.Rri import Rri
			self._rri = Rri(self._core, self._base)
		return self._rri

	@property
	def pilot(self):
		"""pilot commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Cp_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	@property
	def adsc(self):
		"""adsc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_adsc'):
			from .Cp_.Adsc import Adsc
			self._adsc = Adsc(self._core, self._base)
		return self._adsc

	@property
	def apilot(self):
		"""apilot commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_apilot'):
			from .Cp_.Apilot import Apilot
			self._apilot = Apilot(self._core, self._base)
		return self._apilot

	@property
	def drc(self):
		"""drc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_drc'):
			from .Cp_.Drc import Drc
			self._drc = Drc(self._core, self._base)
		return self._drc

	@property
	def data(self):
		"""data commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Cp_.Data import Data
			self._data = Data(self._core, self._base)
		return self._data

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Cp_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Cp_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Cp_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Cp_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cp_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def clone(self) -> 'Cp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
