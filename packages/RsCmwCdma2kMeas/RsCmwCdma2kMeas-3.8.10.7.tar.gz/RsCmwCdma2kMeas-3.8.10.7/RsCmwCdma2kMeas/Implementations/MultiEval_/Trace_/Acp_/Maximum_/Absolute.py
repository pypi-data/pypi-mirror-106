from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute \n
		Snippet: value: List[float] = driver.multiEval.trace.acp.maximum.absolute.read() \n
		Returns the absolute adjacent channel power measured at a series of frequencies. The frequencies are determined by the
		offset values defined via the command method RsCmwCdma2kMeas.Configure.MultiEval.Acp.foffsets. All defined offset values
		are considered (irrespective of their activation status) . The current, average and maximum traces can be retrieved. The
		number to the left of each result parameter is provided for easy identification of the parameter position within the
		result array. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: maximum_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute \n
		Snippet: value: List[float] = driver.multiEval.trace.acp.maximum.absolute.fetch() \n
		Returns the absolute adjacent channel power measured at a series of frequencies. The frequencies are determined by the
		offset values defined via the command method RsCmwCdma2kMeas.Configure.MultiEval.Acp.foffsets. All defined offset values
		are considered (irrespective of their activation status) . The current, average and maximum traces can be retrieved. The
		number to the left of each result parameter is provided for easy identification of the parameter position within the
		result array. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: maximum_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.acp.maximum.absolute.calculate() \n
		Returns the absolute adjacent channel power measured at a series of frequencies. The frequencies are determined by the
		offset values defined via the command method RsCmwCdma2kMeas.Configure.MultiEval.Acp.foffsets. All defined offset values
		are considered (irrespective of their activation status) . The current, average and maximum traces can be retrieved. The
		number to the left of each result parameter is provided for easy identification of the parameter position within the
		result array. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: maximum_acp: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:ACP:MAXimum:ABSolute?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
