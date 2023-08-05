from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_relative'):
			from .Current_.Relative import Relative
			self._relative = Relative(self._core, self._base)
		return self._relative

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_absolute'):
			from .Current_.Absolute import Absolute
			self._absolute = Absolute(self._core, self._base)
		return self._absolute

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
