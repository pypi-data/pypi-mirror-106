from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ginterval:
	"""Ginterval commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ginterval", core, parent)

	def get_time(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:GINTerval:TIME \n
		Snippet: value: float = driver.configure.oltr.ginterval.get_time() \n
		Gets the duration of the guard intervals, i.e. the intervals succeeding the OLTR evaluation intervals and preceding the
		reference power intervals. \n
			:return: guard_interval: float Range: 5 ms to 100 ms
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:GINTerval:TIME?')
		return Conversions.str_to_float(response)

	def get_value(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:GINTerval \n
		Snippet: value: int = driver.configure.oltr.ginterval.get_value() \n
		Defines the duration of the guard intervals, i.e. the intervals succeeding the OLTR evaluation intervals and preceding
		the reference power intervals. \n
			:return: guard_interval: integer The duration of the guard interval as number of power control groups (1.25 ms) . Range: 3 to 60
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:GINTerval?')
		return Conversions.str_to_int(response)

	def set_value(self, guard_interval: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:GINTerval \n
		Snippet: driver.configure.oltr.ginterval.set_value(guard_interval = 1) \n
		Defines the duration of the guard intervals, i.e. the intervals succeeding the OLTR evaluation intervals and preceding
		the reference power intervals. \n
			:param guard_interval: integer The duration of the guard interval as number of power control groups (1.25 ms) . Range: 3 to 60
		"""
		param = Conversions.decimal_value_to_str(guard_interval)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:GINTerval {param}')
