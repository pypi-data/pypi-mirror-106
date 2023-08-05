from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Std_Dev_Acp: List[float]: No parameter help available
			- Ms_Power_Wide: float: No parameter help available
			- Ms_Power_Narrow: float: No parameter help available
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: int: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct('Std_Dev_Acp', DataType.FloatList, None, False, False, 41),
			ArgStruct.scalar_float('Ms_Power_Wide'),
			ArgStruct.scalar_float('Ms_Power_Narrow'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_int('Cur_Stat_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Std_Dev_Acp: List[float] = None
			self.Ms_Power_Wide: float = None
			self.Ms_Power_Narrow: float = None
			self.Out_Of_Tol_Count: float = None
			self.Cur_Stat_Count: int = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:ACP:EXTended:SDEViation \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.acp.extended.standardDev.fetch(segment = repcap.Segment.Default) \n
		Returns the adjacent channel power (ACP) results for segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.value) . If enabled the wideband power and narrowband power results are returned, too. To define the
		statistical length for AVERage, MINimum, MAXimum and SDEviation calculation and enable the calculation of the results use
		the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below.
		The number to the left of each result parameter is provided for easy identification of the parameter position within the
		result array. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACP:EXTended:SDEViation?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: 0 | 3 | 4 | 8 The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated.
			- Std_Dev_Acp: List[enums.ResultStatus2]: No parameter help available
			- Ms_Power_Wide: float: No parameter help available
			- Ms_Power_Narrow: float: No parameter help available
			- Out_Of_Tol_Count: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count (CONFigure:CDMA:MEASi:MEValuation:SCOunt: MODulation) exceeding the specified limits. Range: 0 % to 100 % , Unit: %
			- Cur_Stat_Count: float: decimal Number of evaluated valid slots in this segment. Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct('Std_Dev_Acp', DataType.EnumList, enums.ResultStatus2, False, False, 41),
			ArgStruct.scalar_float('Ms_Power_Wide'),
			ArgStruct.scalar_float('Ms_Power_Narrow'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Cur_Stat_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Std_Dev_Acp: List[enums.ResultStatus2] = None
			self.Ms_Power_Wide: float = None
			self.Ms_Power_Narrow: float = None
			self.Out_Of_Tol_Count: float = None
			self.Cur_Stat_Count: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:ACP:EXTended:SDEViation \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.acp.extended.standardDev.calculate(segment = repcap.Segment.Default) \n
		Returns the adjacent channel power (ACP) results for segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.value) . If enabled the wideband power and narrowband power results are returned, too. To define the
		statistical length for AVERage, MINimum, MAXimum and SDEviation calculation and enable the calculation of the results use
		the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below.
		The number to the left of each result parameter is provided for easy identification of the parameter position within the
		result array. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:ACP:EXTended:SDEViation?', self.__class__.CalculateStruct())
