from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RetriggerMode:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:LIST:MODE \n
		Snippet: value: enums.RetriggerMode = driver.trigger.multiEval.listPy.get_mode() \n
		Specifies whether a trigger event initiates a measurement of the entire measurement interval (comprising the number of
		segments defined via method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count) or the retrigger information from the
		segments is used. \n
			:return: retrigger_mode: ONCE | SEGMent ONCE: Trigger only once. Every segment is measured irrespective the setting of the parameter RetriggerOption for the segment (method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Setup.set) . The trigger is rearmed only after the measurement is stopped and restarted. SEGM: The measurement starts after the first trigger event and continues as long as no segment is reached that requires a retrigger (method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Setup.set) . This mode is recommended for statistic counts where retriggering can compensate a possible time drift of the AT.
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RetriggerMode)

	def set_mode(self, retrigger_mode: enums.RetriggerMode) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:LIST:MODE \n
		Snippet: driver.trigger.multiEval.listPy.set_mode(retrigger_mode = enums.RetriggerMode.ONCE) \n
		Specifies whether a trigger event initiates a measurement of the entire measurement interval (comprising the number of
		segments defined via method RsCmwEvdoMeas.Configure.MultiEval.ListPy.count) or the retrigger information from the
		segments is used. \n
			:param retrigger_mode: ONCE | SEGMent ONCE: Trigger only once. Every segment is measured irrespective the setting of the parameter RetriggerOption for the segment (method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Setup.set) . The trigger is rearmed only after the measurement is stopped and restarted. SEGM: The measurement starts after the first trigger event and continues as long as no segment is reached that requires a retrigger (method RsCmwEvdoMeas.Configure.MultiEval.ListPy.Segment.Setup.set) . This mode is recommended for statistic counts where retriggering can compensate a possible time drift of the AT.
		"""
		param = Conversions.enum_scalar_to_str(retrigger_mode, enums.RetriggerMode)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:LIST:MODE {param}')
