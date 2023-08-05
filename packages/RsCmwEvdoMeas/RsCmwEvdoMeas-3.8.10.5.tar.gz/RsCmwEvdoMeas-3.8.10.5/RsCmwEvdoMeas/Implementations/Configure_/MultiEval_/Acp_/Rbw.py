from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbw:
	"""Rbw commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rbw", core, parent)

	# noinspection PyTypeChecker
	def get_lower(self) -> List[enums.Rbw]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:RBW:LOWer \n
		Snippet: value: List[enums.Rbw] = driver.configure.multiEval.acp.rbw.get_lower() \n
		Defines the resolution bandwidth to be used for lower frequency offset 9 to 0 of the selected carrier for ACP
		measurements (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . \n
			:return: rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:RBW:LOWer?')
		return Conversions.str_to_list_enum(response, enums.Rbw)

	def set_lower(self, rbw: List[enums.Rbw]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:RBW:LOWer \n
		Snippet: driver.configure.multiEval.acp.rbw.set_lower(rbw = [Rbw.F100k, Rbw.F6K25]) \n
		Defines the resolution bandwidth to be used for lower frequency offset 9 to 0 of the selected carrier for ACP
		measurements (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . \n
			:param rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz Unit: Hz
		"""
		param = Conversions.enum_list_to_str(rbw, enums.Rbw)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:RBW:LOWer {param}')

	# noinspection PyTypeChecker
	def get_upper(self) -> List[enums.Rbw]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:RBW:UPPer \n
		Snippet: value: List[enums.Rbw] = driver.configure.multiEval.acp.rbw.get_upper() \n
		Defines the resolution bandwidth to be used for upper frequency offset 0 to 9 of the selected carrier for ACP
		measurements (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . \n
			:return: rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:RBW:UPPer?')
		return Conversions.str_to_list_enum(response, enums.Rbw)

	def set_upper(self, rbw: List[enums.Rbw]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:RBW:UPPer \n
		Snippet: driver.configure.multiEval.acp.rbw.set_upper(rbw = [Rbw.F100k, Rbw.F6K25]) \n
		Defines the resolution bandwidth to be used for upper frequency offset 0 to 9 of the selected carrier for ACP
		measurements (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . \n
			:param rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz Unit: Hz
		"""
		param = Conversions.enum_list_to_str(rbw, enums.Rbw)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:RBW:UPPer {param}')
