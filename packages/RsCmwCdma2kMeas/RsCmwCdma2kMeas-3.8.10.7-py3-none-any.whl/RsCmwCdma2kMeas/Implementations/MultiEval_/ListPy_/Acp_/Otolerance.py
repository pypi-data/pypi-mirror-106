from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Otolerance:
	"""Otolerance commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("otolerance", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:OTOLerance \n
		Snippet: value: List[int] = driver.multiEval.listPy.acp.otolerance.fetch() \n
		Returns the out of tolerance percentages in the adjacent channel power measurement for all active list mode segments. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: out_of_tol_count: decimal The percentage of measurement intervals of the statistic count exceeding the specified limits. Comma-separated list of values, one per active segment. Range: 0 % to 100 % , Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:OTOLerance?', suppressed)
		return response
