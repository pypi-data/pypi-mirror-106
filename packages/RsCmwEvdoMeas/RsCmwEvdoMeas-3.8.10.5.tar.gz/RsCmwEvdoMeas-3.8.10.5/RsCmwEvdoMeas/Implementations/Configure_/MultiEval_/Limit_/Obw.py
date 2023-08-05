from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obw:
	"""Obw commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("obw", core, parent)

	@property
	def check(self):
		"""check commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_check'):
			from .Obw_.Check import Check
			self._check = Check(self._core, self._base)
		return self._check

	def get_multi(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:MULTi \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.obw.get_multi() \n
		Gets/sets the overall occupied bandwidth limit and the state of the limit check for multi-carrier configurations. \n
			:return: obw_limit: Range: 0 MHz to 16 MHz Additional parameter values: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:MULTi?')
		return Conversions.str_to_float_or_bool(response)

	def set_multi(self, obw_limit: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:MULTi \n
		Snippet: driver.configure.multiEval.limit.obw.set_multi(obw_limit = 1.0) \n
		Gets/sets the overall occupied bandwidth limit and the state of the limit check for multi-carrier configurations. \n
			:param obw_limit: Range: 0 MHz to 16 MHz Additional parameter values: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.decimal_or_bool_value_to_str(obw_limit)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:MULTi {param}')

	def get_seta(self) -> List[float]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:SETA \n
		Snippet: value: List[float] = driver.configure.multiEval.limit.obw.get_seta() \n
		Gets/sets the OBW limits for limit set A. This limit set is dedicated to band class 0. \n
			:return: obw_limit_set_a: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:SETA?')
		return response

	def set_seta(self, obw_limit_set_a: List[float]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:SETA \n
		Snippet: driver.configure.multiEval.limit.obw.set_seta(obw_limit_set_a = [1.1, 2.2, 3.3]) \n
		Gets/sets the OBW limits for limit set A. This limit set is dedicated to band class 0. \n
			:param obw_limit_set_a: No help available
		"""
		param = Conversions.list_to_csv_str(obw_limit_set_a)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:SETA {param}')

	def get_setb(self) -> List[float]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:SETB \n
		Snippet: value: List[float] = driver.configure.multiEval.limit.obw.get_setb() \n
		Gets/sets the OBW limits for limit set B. This limit set is used if the currently selected band class is different from 0. \n
			:return: obw_limit_set_b: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:SETB?')
		return response

	def set_setb(self, obw_limit_set_b: List[float]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:OBW:SETB \n
		Snippet: driver.configure.multiEval.limit.obw.set_setb(obw_limit_set_b = [1.1, 2.2, 3.3]) \n
		Gets/sets the OBW limits for limit set B. This limit set is used if the currently selected band class is different from 0. \n
			:param obw_limit_set_b: No help available
		"""
		param = Conversions.list_to_csv_str(obw_limit_set_b)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:OBW:SETB {param}')

	def clone(self) -> 'Obw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Obw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
