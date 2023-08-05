from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 50 total commands, 5 Sub-groups, 6 group commands"""

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
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def acp(self):
		"""acp commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_acp'):
			from .MultiEval_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 14 commands."""
		if not hasattr(self, '_result'):
			from .MultiEval_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 15 commands."""
		if not hasattr(self, '_limit'):
			from .MultiEval_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:TOUT \n
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
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:TOUT \n
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
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped (STOP:...MEAS<i>...) and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped (STOP:...MEAS<i>...) and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCONdition {param}')

	# noinspection PyTypeChecker
	def get_sfactor(self) -> enums.SpreadingFactor:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SFACtor \n
		Snippet: value: enums.SpreadingFactor = driver.configure.multiEval.get_sfactor() \n
		Selects the spreading factor for the code domain power and code domain error measurements. \n
			:return: spreading_factor: SF16 | SF32 | SF64 SF16: spreading factor 16 SF32: spreading factor 32 SF64: spreading factor 64
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:SFACtor?')
		return Conversions.str_to_scalar_enum(response, enums.SpreadingFactor)

	def set_sfactor(self, spreading_factor: enums.SpreadingFactor) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SFACtor \n
		Snippet: driver.configure.multiEval.set_sfactor(spreading_factor = enums.SpreadingFactor.SF16) \n
		Selects the spreading factor for the code domain power and code domain error measurements. \n
			:param spreading_factor: SF16 | SF32 | SF64 SF16: spreading factor 16 SF32: spreading factor 32 SF64: spreading factor 64
		"""
		param = Conversions.enum_scalar_to_str(spreading_factor, enums.SpreadingFactor)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:SFACtor {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON ON: Results are never rejected OFF: Faulty results are rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:MOEXception {param}')

	def get_iql_check(self) -> bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:IQLCheck \n
		Snippet: value: bool = driver.configure.multiEval.get_iql_check() \n
		Enables or disables the CDP I/Q leakage check. \n
			:return: iq_leak_state: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:IQLCheck?')
		return Conversions.str_to_bool(response)

	def set_iql_check(self, iq_leak_state: bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:IQLCheck \n
		Snippet: driver.configure.multiEval.set_iql_check(iq_leak_state = False) \n
		Enables or disables the CDP I/Q leakage check. \n
			:param iq_leak_state: OFF | ON
		"""
		param = Conversions.bool_to_str(iq_leak_state)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:IQLCheck {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
