from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal
			- Narrow_Band: float: float MS power, measured with a filter bandwidth of 1.23 MHz. Range: -256 dBm to 256 dBm
			- Wideband: float: float MS power, measured with the wideband filter (8 MHz) . Range: -256 dBm to 256 dBm
			- Out_Of_Tolerance: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:CDMA:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Narrow_Band'),
			ArgStruct.scalar_float('Wideband'),
			ArgStruct.scalar_float('Out_Of_Tolerance')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Narrow_Band: float = None
			self.Wideband: float = None
			self.Out_Of_Tolerance: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent \n
		Snippet: value: ResultData = driver.multiEval.acp.current.read() \n
		Returns MS power and the 'out of tolerance' statistical results. For the MS power results, the current, average and
		maximum values can be retrieved. The 'Out of Tolerance' retrieved via the CURRent, AVERage and MAXimum command are
		identical. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent \n
		Snippet: value: ResultData = driver.multiEval.acp.current.fetch() \n
		Returns MS power and the 'out of tolerance' statistical results. For the MS power results, the current, average and
		maximum values can be retrieved. The 'Out of Tolerance' retrieved via the CURRent, AVERage and MAXimum command are
		identical. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal
			- Narrow_Band: float: float MS power, measured with a filter bandwidth of 1.23 MHz. Range: -256 dBm to 256 dBm
			- Wideband: float: float MS power, measured with the wideband filter (8 MHz) . Range: -256 dBm to 256 dBm
			- Out_Of_Tolerance: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (see [CMDLINK: CONFigure:CDMA:MEASi:MEValuation:SCOunt:SPECtrum CMDLINK]) exceeding the specified limits, see 'Limits (Spectrum) '. Range: 0 % to 100 %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Narrow_Band'),
			ArgStruct.scalar_float('Wideband'),
			ArgStruct.scalar_float('Out_Of_Tolerance')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Narrow_Band: float = None
			self.Wideband: float = None
			self.Out_Of_Tolerance: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.acp.current.calculate() \n
		Returns MS power and the 'out of tolerance' statistical results. For the MS power results, the current, average and
		maximum values can be retrieved. The 'Out of Tolerance' retrieved via the CURRent, AVERage and MAXimum command are
		identical. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:ACP:CURRent?', self.__class__.CalculateStruct())
