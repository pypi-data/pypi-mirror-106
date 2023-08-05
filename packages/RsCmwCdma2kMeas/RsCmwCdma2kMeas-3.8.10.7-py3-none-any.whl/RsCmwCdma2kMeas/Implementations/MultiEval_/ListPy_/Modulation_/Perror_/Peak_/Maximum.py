from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:PERRor:PEAK:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.perror.peak.maximum.fetch() \n
		Returns peak and RMS phase error (statistical) values for all active list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: perr_peak: float Comma-separated list of values, one per active segment. Range: 0 deg to 180 deg , Unit: deg"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:PERRor:PEAK:MAXimum?', suppressed)
		return response

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: enums.ResultStatus2: decimal See 'Reliability Indicator'.
			- Perr_Peak: List[float]: float Comma-separated list of values, one per active segment. Range: 0 deg to 180 deg , Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Reliability', enums.ResultStatus2),
			ArgStruct('Perr_Peak', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: enums.ResultStatus2 = None
			self.Perr_Peak: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:PERRor:PEAK:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.modulation.perror.peak.maximum.calculate() \n
		Returns peak and RMS phase error (statistical) values for all active list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:PERRor:PEAK:MAXimum?', self.__class__.CalculateStruct())
