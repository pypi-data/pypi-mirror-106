from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Statistic_Length: int: integer The statistical length is limited by the number of steps in the segment which is defined by [CMDLINK: CONFigure:EVDO:MEASi:MEValuation:LIST:SEGMentno:SETup CMDLINK].
			- Enable_Evm: bool: OFF | ON OFF: Disable measurement. ON: Enable measurement of EVM.
			- Enable_Mag_Error: bool: OFF | ON Disable or enable measurement of magnitude error.
			- Enable_Phase_Err: bool: OFF | ON Disable or enable measurement of phase error.
			- Enable_Wave_Qual: bool: OFF | ON Disable or enable measurement of waveform quality.
			- Enable_Iq_Error: bool: OFF | ON Disable or enable measurement of I/Q origin offset and imbalance.
			- Enable_Ch_Pow: bool: OFF | ON Disable or enable measurement of channel power.
			- Enable_Dwcp: bool: OFF | ON Disable or enable measurement of data Walsh code channel power.
			- Enable_Wbnb_Pow: bool: OFF | ON Disable or enable measurement of wideband and narrowband power.
			- Enable_Freq_Err: bool: OFF | ON Disable or enable measurement of carrier frequency error.
			- Enable_Melm_Tte: bool: Optional setting parameter. OFF | ON Disable or enable measurement of transmit time error."""
		__meta_args_list = [
			ArgStruct.scalar_int('Statistic_Length'),
			ArgStruct.scalar_bool('Enable_Evm'),
			ArgStruct.scalar_bool('Enable_Mag_Error'),
			ArgStruct.scalar_bool('Enable_Phase_Err'),
			ArgStruct.scalar_bool('Enable_Wave_Qual'),
			ArgStruct.scalar_bool('Enable_Iq_Error'),
			ArgStruct.scalar_bool('Enable_Ch_Pow'),
			ArgStruct.scalar_bool('Enable_Dwcp'),
			ArgStruct.scalar_bool('Enable_Wbnb_Pow'),
			ArgStruct.scalar_bool('Enable_Freq_Err'),
			ArgStruct.scalar_bool('Enable_Melm_Tte')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Statistic_Length: int = None
			self.Enable_Evm: bool = None
			self.Enable_Mag_Error: bool = None
			self.Enable_Phase_Err: bool = None
			self.Enable_Wave_Qual: bool = None
			self.Enable_Iq_Error: bool = None
			self.Enable_Ch_Pow: bool = None
			self.Enable_Dwcp: bool = None
			self.Enable_Wbnb_Pow: bool = None
			self.Enable_Freq_Err: bool = None
			self.Enable_Melm_Tte: bool = None

	def set(self, structure: ModulationStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: driver.configure.multiEval.listPy.segment.modulation.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enables the calculation of
		the different modulation results in segment <no>; see 'Multi-Evaluation List Mode'. \n
			:param structure: for set value, see the help for ModulationStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation', structure)

	def get(self, segment=repcap.Segment.Default) -> ModulationStruct:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: value: ModulationStruct = driver.configure.multiEval.listPy.segment.modulation.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enables the calculation of
		the different modulation results in segment <no>; see 'Multi-Evaluation List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation?', self.__class__.ModulationStruct())
