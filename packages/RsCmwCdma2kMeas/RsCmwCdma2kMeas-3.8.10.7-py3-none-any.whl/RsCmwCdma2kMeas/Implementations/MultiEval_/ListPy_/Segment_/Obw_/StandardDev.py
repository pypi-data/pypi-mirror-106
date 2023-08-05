from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


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
			- Seg_Reliability: int: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated. Range: 0 | 3 | 4 | 8
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 8 MHz (SDEViation 0 MHz to 4MHz) , Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:OBW:SDEViation \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.obw.standardDev.fetch(segment = repcap.Segment.Default) \n
		Returns occupied bandwidth (OBW) results for the segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.value) . To define the statistical length for AVERage, MAXimum and SDEviation calculation and to enable
		the calculation of the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set.
		The ranges indicated below apply to all results except standard deviation results. The minimum for standard deviation
		results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:SDEViation?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated. Range: 0 | 3 | 4 | 8
			- Obw: float: float Occupied bandwidth Range: 0 MHz to 8 MHz (SDEViation 0 MHz to 4MHz) , Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Obw')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Obw: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:OBW:SDEViation \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.obw.standardDev.calculate(segment = repcap.Segment.Default) \n
		Returns occupied bandwidth (OBW) results for the segment <no> in list mode (see method RsCmwCdma2kMeas.Configure.
		MultiEval.ListPy.value) . To define the statistical length for AVERage, MAXimum and SDEviation calculation and to enable
		the calculation of the results use the command method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Spectrum.set.
		The ranges indicated below apply to all results except standard deviation results. The minimum for standard deviation
		results equals 0. The maximum equals the width of the indicated range divided by two. Exceptions are explicitly stated.
		The values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one
		value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:OBW:SDEViation?', self.__class__.CalculateStruct())
