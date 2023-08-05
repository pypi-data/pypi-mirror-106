from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 36 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	@property
	def current(self):
		"""current commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .Acp_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def extended(self):
		"""extended commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_extended'):
			from .Acp_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	@property
	def average(self):
		"""average commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Acp_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Acp_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'Acp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
