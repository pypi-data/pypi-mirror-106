from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 8 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	@property
	def foffsets(self):
		"""foffsets commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_foffsets'):
			from .Acp_.Foffsets import Foffsets
			self._foffsets = Foffsets(self._core, self._base)
		return self._foffsets

	@property
	def extended(self):
		"""extended commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_extended'):
			from .Acp_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rbw'):
			from .Acp_.Rbw import Rbw
			self._rbw = Rbw(self._core, self._base)
		return self._rbw

	def clone(self) -> 'Acp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
