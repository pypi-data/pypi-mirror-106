from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


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
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Evm_Rms: float: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Merr_Rms: float: float Magnitude error RMS value. Range: 0 % to 100 %, Unit: %
			- Merr_Peak: float: float Magnitude error peak value. Range: -100 % to +100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Perr_Rms: float: float Phase error RMS value. Range: 0 deg to 180 deg , Unit: deg
			- Perr_Peak: float: float Phase error peak value. Range: -180 deg to 180 deg (AVERage: 0 deg to 180 deg, SDEViation: 0 deg to 90 deg) , Unit: deg
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB , Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB , Unit: dB
			- Cfreq_Error: float: float Carrier frequency error Range: -5000 Hz to 5000 Hz , Unit: Hz
			- Trans_Time_Err: float: float Transmit time error Range: -100 µs to 100 µs, Unit: µs
			- Ms_Power_1_M_23: float: No parameter help available
			- Ms_Power_Wideband: float: No parameter help available
			- Wav_Quality: float: float Waveform quality Range: 0 to 1
			- Wav_Qual_Max_Pow: float: No parameter help available
			- Wav_Qual_Min_Power: float: No parameter help available
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: int: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Merr_Rms'),
			ArgStruct.scalar_float('Merr_Peak'),
			ArgStruct.scalar_float('Perr_Rms'),
			ArgStruct.scalar_float('Perr_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Cfreq_Error'),
			ArgStruct.scalar_float('Trans_Time_Err'),
			ArgStruct.scalar_float('Ms_Power_1_M_23'),
			ArgStruct.scalar_float('Ms_Power_Wideband'),
			ArgStruct.scalar_float('Wav_Quality'),
			ArgStruct.scalar_float('Wav_Qual_Max_Pow'),
			ArgStruct.scalar_float('Wav_Qual_Min_Power'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_int('Cur_Stat_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Merr_Rms: float = None
			self.Merr_Peak: float = None
			self.Perr_Rms: float = None
			self.Perr_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Cfreq_Error: float = None
			self.Trans_Time_Err: float = None
			self.Ms_Power_1_M_23: float = None
			self.Ms_Power_Wideband: float = None
			self.Wav_Quality: float = None
			self.Wav_Qual_Max_Pow: float = None
			self.Wav_Qual_Min_Power: float = None
			self.Out_Of_Tol_Count: float = None
			self.Cur_Stat_Count: int = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.current.fetch(segment = repcap.Segment.Default) \n
		Returns modulation single value results for segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enable the
		calculation of the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The
		ranges indicated below apply to all results except standard deviation results. The minimum for standard deviation results
		equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Evm_Rms: float: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value. Range: 0 % to 100 %, Unit: %
			- Merr_Rms: float: float Magnitude error RMS value. Range: 0 % to 100 %, Unit: %
			- Merr_Peak: float: float Magnitude error peak value. Range: -100 % to +100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Perr_Rms: float: float Phase error RMS value. Range: 0 deg to 180 deg , Unit: deg
			- Perr_Peak: float: float Phase error peak value. Range: -180 deg to 180 deg (AVERage: 0 deg to 180 deg, SDEViation: 0 deg to 90 deg) , Unit: deg
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB , Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB , Unit: dB
			- Cfreq_Error: float: float Carrier frequency error Range: -5000 Hz to 5000 Hz , Unit: Hz
			- Trans_Time_Err: float: float Transmit time error Range: -100 µs to 100 µs, Unit: µs
			- Ms_Power_1_M_23: float: No parameter help available
			- Ms_Power_Wideband: float: No parameter help available
			- Wav_Quality: float: float Waveform quality Range: 0 to 1
			- Wav_Qual_Max_Pow: float: No parameter help available
			- Wav_Qual_Min_Power: float: No parameter help available
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: float: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Merr_Rms'),
			ArgStruct.scalar_float('Merr_Peak'),
			ArgStruct.scalar_float('Perr_Rms'),
			ArgStruct.scalar_float('Perr_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Cfreq_Error'),
			ArgStruct.scalar_float('Trans_Time_Err'),
			ArgStruct.scalar_float('Ms_Power_1_M_23'),
			ArgStruct.scalar_float('Ms_Power_Wideband'),
			ArgStruct.scalar_float('Wav_Quality'),
			ArgStruct.scalar_float('Wav_Qual_Max_Pow'),
			ArgStruct.scalar_float('Wav_Qual_Min_Power'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Cur_Stat_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Merr_Rms: float = None
			self.Merr_Peak: float = None
			self.Perr_Rms: float = None
			self.Perr_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Cfreq_Error: float = None
			self.Trans_Time_Err: float = None
			self.Ms_Power_1_M_23: float = None
			self.Ms_Power_Wideband: float = None
			self.Wav_Quality: float = None
			self.Wav_Qual_Max_Pow: float = None
			self.Wav_Qual_Min_Power: float = None
			self.Out_Of_Tol_Count: float = None
			self.Cur_Stat_Count: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.modulation.current.calculate(segment = repcap.Segment.Default) \n
		Returns modulation single value results for segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum and SDEViation calculation and enable the
		calculation of the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set. The
		ranges indicated below apply to all results except standard deviation results. The minimum for standard deviation results
		equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:CURRent?', self.__class__.CalculateStruct())
