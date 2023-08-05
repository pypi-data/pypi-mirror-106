from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Acpm_10: List[float]: No parameter help available
			- Acpm_9: List[float]: No parameter help available
			- Acpm_8: List[float]: No parameter help available
			- Acpm_7: List[float]: No parameter help available
			- Acpm_6: List[float]: No parameter help available
			- Acpm_5: List[float]: No parameter help available
			- Acpm_4: List[float]: No parameter help available
			- Acpm_3: List[float]: No parameter help available
			- Acpm_2: List[float]: No parameter help available
			- Acpm_1: List[float]: No parameter help available
			- Acp_Carrier: List[float]: float ACP M/P n refers to the average channel power at the carrier frequency minus/plus the frequency offset value number n. Range: -100 dB to 50 dB , Unit: dB
			- Acpp_1: List[float]: No parameter help available
			- Acpp_2: List[float]: No parameter help available
			- Acpp_3: List[float]: No parameter help available
			- Acpp_4: List[float]: No parameter help available
			- Acpp_5: List[float]: No parameter help available
			- Acpp_6: List[float]: No parameter help available
			- Acpp_7: List[float]: No parameter help available
			- Acpp_8: List[float]: No parameter help available
			- Acpp_9: List[float]: No parameter help available
			- Acpp_10: List[float]: No parameter help available
			- Ms_Power_Wide: List[float]: float Results of the wideband (8 MHz) power measurement. Range: -55 dBm to 42 dBm , Unit: dBm
			- Ms_Power_Narrow: List[float]: float Results of the narrowband (1.23 MHz) power measurement. Range: -55 dBm to 42 dBm , Unit: dBm
			- Out_Of_Tol_Count: List[float]: decimal Out of tolerance result, i.e. percentage of measurement intervals of the statistic count exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: List[int]: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Acpm_10', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_9', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_8', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_7', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_6', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_5', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_4', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_3', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpm_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acp_Carrier', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_3', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_4', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_5', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_6', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_7', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_8', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_9', DataType.FloatList, None, False, True, 1),
			ArgStruct('Acpp_10', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Wide', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Narrow', DataType.FloatList, None, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Acpm_10: List[float] = None
			self.Acpm_9: List[float] = None
			self.Acpm_8: List[float] = None
			self.Acpm_7: List[float] = None
			self.Acpm_6: List[float] = None
			self.Acpm_5: List[float] = None
			self.Acpm_4: List[float] = None
			self.Acpm_3: List[float] = None
			self.Acpm_2: List[float] = None
			self.Acpm_1: List[float] = None
			self.Acp_Carrier: List[float] = None
			self.Acpp_1: List[float] = None
			self.Acpp_2: List[float] = None
			self.Acpp_3: List[float] = None
			self.Acpp_4: List[float] = None
			self.Acpp_5: List[float] = None
			self.Acpp_6: List[float] = None
			self.Acpp_7: List[float] = None
			self.Acpp_8: List[float] = None
			self.Acpp_9: List[float] = None
			self.Acpp_10: List[float] = None
			self.Ms_Power_Wide: List[float] = None
			self.Ms_Power_Narrow: List[float] = None
			self.Out_Of_Tol_Count: List[float] = None
			self.Cur_Stat_Count: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.acp.maximum.fetch() \n
		Returns the adjacent channel power (ACP) results of each active segment (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . If enabled the wideband power and narrowband power results are returned, too. To define the statistical
		length for AVERage, SDEviation, MINimum and MAXimum calculation and to enable the calculation of the results, use the
		command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set. The values described below are returned
		by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below.
		The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg
		n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.count. The number
		to the left of each result parameter is provided for easy identification of the parameter position within the result
		array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:MAXimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Acpm_10: List[enums.ResultStatus2]: No parameter help available
			- Acpm_9: List[enums.ResultStatus2]: No parameter help available
			- Acpm_8: List[enums.ResultStatus2]: No parameter help available
			- Acpm_7: List[enums.ResultStatus2]: No parameter help available
			- Acpm_6: List[enums.ResultStatus2]: No parameter help available
			- Acpm_5: List[enums.ResultStatus2]: No parameter help available
			- Acpm_4: List[enums.ResultStatus2]: No parameter help available
			- Acpm_3: List[enums.ResultStatus2]: No parameter help available
			- Acpm_2: List[enums.ResultStatus2]: No parameter help available
			- Acpm_1: List[enums.ResultStatus2]: No parameter help available
			- Acp_Carrier: List[enums.ResultStatus2]: float ACP M/P n refers to the average channel power at the carrier frequency minus/plus the frequency offset value number n. Range: -100 dB to 50 dB , Unit: dB
			- Acpp_1: List[enums.ResultStatus2]: No parameter help available
			- Acpp_2: List[enums.ResultStatus2]: No parameter help available
			- Acpp_3: List[enums.ResultStatus2]: No parameter help available
			- Acpp_4: List[enums.ResultStatus2]: No parameter help available
			- Acpp_5: List[enums.ResultStatus2]: No parameter help available
			- Acpp_6: List[enums.ResultStatus2]: No parameter help available
			- Acpp_7: List[enums.ResultStatus2]: No parameter help available
			- Acpp_8: List[enums.ResultStatus2]: No parameter help available
			- Acpp_9: List[enums.ResultStatus2]: No parameter help available
			- Acpp_10: List[enums.ResultStatus2]: No parameter help available
			- Ms_Power_Wide: List[float]: float Results of the wideband (8 MHz) power measurement. Range: -55 dBm to 42 dBm , Unit: dBm
			- Ms_Power_Narrow: List[float]: float Results of the narrowband (1.23 MHz) power measurement. Range: -55 dBm to 42 dBm , Unit: dBm
			- Out_Of_Tol_Count: List[float]: decimal Out of tolerance result, i.e. percentage of measurement intervals of the statistic count exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: List[float]: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Acpm_10', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_9', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_8', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_7', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_6', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_5', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_4', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_3', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_2', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpm_1', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acp_Carrier', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_1', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_2', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_3', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_4', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_5', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_6', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_7', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_8', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_9', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Acpp_10', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Ms_Power_Wide', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Narrow', DataType.FloatList, None, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Acpm_10: List[enums.ResultStatus2] = None
			self.Acpm_9: List[enums.ResultStatus2] = None
			self.Acpm_8: List[enums.ResultStatus2] = None
			self.Acpm_7: List[enums.ResultStatus2] = None
			self.Acpm_6: List[enums.ResultStatus2] = None
			self.Acpm_5: List[enums.ResultStatus2] = None
			self.Acpm_4: List[enums.ResultStatus2] = None
			self.Acpm_3: List[enums.ResultStatus2] = None
			self.Acpm_2: List[enums.ResultStatus2] = None
			self.Acpm_1: List[enums.ResultStatus2] = None
			self.Acp_Carrier: List[enums.ResultStatus2] = None
			self.Acpp_1: List[enums.ResultStatus2] = None
			self.Acpp_2: List[enums.ResultStatus2] = None
			self.Acpp_3: List[enums.ResultStatus2] = None
			self.Acpp_4: List[enums.ResultStatus2] = None
			self.Acpp_5: List[enums.ResultStatus2] = None
			self.Acpp_6: List[enums.ResultStatus2] = None
			self.Acpp_7: List[enums.ResultStatus2] = None
			self.Acpp_8: List[enums.ResultStatus2] = None
			self.Acpp_9: List[enums.ResultStatus2] = None
			self.Acpp_10: List[enums.ResultStatus2] = None
			self.Ms_Power_Wide: List[float] = None
			self.Ms_Power_Narrow: List[float] = None
			self.Out_Of_Tol_Count: List[float] = None
			self.Cur_Stat_Count: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.acp.maximum.calculate() \n
		Returns the adjacent channel power (ACP) results of each active segment (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . If enabled the wideband power and narrowband power results are returned, too. To define the statistical
		length for AVERage, SDEviation, MINimum and MAXimum calculation and to enable the calculation of the results, use the
		command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set. The values described below are returned
		by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below.
		The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg
		n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.count. The number
		to the left of each result parameter is provided for easy identification of the parameter position within the result
		array. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:MAXimum?', self.__class__.CalculateStruct())
