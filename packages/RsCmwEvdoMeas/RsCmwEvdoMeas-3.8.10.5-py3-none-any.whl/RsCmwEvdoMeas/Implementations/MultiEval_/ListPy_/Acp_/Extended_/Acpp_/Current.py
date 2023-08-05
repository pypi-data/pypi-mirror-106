from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, acpPlus=repcap.AcpPlus.Default) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:ACPP<freqpoint>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.listPy.acp.extended.acpp.current.fetch(acpPlus = repcap.AcpPlus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±20 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpPlus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpp')
			:return: acpm: float Comma-separated list of values, one per active segment. Range: -999 dB to 999 dB, Unit: dB"""
		acpPlus_cmd_val = self._base.get_repcap_cmd_value(acpPlus, repcap.AcpPlus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:ACPP{acpPlus_cmd_val}:CURRent?', suppressed)
		return response

	def calculate(self, acpPlus=repcap.AcpPlus.Default) -> List[float]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:ACPP<freqpoint>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.listPy.acp.extended.acpp.current.calculate(acpPlus = repcap.AcpPlus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±20 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpPlus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpp')
			:return: acpm: float Comma-separated list of values, one per active segment. Range: -999 dB to 999 dB, Unit: dB"""
		acpPlus_cmd_val = self._base.get_repcap_cmd_value(acpPlus, repcap.AcpPlus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:ACPP{acpPlus_cmd_val}:CURRent?', suppressed)
		return response
