from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.average.read() \n
		Returns the values of the RMS magnitude error traces. The values cover a time interval of 500 μs and contain one value
		per chip. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: average_merr: float Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.average.fetch() \n
		Returns the values of the RMS magnitude error traces. The values cover a time interval of 500 μs and contain one value
		per chip. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: average_merr: float Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage?', suppressed)
		return response
