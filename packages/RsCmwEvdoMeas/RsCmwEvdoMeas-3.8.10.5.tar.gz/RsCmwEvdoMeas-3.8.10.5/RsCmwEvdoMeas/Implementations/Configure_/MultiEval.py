from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 82 total commands, 6 Sub-groups, 17 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scount'):
			from .MultiEval_.Scount import Scount
			self._scount = Scount(self._core, self._base)
		return self._scount

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_carrier'):
			from .MultiEval_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def acp(self):
		"""acp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .MultiEval_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 12 commands."""
		if not hasattr(self, '_result'):
			from .MultiEval_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 5 Sub-classes, 11 commands."""
		if not hasattr(self, '_limit'):
			from .MultiEval_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:TOUT \n
		Snippet: driver.configure.multiEval.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_dmodulation(self) -> enums.Dmodulation:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DMODulation \n
		Snippet: value: enums.Dmodulation = driver.configure.multiEval.get_dmodulation() \n
		Specifies the data channel modulation type of the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.
		select) . This setting is only relevant for measurements using physical layer subtype 2 or 3 (see method RsCmwEvdoMeas.
		Configure.MultiEval.plSubtype) . \n
			:return: dmodulation: AUTO | B4 | Q4 | Q2 | Q4Q2 | E4E2 AUTO: automatic detection of the modulation type. Signals with unrecognized modulation type are ignored. B4: BPSK modulation with 4-ary Walsh cover (W24) Q4: QPSK modulation with 4-ary Walsh cover (W24) Q2: QPSK modulation with 2-ary Walsh cover (W12) Q4Q2: (QPSK, W24) + (QPSK, W12) E4E2: (8-PSK, W24) + (8-PSK, W12)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:DMODulation?')
		return Conversions.str_to_scalar_enum(response, enums.Dmodulation)

	def set_dmodulation(self, dmodulation: enums.Dmodulation) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DMODulation \n
		Snippet: driver.configure.multiEval.set_dmodulation(dmodulation = enums.Dmodulation.AUTO) \n
		Specifies the data channel modulation type of the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.
		select) . This setting is only relevant for measurements using physical layer subtype 2 or 3 (see method RsCmwEvdoMeas.
		Configure.MultiEval.plSubtype) . \n
			:param dmodulation: AUTO | B4 | Q4 | Q2 | Q4Q2 | E4E2 AUTO: automatic detection of the modulation type. Signals with unrecognized modulation type are ignored. B4: BPSK modulation with 4-ary Walsh cover (W24) Q4: QPSK modulation with 4-ary Walsh cover (W24) Q2: QPSK modulation with 2-ary Walsh cover (W12) Q4Q2: (QPSK, W24) + (QPSK, W12) E4E2: (8-PSK, W24) + (8-PSK, W12)
		"""
		param = Conversions.enum_scalar_to_str(dmodulation, enums.Dmodulation)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:DMODulation {param}')

	# noinspection PyTypeChecker
	def get_hslot(self) -> enums.HalfSlot:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:HSLot \n
		Snippet: value: enums.HalfSlot = driver.configure.multiEval.get_hslot() \n
		Specifies which half-slots of the code channel is/are evaluated for measurements using physical layer subtype 2 or 3 (see
		method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . Consider that the DSC channel and the ACK channel are transmitted
		time-multiplexed on Walsh channel W1232. The ACK is transmitted on the first half-slot and the DSC on the second
		half-slot. \n
			:return: hslot: FHSLot | SHSLot | BHSLots FHSLot: evaluate the first half-slot SHSLot: evaluate the second half-slot BHSLots: evaluate both half-slots
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:HSLot?')
		return Conversions.str_to_scalar_enum(response, enums.HalfSlot)

	def set_hslot(self, hslot: enums.HalfSlot) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:HSLot \n
		Snippet: driver.configure.multiEval.set_hslot(hslot = enums.HalfSlot.BHSLots) \n
		Specifies which half-slots of the code channel is/are evaluated for measurements using physical layer subtype 2 or 3 (see
		method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . Consider that the DSC channel and the ACK channel are transmitted
		time-multiplexed on Walsh channel W1232. The ACK is transmitted on the first half-slot and the DSC on the second
		half-slot. \n
			:param hslot: FHSLot | SHSLot | BHSLots FHSLot: evaluate the first half-slot SHSLot: evaluate the second half-slot BHSLots: evaluate both half-slots
		"""
		param = Conversions.enum_scalar_to_str(hslot, enums.HalfSlot)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:HSLot {param}')

	# noinspection PyTypeChecker
	def get_drc(self) -> enums.MeasCondition:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DRC \n
		Snippet: value: enums.MeasCondition = driver.configure.multiEval.get_drc() \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the data rate control (DRC) channel. \n
			:return: dr_control: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:DRC?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCondition)

	def set_drc(self, dr_control: enums.MeasCondition) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DRC \n
		Snippet: driver.configure.multiEval.set_drc(dr_control = enums.MeasCondition.DNCare) \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the data rate control (DRC) channel. \n
			:param dr_control: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		param = Conversions.enum_scalar_to_str(dr_control, enums.MeasCondition)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:DRC {param}')

	# noinspection PyTypeChecker
	def get_ack(self) -> enums.MeasCondition:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACK \n
		Snippet: value: enums.MeasCondition = driver.configure.multiEval.get_ack() \n
		Specify a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the acknowledgment channel. Value ACK is only relevant for physical layer protocol subtype 0/1
		(see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:return: ack: DNCare | ON | OFF OFF: do not evaluate the signal regardless of whether it is active or not. ON: evaluate the signal only when the ACK channel is present. Otherwise the CMW returns invalid results (INV) . DNCare: evaluate the signal irrespective of the presence of the channel.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACK?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCondition)

	def set_ack(self, ack: enums.MeasCondition) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACK \n
		Snippet: driver.configure.multiEval.set_ack(ack = enums.MeasCondition.DNCare) \n
		Specify a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the acknowledgment channel. Value ACK is only relevant for physical layer protocol subtype 0/1
		(see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:param ack: DNCare | ON | OFF OFF: do not evaluate the signal regardless of whether it is active or not. ON: evaluate the signal only when the ACK channel is present. Otherwise the CMW returns invalid results (INV) . DNCare: evaluate the signal irrespective of the presence of the channel.
		"""
		param = Conversions.enum_scalar_to_str(ack, enums.MeasCondition)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACK {param}')

	# noinspection PyTypeChecker
	def get_ack_dsc(self) -> enums.AckDsc:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACKDsc \n
		Snippet: value: enums.AckDsc = driver.configure.multiEval.get_ack_dsc() \n
		Specify a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the acknowledgment channel / data source control channel. Value DSC is only relevant for
		physical layer protocol subtypes 2 and 3 (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:return: ack_dsc: DNCare | DSC | ACK | OFF OFF: evaluate the signal only when no DSC or ACK channels are present DSC: evaluate the signal only when the DSC channel is present ACK: evaluate the signal only when the ACK channel is present DNCare: evaluate the signal irrespective of the presence of the channels
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACKDsc?')
		return Conversions.str_to_scalar_enum(response, enums.AckDsc)

	def set_ack_dsc(self, ack_dsc: enums.AckDsc) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ACKDsc \n
		Snippet: driver.configure.multiEval.set_ack_dsc(ack_dsc = enums.AckDsc.ACK) \n
		Specify a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the acknowledgment channel / data source control channel. Value DSC is only relevant for
		physical layer protocol subtypes 2 and 3 (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:param ack_dsc: DNCare | DSC | ACK | OFF OFF: evaluate the signal only when no DSC or ACK channels are present DSC: evaluate the signal only when the DSC channel is present ACK: evaluate the signal only when the ACK channel is present DNCare: evaluate the signal irrespective of the presence of the channels
		"""
		param = Conversions.enum_scalar_to_str(ack_dsc, enums.AckDsc)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ACKDsc {param}')

	# noinspection PyTypeChecker
	def get_data(self) -> enums.MeasCondition:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DATA \n
		Snippet: value: enums.MeasCondition = driver.configure.multiEval.get_data() \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the data channel. \n
			:return: code_chs_data: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCondition)

	def set_data(self, code_chs_data: enums.MeasCondition) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:DATA \n
		Snippet: driver.configure.multiEval.set_data(code_chs_data = enums.MeasCondition.DNCare) \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the data channel. \n
			:param code_chs_data: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		param = Conversions.enum_scalar_to_str(code_chs_data, enums.MeasCondition)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:DATA {param}')

	# noinspection PyTypeChecker
	def get_apilot(self) -> enums.MeasCondition:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:APILot \n
		Snippet: value: enums.MeasCondition = driver.configure.multiEval.get_apilot() \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the auxiliary pilot channel. The condition is only relevant for physical layer protocol subtypes
		2 and 3 (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:return: apilot: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:APILot?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCondition)

	def set_apilot(self, apilot: enums.MeasCondition) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:APILot \n
		Snippet: driver.configure.multiEval.set_apilot(apilot = enums.MeasCondition.DNCare) \n
		Specifies a measurement condition for the selected carrier (see method RsCmwEvdoMeas.Configure.MultiEval.Carrier.select)
		based on the presence of the auxiliary pilot channel. The condition is only relevant for physical layer protocol subtypes
		2 and 3 (see method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:param apilot: DNCare | ON | OFF DNCare: evaluate the signal irrespective of the presence of the channel ON: evaluate the signal only when the channel is present OFF: evaluate the signal only when the channel is not present
		"""
		param = Conversions.enum_scalar_to_str(apilot, enums.MeasCondition)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:APILot {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:REPetition \n
		Snippet: driver.configure.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:REPetition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_pl_subtype(self) -> enums.PlSubtype:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:PLSubtype \n
		Snippet: value: enums.PlSubtype = driver.configure.multiEval.get_pl_subtype() \n
		Selects the physical layer protocol subtype.
		For the combined signal path scenario, use CONFigure:EVDO:SIGN<i>:NETWork:RELease. \n
			:return: pl_subtype: ST01 | ST2 | ST3 ST01: subtype 0 or 1 ST2: subtype 2 ST3: subtype 3
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:PLSubtype?')
		return Conversions.str_to_scalar_enum(response, enums.PlSubtype)

	def set_pl_subtype(self, pl_subtype: enums.PlSubtype) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:PLSubtype \n
		Snippet: driver.configure.multiEval.set_pl_subtype(pl_subtype = enums.PlSubtype.ST01) \n
		Selects the physical layer protocol subtype.
		For the combined signal path scenario, use CONFigure:EVDO:SIGN<i>:NETWork:RELease. \n
			:param pl_subtype: ST01 | ST2 | ST3 ST01: subtype 0 or 1 ST2: subtype 2 ST3: subtype 3
		"""
		param = Conversions.enum_scalar_to_str(pl_subtype, enums.PlSubtype)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:PLSubtype {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopConditionB:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopConditionB = driver.configure.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. OLFail means that the measurement
		is stopped (STOP:...MEAS<i>...) and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | OLFail NONE: Continue measurement irrespective of the limit check OLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopConditionB)

	def set_scondition(self, stop_condition: enums.StopConditionB) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.multiEval.set_scondition(stop_condition = enums.StopConditionB.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. OLFail means that the measurement
		is stopped (STOP:...MEAS<i>...) and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | OLFail NONE: Continue measurement irrespective of the limit check OLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopConditionB)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_sfactor(self) -> enums.Srate:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:SFACtor \n
		Snippet: value: enums.Srate = driver.configure.multiEval.get_sfactor() \n
		Queries the spreading factor. The spreading factor cannot be set directly but depends on the physical layer protocol
		subtype (method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:return: srate: SF16 | SF32
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:SFACtor?')
		return Conversions.str_to_scalar_enum(response, enums.Srate)

	def set_sfactor(self, srate: enums.Srate) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:SFACtor \n
		Snippet: driver.configure.multiEval.set_sfactor(srate = enums.Srate.SF16) \n
		Queries the spreading factor. The spreading factor cannot be set directly but depends on the physical layer protocol
		subtype (method RsCmwEvdoMeas.Configure.MultiEval.plSubtype) . \n
			:param srate: No help available
		"""
		param = Conversions.enum_scalar_to_str(srate, enums.Srate)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:SFACtor {param}')

	def get_ilc_mask(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ILCMask \n
		Snippet: value: float = driver.configure.multiEval.get_ilc_mask() \n
		Specifies the long code mask for the I branch. \n
			:return: lc_mask_i: numeric Range: #H0 to #H3FFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:ILCMask?')
		return Conversions.str_to_float(response)

	def set_ilc_mask(self, lc_mask_i: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:ILCMask \n
		Snippet: driver.configure.multiEval.set_ilc_mask(lc_mask_i = 1.0) \n
		Specifies the long code mask for the I branch. \n
			:param lc_mask_i: numeric Range: #H0 to #H3FFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(lc_mask_i)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:ILCMask {param}')

	def get_qlcmask(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:QLCMask \n
		Snippet: value: float = driver.configure.multiEval.get_qlcmask() \n
		Specifies the long code mask for the Q branch. \n
			:return: lc_mask_q: numeric Range: #H0 to #H3FFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:QLCMask?')
		return Conversions.str_to_float(response)

	def set_qlcmask(self, lc_mask_q: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:QLCMask \n
		Snippet: driver.configure.multiEval.set_qlcmask(lc_mask_q = 1.0) \n
		Specifies the long code mask for the Q branch. \n
			:param lc_mask_q: numeric Range: #H0 to #H3FFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(lc_mask_q)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:QLCMask {param}')

	# noinspection PyTypeChecker
	def get_rp_mode(self) -> enums.RefPowerMode:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RPMode \n
		Snippet: value: enums.RefPowerMode = driver.configure.multiEval.get_rp_mode() \n
		Sets the reference power relative to which the power (in dB) of the reverse link physical channels of both the I and Q
		signal are measured. \n
			:return: ref_power_mode: ATPower | PPOWer ATPower: total channel power PPOWer: pilot power
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RPMode?')
		return Conversions.str_to_scalar_enum(response, enums.RefPowerMode)

	def set_rp_mode(self, ref_power_mode: enums.RefPowerMode) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RPMode \n
		Snippet: driver.configure.multiEval.set_rp_mode(ref_power_mode = enums.RefPowerMode.ATPower) \n
		Sets the reference power relative to which the power (in dB) of the reverse link physical channels of both the I and Q
		signal are measured. \n
			:param ref_power_mode: ATPower | PPOWer ATPower: total channel power PPOWer: pilot power
		"""
		param = Conversions.enum_scalar_to_str(ref_power_mode, enums.RefPowerMode)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RPMode {param}')

	def get_iql_check(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:IQLCheck \n
		Snippet: value: bool = driver.configure.multiEval.get_iql_check() \n
		Enables or disables the CDP I/Q leakage check. \n
			:return: iq_leakage_check: OFF | ON ON: enable check OFF: disable check
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:IQLCheck?')
		return Conversions.str_to_bool(response)

	def set_iql_check(self, iq_leakage_check: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:IQLCheck \n
		Snippet: driver.configure.multiEval.set_iql_check(iq_leakage_check = False) \n
		Enables or disables the CDP I/Q leakage check. \n
			:param iq_leakage_check: OFF | ON ON: enable check OFF: disable check
		"""
		param = Conversions.bool_to_str(iq_leakage_check)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:IQLCheck {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
