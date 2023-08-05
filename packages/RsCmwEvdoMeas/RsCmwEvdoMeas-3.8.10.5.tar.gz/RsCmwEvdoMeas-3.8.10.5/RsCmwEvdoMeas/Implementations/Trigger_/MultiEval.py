from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 9 total commands, 2 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .MultiEval_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def get_source(self) -> str:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:SOURce \n
		Snippet: value: str = driver.trigger.multiEval.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: trigger_source: string 'Free Run': Free run (untriggered) 'IF Power': Power trigger (received RF power) 'IF Auto Sync': Power trigger auto synchronized
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:SOURce?')
		return trim_str_response(response)

	def set_source(self, trigger_source: str) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:SOURce \n
		Snippet: driver.trigger.multiEval.set_source(trigger_source = '1') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param trigger_source: string 'Free Run': Free run (untriggered) 'IF Power': Power trigger (received RF power) 'IF Auto Sync': Power trigger auto synchronized
		"""
		param = Conversions.value_to_quoted_str(trigger_source)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:SOURce {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.TriggerSlope:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:SLOPe \n
		Snippet: value: enums.TriggerSlope = driver.trigger.multiEval.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: trigger_slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSlope)

	def set_slope(self, trigger_slope: enums.TriggerSlope) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:SLOPe \n
		Snippet: driver.trigger.multiEval.set_slope(trigger_slope = enums.TriggerSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param trigger_slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(trigger_slope, enums.TriggerSlope)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:SLOPe {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:THReshold \n
		Snippet: value: float = driver.trigger.multiEval.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: numeric Range: -50 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:THReshold \n
		Snippet: driver.trigger.multiEval.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: numeric Range: -50 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:THReshold {param}')

	def get_delay(self) -> float:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:DELay \n
		Snippet: value: float = driver.trigger.multiEval.get_delay() \n
		Defines a time delaying the start of the measurement relative to the trigger event. This setting has no influence on
		'Free Run' measurements. \n
			:return: delay: numeric Range: -1.25E-3 s to 0.08 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:DELay \n
		Snippet: driver.trigger.multiEval.set_delay(delay = 1.0) \n
		Defines a time delaying the start of the measurement relative to the trigger event. This setting has no influence on
		'Free Run' measurements. \n
			:param delay: numeric Range: -1.25E-3 s to 0.08 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:DELay {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: value: float or bool = driver.trigger.multiEval.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: trigger_time: Range: 0 s to 83.88607E+3 s, Unit: s Additional parameters: OFF | ON (disables | enables the timeout)
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_time: float or bool) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: driver.trigger.multiEval.set_timeout(trigger_time = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param trigger_time: Range: 0 s to 83.88607E+3 s, Unit: s Additional parameters: OFF | ON (disables | enables the timeout)
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_time)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:MGAP \n
		Snippet: value: float = driver.trigger.multiEval.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: min_trigger_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, min_trigger_gap: float) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:MGAP \n
		Snippet: driver.trigger.multiEval.set_mgap(min_trigger_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param min_trigger_gap: numeric Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(min_trigger_gap)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:MGAP {param}')

	def get_eoffset(self) -> int:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:EOFFset \n
		Snippet: value: int = driver.trigger.multiEval.get_eoffset() \n
		Defines a delay time for the measurement relative to the 'IF Power' or external trigger events (see method RsCmwEvdoMeas.
		Trigger.MultiEval.source) . The range is entered as an integer number of slots. Each slot has a duration of 1.25 ms. \n
			:return: eval_offset: integer Range: 0 to 64, Unit: slot
		"""
		response = self._core.io.query_str('TRIGger:EVDO:MEASurement<Instance>:MEValuation:EOFFset?')
		return Conversions.str_to_int(response)

	def set_eoffset(self, eval_offset: int) -> None:
		"""SCPI: TRIGger:EVDO:MEASurement<instance>:MEValuation:EOFFset \n
		Snippet: driver.trigger.multiEval.set_eoffset(eval_offset = 1) \n
		Defines a delay time for the measurement relative to the 'IF Power' or external trigger events (see method RsCmwEvdoMeas.
		Trigger.MultiEval.source) . The range is entered as an integer number of slots. Each slot has a duration of 1.25 ms. \n
			:param eval_offset: integer Range: 0 to 64, Unit: slot
		"""
		param = Conversions.decimal_value_to_str(eval_offset)
		self._core.io.write(f'TRIGger:EVDO:MEASurement<Instance>:MEValuation:EOFFset {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
