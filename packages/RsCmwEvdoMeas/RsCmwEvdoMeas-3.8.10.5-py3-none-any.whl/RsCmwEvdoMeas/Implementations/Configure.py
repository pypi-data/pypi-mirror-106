from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 101 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def multiEval(self):
		"""multiEval commands group. 6 Sub-classes, 17 commands."""
		if not hasattr(self, '_multiEval'):
			from .Configure_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def oltr(self):
		"""oltr commands group. 4 Sub-classes, 4 commands."""
		if not hasattr(self, '_oltr'):
			from .Configure_.Oltr import Oltr
			self._oltr = Oltr(self._core, self._base)
		return self._oltr

	# noinspection PyTypeChecker
	def get_display(self) -> enums.Tab:
		"""SCPI: CONFigure:EVDO:MEASurement<Instance>:DISPlay \n
		Snippet: value: enums.Tab = driver.configure.get_display() \n
		Selects the view to be shown when the display is switched on during remote control. \n
			:return: tab: MEVA | OLTR Multi-evaluation - overview, OLTR view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.Tab)

	def set_display(self, tab: enums.Tab) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.set_display(tab = enums.Tab.MEVA) \n
		Selects the view to be shown when the display is switched on during remote control. \n
			:param tab: MEVA | OLTR Multi-evaluation - overview, OLTR view
		"""
		param = Conversions.enum_scalar_to_str(tab, enums.Tab)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:DISPlay {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
