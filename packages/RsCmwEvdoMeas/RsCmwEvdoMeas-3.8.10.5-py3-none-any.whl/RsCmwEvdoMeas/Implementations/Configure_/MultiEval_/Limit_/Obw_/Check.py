from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Check:
	"""Check commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("check", core, parent)

	# noinspection PyTypeChecker
	def get_used(self) -> enums.ObwUsedLimitSet:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:CHECk:USED \n
		Snippet: value: enums.ObwUsedLimitSet = driver.configure.multiEval.limit.obw.check.get_used() \n
		Returns the currently used OBW limit set. This limit is ultimately determined by the currently selected band class: limit
		set A is dedicated to band class 0, limit set B is used for all other band classes. \n
			:return: obw_used_limit_set: SETA | SETB The currently used limit set.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:CHECk:USED?')
		return Conversions.str_to_scalar_enum(response, enums.ObwUsedLimitSet)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:CHECk \n
		Snippet: value: bool = driver.configure.multiEval.limit.obw.check.get_value() \n
		Gets/sets the enabled state of OBW limit checks. Depending on the current band class, either limit set A or B applies. \n
			:return: obw_limit_check: OFF | ON Disable/enable OBW limit checks.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:CHECk?')
		return Conversions.str_to_bool(response)

	def set_value(self, obw_limit_check: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:CHECk \n
		Snippet: driver.configure.multiEval.limit.obw.check.set_value(obw_limit_check = False) \n
		Gets/sets the enabled state of OBW limit checks. Depending on the current band class, either limit set A or B applies. \n
			:param obw_limit_check: OFF | ON Disable/enable OBW limit checks.
		"""
		param = Conversions.bool_to_str(obw_limit_check)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:CHECk {param}')
