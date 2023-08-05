from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rpi_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rdc_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rcc_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rea_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rfch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_0_W_02_E_04: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_0_W_01_E_02: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_1_W_06_E_08: List[float]: float For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: List[float]: float For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rpi_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rdc_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rcc_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rea_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rfch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_0_W_02_E_04', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_0_W_01_E_02', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_1_W_06_E_08', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_1_W_02_E_04', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Rpi_Ch: List[float] = None
			self.Rdc_Ch: List[float] = None
			self.Rcc_Ch: List[float] = None
			self.Rea_Ch: List[float] = None
			self.Rfch: List[float] = None
			self.Rsch_0_W_02_E_04: List[float] = None
			self.Rsch_0_W_01_E_02: List[float] = None
			self.Rsch_1_W_06_E_08: List[float] = None
			self.Rsch_1_W_02_E_04: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:AVERage \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.cp.average.fetch() \n
		Returns channel power (CP) results for all active segments in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum calculation and to enable the calculation
		of the results, use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The values
		described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...
		}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.count. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:AVERage?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rpi_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rdc_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rcc_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rea_Ch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rfch: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_0_W_02_E_04: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_0_W_01_E_02: List[float]: float RMS channel power values for the indicated channels. Range: -60 dB to 0 dB (SDEViation 0 dB to 60 dB) , Unit: dB
			- Rsch_1_W_06_E_08: List[float]: float For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: List[float]: float For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rpi_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rdc_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rcc_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rea_Ch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rfch', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_0_W_02_E_04', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_0_W_01_E_02', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_1_W_06_E_08', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rsch_1_W_02_E_04', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Rpi_Ch: List[float] = None
			self.Rdc_Ch: List[float] = None
			self.Rcc_Ch: List[float] = None
			self.Rea_Ch: List[float] = None
			self.Rfch: List[float] = None
			self.Rsch_0_W_02_E_04: List[float] = None
			self.Rsch_0_W_01_E_02: List[float] = None
			self.Rsch_1_W_06_E_08: List[float] = None
			self.Rsch_1_W_02_E_04: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.cp.average.calculate() \n
		Returns channel power (CP) results for all active segments in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum calculation and to enable the calculation
		of the results, use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The values
		described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The values listed below in curly brackets {} are returned for each active segment: {...}seg 1, {...
		}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.count. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:AVERage?', self.__class__.CalculateStruct())
