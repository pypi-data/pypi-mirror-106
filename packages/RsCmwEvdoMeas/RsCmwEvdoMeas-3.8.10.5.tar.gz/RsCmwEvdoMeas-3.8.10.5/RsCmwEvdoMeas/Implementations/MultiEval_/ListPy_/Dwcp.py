from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwcp:
	"""Dwcp commands group definition. 40 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dwcp", core, parent)

	@property
	def wtfi(self):
		"""wtfi commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_wtfi'):
			from .Dwcp_.Wtfi import Wtfi
			self._wtfi = Wtfi(self._core, self._base)
		return self._wtfi

	@property
	def wtfq(self):
		"""wtfq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_wtfq'):
			from .Dwcp_.Wtfq import Wtfq
			self._wtfq = Wtfq(self._core, self._base)
		return self._wtfq

	@property
	def woti(self):
		"""woti commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_woti'):
			from .Dwcp_.Woti import Woti
			self._woti = Woti(self._core, self._base)
		return self._woti

	@property
	def wotq(self):
		"""wotq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_wotq'):
			from .Dwcp_.Wotq import Wotq
			self._wotq = Wotq(self._core, self._base)
		return self._wotq

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Dwcp_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Dwcp_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Dwcp_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Dwcp_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	def clone(self) -> 'Dwcp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dwcp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
