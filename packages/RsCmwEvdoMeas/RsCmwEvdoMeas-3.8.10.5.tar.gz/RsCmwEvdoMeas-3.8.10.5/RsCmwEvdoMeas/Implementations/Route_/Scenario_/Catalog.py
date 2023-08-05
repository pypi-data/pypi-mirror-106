from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get_cspath(self) -> List[str]:
		"""SCPI: ROUTe:EVDO:MEASurement<instance>:SCENario:CATalog:CSPath \n
		Snippet: value: List[str] = driver.route.scenario.catalog.get_cspath() \n
		Lists all applications that can be set as master for the combined signal path scenario using method RsCmwEvdoMeas.Route.
		Scenario.cspath. \n
			:return: source_list: string Comma-separated list. Each supported value is represented as a string.
		"""
		response = self._core.io.query_str('ROUTe:EVDO:MEASurement<Instance>:SCENario:CATalog:CSPath?')
		return Conversions.str_to_str_list(response)
