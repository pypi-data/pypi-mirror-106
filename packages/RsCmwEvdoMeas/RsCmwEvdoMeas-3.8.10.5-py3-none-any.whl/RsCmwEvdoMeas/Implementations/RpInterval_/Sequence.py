from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 4 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Sequence, default value after init: Sequence.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sequence", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_sequence_get', 'repcap_sequence_set', repcap.Sequence.Nr1)

	def repcap_sequence_set(self, enum_value: repcap.Sequence) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Sequence.Default
		Default value after init: Sequence.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_sequence_get(self) -> repcap.Sequence:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Sequence_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def clone(self) -> 'Sequence':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequence(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
