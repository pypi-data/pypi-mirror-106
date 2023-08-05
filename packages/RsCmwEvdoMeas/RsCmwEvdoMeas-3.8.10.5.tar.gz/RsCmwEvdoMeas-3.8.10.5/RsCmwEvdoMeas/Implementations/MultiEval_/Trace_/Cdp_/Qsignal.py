from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qsignal:
	"""Qsignal commands group definition. 28 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qsignal", core, parent)

	@property
	def rri(self):
		"""rri commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_rri'):
			from .Qsignal_.Rri import Rri
			self._rri = Rri(self._core, self._base)
		return self._rri

	@property
	def pilot(self):
		"""pilot commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Qsignal_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	def clone(self) -> 'Qsignal':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qsignal(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
