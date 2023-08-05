from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StCount:
	"""StCount commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("stCount", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:STCount \n
		Snippet: value: List[int] = driver.multiEval.listPy.acp.stCount.fetch() \n
		Returns the statistic count of the spectrum measurement for all active list mode segments. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: statistic_count: decimal Number of evaluated valid slots. Comma-separated list of values, one per active segment. Range: 0 to 1000"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:STCount?', suppressed)
		return response
