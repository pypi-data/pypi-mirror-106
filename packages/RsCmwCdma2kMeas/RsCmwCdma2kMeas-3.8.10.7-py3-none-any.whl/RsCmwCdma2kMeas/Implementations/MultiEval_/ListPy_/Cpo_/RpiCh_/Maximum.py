from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RPICh:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.cpo.rpiCh.maximum.fetch() \n
		Returns the phase offset (statistical values) of the reverse pilot channel for all active list mode segments. The values
		described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: rpi_ch: float Comma-separated list of values, one per active segment. Range: –180 deg to +180 deg"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RPICh:MAXimum?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RPICh:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.listPy.cpo.rpiCh.maximum.calculate() \n
		Returns the phase offset (statistical values) of the reverse pilot channel for all active list mode segments. The values
		described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: rpi_ch: float Comma-separated list of values, one per active segment. Range: –180 deg to +180 deg"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RPICh:MAXimum?', suppressed)
		return response
