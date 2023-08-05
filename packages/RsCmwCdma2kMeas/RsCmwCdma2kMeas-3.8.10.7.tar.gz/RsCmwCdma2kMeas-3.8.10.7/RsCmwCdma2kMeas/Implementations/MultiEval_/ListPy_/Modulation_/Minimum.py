from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Evm_Rms: List[float]: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Evm_Peak: List[float]: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Merr_Rms: List[float]: float Magnitude error RMS value. Range: 0 % to 100 %, Unit: %
			- Merr_Peak: List[float]: float Magnitude error peak value. Range: -100 % to +100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Perr_Rms: List[float]: float Phase error RMS value. Range: 0 deg to 180 deg , Unit: deg
			- Perr_Peak: List[float]: float Phase error peak value. Range: -180 deg to 180 deg (AVERage: 0 deg to 180 deg, SDEViation: 0 deg to 90 deg) , Unit: deg
			- Iq_Offset: List[float]: float I/Q origin offset Range: -100 dB to 0 dB , Unit: dB
			- Iq_Imbalance: List[float]: float I/Q imbalance Range: -100 dB to 0 dB , Unit: dB
			- Cfreq_Error: List[float]: float Carrier frequency error Range: -5000 Hz to 5000 Hz , Unit: Hz
			- Trans_Time_Err: List[float]: float Transmit time error Range: -100 µs to 100 µs, Unit: µs
			- Ms_Power_1_M_23: List[float]: No parameter help available
			- Ms_Power_Wideband: List[float]: No parameter help available
			- Wav_Quality: List[float]: float Waveform quality Range: 0 to 1
			- Wav_Qual_Max_Pow: List[float]: No parameter help available
			- Wav_Qual_Min_Power: List[float]: No parameter help available
			- Out_Of_Tol_Count: List[float]: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: List[int]: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Merr_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Merr_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Perr_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Perr_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Imbalance', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cfreq_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Trans_Time_Err', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_1_M_23', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Wideband', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Quality', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Qual_Max_Pow', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Qual_Min_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Evm_Rms: List[float] = None
			self.Evm_Peak: List[float] = None
			self.Merr_Rms: List[float] = None
			self.Merr_Peak: List[float] = None
			self.Perr_Rms: List[float] = None
			self.Perr_Peak: List[float] = None
			self.Iq_Offset: List[float] = None
			self.Iq_Imbalance: List[float] = None
			self.Cfreq_Error: List[float] = None
			self.Trans_Time_Err: List[float] = None
			self.Ms_Power_1_M_23: List[float] = None
			self.Ms_Power_Wideband: List[float] = None
			self.Wav_Quality: List[float] = None
			self.Wav_Qual_Max_Pow: List[float] = None
			self.Wav_Qual_Min_Power: List[float] = None
			self.Out_Of_Tol_Count: List[float] = None
			self.Cur_Stat_Count: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:MINimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.modulation.minimum.fetch() \n
		Returns modulation single value results in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.value) .
		To define the statistical length for AVERage, MAXimum, MINimum and SDEviation calculation and to enable the calculation
		of the results, use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The ranges
		indicated below apply to all results except standard deviation results. The minimum for standard deviation results equals
		0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. The values listed below in curly brackets {} are returned for each active segment: {..
		.}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.count. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:MINimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Evm_Rms: List[float]: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Evm_Peak: List[float]: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Merr_Rms: List[float]: float Magnitude error RMS value. Range: 0 % to 100 %, Unit: %
			- Merr_Peak: List[float]: float Magnitude error peak value. Range: -100 % to +100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Perr_Rms: List[float]: float Phase error RMS value. Range: 0 deg to 180 deg , Unit: deg
			- Perr_Peak: List[float]: float Phase error peak value. Range: -180 deg to 180 deg (AVERage: 0 deg to 180 deg, SDEViation: 0 deg to 90 deg) , Unit: deg
			- Iq_Offset: List[float]: float I/Q origin offset Range: -100 dB to 0 dB , Unit: dB
			- Iq_Imbalance: List[float]: float I/Q imbalance Range: -100 dB to 0 dB , Unit: dB
			- Cfreq_Error: List[float]: float Carrier frequency error Range: -5000 Hz to 5000 Hz , Unit: Hz
			- Trans_Time_Err: List[float]: float Transmit time error Range: -100 µs to 100 µs, Unit: µs
			- Ms_Power_1_M_23: List[float]: No parameter help available
			- Ms_Power_Wideband: List[float]: No parameter help available
			- Wav_Quality: List[float]: float Waveform quality Range: 0 to 1
			- Wav_Qual_Max_Pow: List[float]: No parameter help available
			- Wav_Qual_Min_Power: List[float]: No parameter help available
			- Out_Of_Tol_Count: List[float]: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: List[float]: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Merr_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Merr_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Perr_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Perr_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Imbalance', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cfreq_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Trans_Time_Err', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_1_M_23', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ms_Power_Wideband', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Quality', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Qual_Max_Pow', DataType.FloatList, None, False, True, 1),
			ArgStruct('Wav_Qual_Min_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Out_Of_Tol_Count', DataType.FloatList, None, False, True, 1),
			ArgStruct('Cur_Stat_Count', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Evm_Rms: List[float] = None
			self.Evm_Peak: List[float] = None
			self.Merr_Rms: List[float] = None
			self.Merr_Peak: List[float] = None
			self.Perr_Rms: List[float] = None
			self.Perr_Peak: List[float] = None
			self.Iq_Offset: List[float] = None
			self.Iq_Imbalance: List[float] = None
			self.Cfreq_Error: List[float] = None
			self.Trans_Time_Err: List[float] = None
			self.Ms_Power_1_M_23: List[float] = None
			self.Ms_Power_Wideband: List[float] = None
			self.Wav_Quality: List[float] = None
			self.Wav_Qual_Max_Pow: List[float] = None
			self.Wav_Qual_Min_Power: List[float] = None
			self.Out_Of_Tol_Count: List[float] = None
			self.Cur_Stat_Count: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:MINimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.modulation.minimum.calculate() \n
		Returns modulation single value results in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.value) .
		To define the statistical length for AVERage, MAXimum, MINimum and SDEviation calculation and to enable the calculation
		of the results, use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The ranges
		indicated below apply to all results except standard deviation results. The minimum for standard deviation results equals
		0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. The values listed below in curly brackets {} are returned for each active segment: {..
		.}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined by method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.count. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:MODulation:MINimum?', self.__class__.CalculateStruct())
