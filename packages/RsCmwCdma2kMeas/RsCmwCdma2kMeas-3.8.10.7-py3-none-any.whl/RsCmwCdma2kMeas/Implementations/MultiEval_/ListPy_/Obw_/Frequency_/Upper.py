from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("upper", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:FREQuency:UPPer \n
		Snippet: value: List[float] = driver.multiEval.listPy.obw.frequency.upper.fetch() \n
		Returns lower and upper OBW frequencies for all active list mode segments. The values are taken from the 'CURRent'
		measurement. The values described below are returned by FETCh commands. CALCulate commands return limit check results
		instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: obw_upper: float Comma-separated list of values, one per active segment. Range: 0 Hz to 100 Hz, Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:FREQuency:UPPer?', suppressed)
		return response
