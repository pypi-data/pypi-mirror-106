from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def get_ilower(self) -> int:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:LIMit:ILOWer \n
		Snippet: value: int = driver.configure.oltr.limit.get_ilower() \n
		Sets initial lower limit for open loop power control step response (3GPP2 C.S0033) . \n
			:return: initial_lower: numeric Range: -2 dB to -1 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:LIMit:ILOWer?')
		return Conversions.str_to_int(response)

	def set_ilower(self, initial_lower: int) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:LIMit:ILOWer \n
		Snippet: driver.configure.oltr.limit.set_ilower(initial_lower = 1) \n
		Sets initial lower limit for open loop power control step response (3GPP2 C.S0033) . \n
			:param initial_lower: numeric Range: -2 dB to -1 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(initial_lower)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:LIMit:ILOWer {param}')
