from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 174 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .Trace_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Trace_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Trace_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def cdp(self):
		"""cdp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdp'):
			from .Trace_.Cdp import Cdp
			self._cdp = Cdp(self._core, self._base)
		return self._cdp

	@property
	def cde(self):
		"""cde commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cde'):
			from .Trace_.Cde import Cde
			self._cde = Cde(self._core, self._base)
		return self._cde

	@property
	def cp(self):
		"""cp commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cp'):
			from .Trace_.Cp import Cp
			self._cp = Cp(self._core, self._base)
		return self._cp

	@property
	def acp(self):
		"""acp commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .Trace_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def obw(self):
		"""obw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .Trace_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	@property
	def spectrum(self):
		"""spectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Trace_.Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._base)
		return self._spectrum

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Trace_.Iq import Iq
			self._iq = Iq(self._core, self._base)
		return self._iq

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
