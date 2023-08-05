from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acpm:
	"""Acpm commands group definition. 6 total commands, 3 Sub-groups, 0 group commands
	Repeated Capability: AcpMinus, default value after init: AcpMinus.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acpm", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_acpMinus_get', 'repcap_acpMinus_set', repcap.AcpMinus.Ch1)

	def repcap_acpMinus_set(self, enum_value: repcap.AcpMinus) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AcpMinus.Default
		Default value after init: AcpMinus.Ch1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_acpMinus_get(self) -> repcap.AcpMinus:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Acpm_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Acpm_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Acpm_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'Acpm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acpm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
