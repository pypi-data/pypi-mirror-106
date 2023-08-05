from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self, acpMinus=repcap.AcpMinus.Default) -> List[float]:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:ACPM<freqpoint>:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.acp.extended.acpm.average.fetch(acpMinus = repcap.AcpMinus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±20 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpMinus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpm')
			:return: acpm: float Comma-separated list of values, one per active segment. Range: -999 dB to 999 dB, Unit: dB"""
		acpMinus_cmd_val = self._base.get_repcap_cmd_value(acpMinus, repcap.AcpMinus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:ACPM{acpMinus_cmd_val}:AVERage?', suppressed)
		return response

	def calculate(self, acpMinus=repcap.AcpMinus.Default) -> List[float]:
		"""SCPI: CALCulate:EVDO:MEASurement<instance>:MEValuation:LIST:ACP:EXTended:ACPM<freqpoint>:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.acp.extended.acpm.average.calculate(acpMinus = repcap.AcpMinus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±20 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwEvdoMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpMinus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpm')
			:return: acpm: float Comma-separated list of values, one per active segment. Range: -999 dB to 999 dB, Unit: dB"""
		acpMinus_cmd_val = self._base.get_repcap_cmd_value(acpMinus, repcap.AcpMinus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:EVDO:MEASurement<Instance>:MEValuation:LIST:ACP:EXTended:ACPM{acpMinus_cmd_val}:AVERage?', suppressed)
		return response
