from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: Hz
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINK: CONFigure:CDMA:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified limit, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Out_Of_Tol_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw: float = None
			self.Out_Of_Tol_Count: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage \n
		Snippet: value: ResultData = driver.multiEval.obw.average.read() \n
		Return the current, average and maximum occupied bandwidth value results. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage \n
		Snippet: value: ResultData = driver.multiEval.obw.average.fetch() \n
		Return the current, average and maximum occupied bandwidth value results. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: Hz
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINK: CONFigure:CDMA:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified limit, see 'Limits (Spectrum) '. Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Obw'),
			ArgStruct.scalar_float('Out_Of_Tol_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Obw: float = None
			self.Out_Of_Tol_Count: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.obw.average.calculate() \n
		Return the current, average and maximum occupied bandwidth value results. The values described below are returned by
		FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:OBW:AVERage?', self.__class__.CalculateStruct())
