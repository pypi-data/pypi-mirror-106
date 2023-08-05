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
			- Rpi_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rdc_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rcc_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rea_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rfch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_0_W_02_E_04: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_0_W_01_E_02: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_1_W_06_E_08: float: float For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: float: float For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Rpi_Ch'),
			ArgStruct.scalar_float('Rdc_Ch'),
			ArgStruct.scalar_float('Rcc_Ch'),
			ArgStruct.scalar_float('Rea_Ch'),
			ArgStruct.scalar_float('Rfch'),
			ArgStruct.scalar_float('Rsch_0_W_02_E_04'),
			ArgStruct.scalar_float('Rsch_0_W_01_E_02'),
			ArgStruct.scalar_float('Rsch_1_W_06_E_08'),
			ArgStruct.scalar_float('Rsch_1_W_02_E_04')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Rpi_Ch: float = None
			self.Rdc_Ch: float = None
			self.Rcc_Ch: float = None
			self.Rea_Ch: float = None
			self.Rfch: float = None
			self.Rsch_0_W_02_E_04: float = None
			self.Rsch_0_W_01_E_02: float = None
			self.Rsch_1_W_06_E_08: float = None
			self.Rsch_1_W_02_E_04: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CP:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.cp.current.fetch(segment = repcap.Segment.Default) \n
		Returns channel power (CP) results for the segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum calculation and enable the calculation of
		the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Rpi_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rdc_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rcc_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rea_Ch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rfch: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_0_W_02_E_04: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_0_W_01_E_02: float: float RMS channel power values for the indicated channels. Range: -25 dB to 0 dB (SDEViation 0 dB to 25 dB) Unit: dB
			- Rsch_1_W_06_E_08: float: float For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: float: float For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Rpi_Ch'),
			ArgStruct.scalar_float('Rdc_Ch'),
			ArgStruct.scalar_float('Rcc_Ch'),
			ArgStruct.scalar_float('Rea_Ch'),
			ArgStruct.scalar_float('Rfch'),
			ArgStruct.scalar_float('Rsch_0_W_02_E_04'),
			ArgStruct.scalar_float('Rsch_0_W_01_E_02'),
			ArgStruct.scalar_float('Rsch_1_W_06_E_08'),
			ArgStruct.scalar_float('Rsch_1_W_02_E_04')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Rpi_Ch: float = None
			self.Rdc_Ch: float = None
			self.Rcc_Ch: float = None
			self.Rea_Ch: float = None
			self.Rfch: float = None
			self.Rsch_0_W_02_E_04: float = None
			self.Rsch_0_W_01_E_02: float = None
			self.Rsch_1_W_06_E_08: float = None
			self.Rsch_1_W_02_E_04: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CP:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.cp.current.calculate(segment = repcap.Segment.Default) \n
		Returns channel power (CP) results for the segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.MultiEval.
		ListPy.value) . To define the statistical length for AVERage, MAXimum, MINimum calculation and enable the calculation of
		the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Modulation.set.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:CURRent?', self.__class__.CalculateStruct())
