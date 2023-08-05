from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Pich: float: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns
			- Dcch: float: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns
			- Sch_1: float: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Pich'),
			ArgStruct.scalar_float('Dcch'),
			ArgStruct.scalar_float('Sch_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pich: float = None
			self.Dcch: float = None
			self.Sch_1: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.cto.isignal.current.read() \n
		Returns channel time offset for the indicated channels in the in-phase signal path (I-signal) . The results of the
		current, average and maximum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.cto.isignal.current.fetch() \n
		Returns channel time offset for the indicated channels in the in-phase signal path (I-signal) . The results of the
		current, average and maximum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Pich: enums.ResultStatus2: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns
			- Dcch: enums.ResultStatus2: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns
			- Sch_1: enums.ResultStatus2: float Time offset in nanoseconds for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -50 ns to +50ns , Unit: ns"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Pich', enums.ResultStatus2),
			ArgStruct.scalar_enum('Dcch', enums.ResultStatus2),
			ArgStruct.scalar_enum('Sch_1', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Pich: enums.ResultStatus2 = None
			self.Dcch: enums.ResultStatus2 = None
			self.Sch_1: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.trace.cto.isignal.current.calculate() \n
		Returns channel time offset for the indicated channels in the in-phase signal path (I-signal) . The results of the
		current, average and maximum traces can be retrieved. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:CURRent?', self.__class__.CalculateStruct())
