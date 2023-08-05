from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 66 total commands, 12 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	@property
	def otolerance(self):
		"""otolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_otolerance'):
			from .Acp_.Otolerance import Otolerance
			self._otolerance = Otolerance(self._core, self._base)
		return self._otolerance

	@property
	def stCount(self):
		"""stCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stCount'):
			from .Acp_.StCount import StCount
			self._stCount = StCount(self._core, self._base)
		return self._stCount

	@property
	def acpm(self):
		"""acpm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acpm'):
			from .Acp_.Acpm import Acpm
			self._acpm = Acpm(self._core, self._base)
		return self._acpm

	@property
	def extended(self):
		"""extended commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_extended'):
			from .Acp_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	@property
	def acpp(self):
		"""acpp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acpp'):
			from .Acp_.Acpp import Acpp
			self._acpp = Acpp(self._core, self._base)
		return self._acpp

	@property
	def npow(self):
		"""npow commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_npow'):
			from .Acp_.Npow import Npow
			self._npow = Npow(self._core, self._base)
		return self._npow

	@property
	def wpow(self):
		"""wpow commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_wpow'):
			from .Acp_.Wpow import Wpow
			self._wpow = Wpow(self._core, self._base)
		return self._wpow

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Acp_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Acp_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Acp_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Acp_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Acp_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Acp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
