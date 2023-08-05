from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lower", core, parent)

	def get_relative(self) -> List[float or bool]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:ACP:LOWer[:RELative] \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.limit.acp.lower.get_relative() \n
		Defines limits for the relative ACP in dBc of the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.
		select) at the individual negative offset frequencies (set via method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.
		lower) . The limit index 0 to 9 corresponds to the index used in manual control. \n
			:return: acp_setting: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:ACP:LOWer:RELative?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_relative(self, acp_setting: List[float or bool]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:ACP:LOWer[:RELative] \n
		Snippet: driver.configure.multiEval.limit.acp.lower.set_relative(acp_setting = [1.1, True, 2.2, False, 3.3]) \n
		Defines limits for the relative ACP in dBc of the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.
		select) at the individual negative offset frequencies (set via method RsCmwEvdoMeas.Configure.MultiEval.Acp.Foffsets.
		lower) . The limit index 0 to 9 corresponds to the index used in manual control. \n
			:param acp_setting: numeric | ON | OFF Range: -80 dBc to 10 dBc, Unit: dBc Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.list_to_csv_str(acp_setting)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:ACP:LOWer:RELative {param}')

	def get_absolute(self) -> List[float or bool]:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:ACP:LOWer:ABSolute \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.limit.acp.lower.get_absolute() \n
		Defines lower limits 9 to 0 for the ACP measurement in dBm of the selected carrier (see method RsCmwEvdoMeas.Configure.
		MultiEval.Carrier.select) at the individual negative offset frequencies (set via method RsCmwEvdoMeas.Configure.MultiEval.
		Acp.Foffsets.lower) . The limit index 9 to 0 corresponds to the index used in manual control. \n
			:return: acp_setting: Range: -80 dBm to 10 dBm , Unit: dBm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:ACP:LOWer:ABSolute?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_absolute(self, acp_setting: List[float or bool]) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIMit:ACP:LOWer:ABSolute \n
		Snippet: driver.configure.multiEval.limit.acp.lower.set_absolute(acp_setting = [1.1, True, 2.2, False, 3.3]) \n
		Defines lower limits 9 to 0 for the ACP measurement in dBm of the selected carrier (see method RsCmwEvdoMeas.Configure.
		MultiEval.Carrier.select) at the individual negative offset frequencies (set via method RsCmwEvdoMeas.Configure.MultiEval.
		Acp.Foffsets.lower) . The limit index 9 to 0 corresponds to the index used in manual control. \n
			:param acp_setting: Range: -80 dBm to 10 dBm , Unit: dBm Additional parameters: OFF | ON (disables | enables the limit check)
		"""
		param = Conversions.list_to_csv_str(acp_setting)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIMit:ACP:LOWer:ABSolute {param}')
