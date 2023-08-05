from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.obw.current.read() \n
		Returns the traces of the current occupied bandwidth (OBW) . The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_obw: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.obw.current.fetch() \n
		Returns the traces of the current occupied bandwidth (OBW) . The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_obw: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.trace.obw.current.calculate() \n
		Returns the traces of the current occupied bandwidth (OBW) . The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: curr_obw: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:OBW:CURRent?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
