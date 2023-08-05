from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isignal:
	"""Isignal commands group definition. 22 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("isignal", core, parent)

	@property
	def rri(self):
		"""rri commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_rri'):
			from .Isignal_.Rri import Rri
			self._rri = Rri(self._core, self._base)
		return self._rri

	@property
	def pilot(self):
		"""pilot commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Isignal_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	def clone(self) -> 'Isignal':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Isignal(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
