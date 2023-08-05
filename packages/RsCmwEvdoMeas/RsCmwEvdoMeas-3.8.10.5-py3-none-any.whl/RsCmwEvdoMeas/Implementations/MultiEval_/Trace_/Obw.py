from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obw:
	"""Obw commands group definition. 3 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Obw, default value after init: Obw.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("obw", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_obw_get', 'repcap_obw_set', repcap.Obw.Nr1)

	def repcap_obw_set(self, enum_value: repcap.Obw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Obw.Default
		Default value after init: Obw.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_obw_get(self) -> repcap.Obw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Obw_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'Obw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Obw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
