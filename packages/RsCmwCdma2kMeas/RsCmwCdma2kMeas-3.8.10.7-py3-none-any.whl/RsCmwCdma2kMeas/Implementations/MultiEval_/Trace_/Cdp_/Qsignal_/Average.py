from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.cdp.qsignal.average.read() \n
		Returns the values of the code domain power (CDP) I-Signal and Q-Signal traces. The results of the current, average,
		maximum and minimum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: cdp_qsig_aver: float The number of results corresponds to the selected spreading factor (method RsCmwCdma2kMeas.Configure.MultiEval.sfactor) , for example 16 results for SF16. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.cdp.qsignal.average.fetch() \n
		Returns the values of the code domain power (CDP) I-Signal and Q-Signal traces. The results of the current, average,
		maximum and minimum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: cdp_qsig_average: float The number of results corresponds to the selected spreading factor (method RsCmwCdma2kMeas.Configure.MultiEval.sfactor) , for example 16 results for SF16. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.cdp.qsignal.average.calculate() \n
		Returns the values of the code domain power (CDP) I-Signal and Q-Signal traces. The results of the current, average,
		maximum and minimum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: cdp_qsig_average: float The number of results corresponds to the selected spreading factor (method RsCmwCdma2kMeas.Configure.MultiEval.sfactor) , for example 16 results for SF16. Range: -70 dB to 0 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CDP:QSIGnal:AVERage?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
