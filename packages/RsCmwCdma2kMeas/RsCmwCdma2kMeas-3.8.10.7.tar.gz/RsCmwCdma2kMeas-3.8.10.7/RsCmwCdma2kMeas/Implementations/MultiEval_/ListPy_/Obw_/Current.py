from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: List[float]: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: MHz
			- Lower_Freq: List[float]: float Lower frequency of the occupied bandwidth. Range: -8 MHz to 0 MHz , Unit: MHz
			- Upper_Freq: List[float]: float Upper frequency of the occupied bandwidth. Range: 0 MHz to 8 MHz , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Obw', DataType.FloatList, None, False, True, 1),
			ArgStruct('Lower_Freq', DataType.FloatList, None, False, True, 1),
			ArgStruct('Upper_Freq', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Obw: List[float] = None
			self.Lower_Freq: List[float] = None
			self.Upper_Freq: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.obw.current.fetch() \n
		Returns CURrent occupied bandwidth (OBW) results for all active segments in list mode (see method RsCmwCdma2kMeas.
		Configure.MultiEval.ListPy.value) . The values described below are returned by FETCh commands. CALCulate commands return
		limit check results instead, one value for each result listed below. The values listed below in curly brackets {} are
		returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined
		by method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.count. The number to the left of each result parameter is provided
		for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Obw: List[float]: float Occupied bandwidth Range: 0 MHz to 8 MHz , Unit: MHz
			- Lower_Freq: List[enums.ResultStatus2]: float Lower frequency of the occupied bandwidth. Range: -8 MHz to 0 MHz , Unit: MHz
			- Upper_Freq: List[enums.ResultStatus2]: float Upper frequency of the occupied bandwidth. Range: 0 MHz to 8 MHz , Unit: MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Obw', DataType.FloatList, None, False, True, 1),
			ArgStruct('Lower_Freq', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Upper_Freq', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Obw: List[float] = None
			self.Lower_Freq: List[enums.ResultStatus2] = None
			self.Upper_Freq: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.obw.current.calculate() \n
		Returns CURrent occupied bandwidth (OBW) results for all active segments in list mode (see method RsCmwCdma2kMeas.
		Configure.MultiEval.ListPy.value) . The values described below are returned by FETCh commands. CALCulate commands return
		limit check results instead, one value for each result listed below. The values listed below in curly brackets {} are
		returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined
		by method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.count. The number to the left of each result parameter is provided
		for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:OBW:CURRent?', self.__class__.CalculateStruct())
