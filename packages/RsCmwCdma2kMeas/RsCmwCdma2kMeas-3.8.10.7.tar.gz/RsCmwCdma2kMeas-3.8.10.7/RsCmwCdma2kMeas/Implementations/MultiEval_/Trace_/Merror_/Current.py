from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.current.read() \n
		Returns the values of the RMS magnitude error traces. The values cover a time interval of 500 μs and contain one value
		per chip. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: current_merr: float Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent?', suppressed)
		return response

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Relaibiltiy: int: No parameter help available
			- Current_Merr: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Relaibiltiy'),
			ArgStruct('Current_Merr', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Relaibiltiy: int = None
			self.Current_Merr: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.trace.merror.current.fetch() \n
		Returns the values of the RMS magnitude error traces. The values cover a time interval of 500 μs and contain one value
		per chip. The results of the current, average and maximum traces can be retrieved. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:MERRor:CURRent?', self.__class__.FetchStruct())
