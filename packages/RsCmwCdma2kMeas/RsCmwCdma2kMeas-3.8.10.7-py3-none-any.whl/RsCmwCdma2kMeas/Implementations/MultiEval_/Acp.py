from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 12 total commands, 3 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Acp_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Acp_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_maximum'):
			from .Acp_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def read(self) -> float:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:ACP \n
		Snippet: value: float = driver.multiEval.acp.read() \n
		Returns the 'Out of Tolerance' result, i.e. the percentage of measurement intervals of the statistic count (method
		RsCmwCdma2kMeas.Configure.MultiEval.Scount.spectrum) exceeding the specified limits, see 'Limits (Spectrum) '. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: out_of_tolerance: float Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:ACP?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:ACP \n
		Snippet: value: float = driver.multiEval.acp.fetch() \n
		Returns the 'Out of Tolerance' result, i.e. the percentage of measurement intervals of the statistic count (method
		RsCmwCdma2kMeas.Configure.MultiEval.Scount.spectrum) exceeding the specified limits, see 'Limits (Spectrum) '. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: out_of_tolerance: float Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:ACP?', suppressed)
		return Conversions.str_to_float(response)

	def calculate(self) -> float:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:ACP \n
		Snippet: value: float = driver.multiEval.acp.calculate() \n
		Returns the 'Out of Tolerance' result, i.e. the percentage of measurement intervals of the statistic count (method
		RsCmwCdma2kMeas.Configure.MultiEval.Scount.spectrum) exceeding the specified limits, see 'Limits (Spectrum) '. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: out_of_tolerance: float Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:ACP?', suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'Acp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
