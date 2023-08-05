from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffsets:
	"""Foffsets commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("foffsets", core, parent)

	def get_lower(self) -> List[float or bool]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:EXTended:FOFFsets:LOWer \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.acp.extended.foffsets.get_lower() \n
		Defines the negative (lower) frequency offsets 19 to 0, to be used for extended ACP measurements of the selected carrier
		(see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. The offset index 19 to 0 corresponds to the index used in manual
		control. \n
			:return: frequency_offset: Range: -4 MHz to 0 MHz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets:LOWer?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_lower(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:EXTended:FOFFsets:LOWer \n
		Snippet: driver.configure.multiEval.acp.extended.foffsets.set_lower(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the negative (lower) frequency offsets 19 to 0, to be used for extended ACP measurements of the selected carrier
		(see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. The offset index 19 to 0 corresponds to the index used in manual
		control. \n
			:param frequency_offset: Range: -4 MHz to 0 MHz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets:LOWer {param}')

	def get_upper(self) -> List[float or bool]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:EXTended:FOFFsets:UPPer \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.acp.extended.foffsets.get_upper() \n
		Defines the positive (upper) frequency offsets 0 to 19, to be used for extended ACP measurements of the selected carrier
		(see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. The offset index 0 to 19 corresponds to the index used in manual
		control. \n
			:return: frequency_offset: Range: 0 MHz to 4 MHz , Unit: Hz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets:UPPer?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_upper(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACP:EXTended:FOFFsets:UPPer \n
		Snippet: driver.configure.multiEval.acp.extended.foffsets.set_upper(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the positive (upper) frequency offsets 0 to 19, to be used for extended ACP measurements of the selected carrier
		(see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select) . The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. The offset index 0 to 19 corresponds to the index used in manual
		control. \n
			:param frequency_offset: Range: 0 MHz to 4 MHz , Unit: Hz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets:UPPer {param}')
