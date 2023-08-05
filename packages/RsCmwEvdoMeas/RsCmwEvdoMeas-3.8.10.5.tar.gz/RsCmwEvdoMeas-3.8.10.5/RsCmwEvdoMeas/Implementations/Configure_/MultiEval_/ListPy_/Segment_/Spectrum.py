from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	# noinspection PyTypeChecker
	class SpectrumStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Statistic_Length: int: integer The statistical length is limited by the number of steps in the segment which is defined by [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:LIST:SEGMentno:SETup CMDLINK].
			- Enable_Acp_Rms: bool: OFF | ON OFF: Disable measurement ON: Enable measurement of adjacent channel power (RMS) .
			- Enable_Obw: bool: OFF | ON Disable or enable measurement of the occupied bandwidth."""
		__meta_args_list = [
			ArgStruct.scalar_int('Statistic_Length'),
			ArgStruct.scalar_bool('Enable_Acp_Rms'),
			ArgStruct.scalar_bool('Enable_Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Statistic_Length: int = None
			self.Enable_Acp_Rms: bool = None
			self.Enable_Obw: bool = None

	def set(self, structure: SpectrumStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: driver.configure.multiEval.listPy.segment.spectrum.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enables the calculation of
		the different spectrum results in segment <no>; see 'Multi-Evaluation List Mode'. \n
			:param structure: for set value, see the help for SpectrumStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum', structure)

	def get(self, segment=repcap.Segment.Default) -> SpectrumStruct:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:SPECtrum \n
		Snippet: value: SpectrumStruct = driver.configure.multiEval.listPy.segment.spectrum.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enables the calculation of
		the different spectrum results in segment <no>; see 'Multi-Evaluation List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SpectrumStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SPECtrum?', self.__class__.SpectrumStruct())
