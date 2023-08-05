from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extended:
	"""Extended commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extended", core, parent)

	@property
	def lower(self):
		"""lower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lower'):
			from .Extended_.Lower import Lower
			self._lower = Lower(self._core, self._base)
		return self._lower

	@property
	def upper(self):
		"""upper commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_upper'):
			from .Extended_.Upper import Upper
			self._upper = Upper(self._core, self._base)
		return self._upper

	def clone(self) -> 'Extended':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Extended(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
