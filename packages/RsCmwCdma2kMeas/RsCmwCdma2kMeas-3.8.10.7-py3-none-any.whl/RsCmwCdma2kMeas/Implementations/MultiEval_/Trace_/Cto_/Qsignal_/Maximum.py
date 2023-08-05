from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Fch: float: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Sch_0: float: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Each: float: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Ccch: float: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Fch'),
			ArgStruct.scalar_float('Sch_0'),
			ArgStruct.scalar_float('Each'),
			ArgStruct.scalar_float('Ccch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Fch: float = None
			self.Sch_0: float = None
			self.Each: float = None
			self.Ccch: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.trace.cto.qsignal.maximum.read() \n
		Returns the values of the channel time offset Q-Signal traces. The results of the current, average and maximum traces can
		be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum \n
		Snippet: value: ResultData = driver.multiEval.trace.cto.qsignal.maximum.fetch() \n
		Returns the values of the channel time offset Q-Signal traces. The results of the current, average and maximum traces can
		be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Fch: enums.ResultStatus2: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Sch_0: enums.ResultStatus2: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Each: enums.ResultStatus2: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns
			- Ccch: enums.ResultStatus2: float Time offset in nanoseconds for reverse fundamental channel, reverse supplemental channel 0, enhanced access channel and reverse common control channel. Range: - 50 ns to + 50 ns , Unit: ns"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Fch', enums.ResultStatus2),
			ArgStruct.scalar_enum('Sch_0', enums.ResultStatus2),
			ArgStruct.scalar_enum('Each', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ccch', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Fch: enums.ResultStatus2 = None
			self.Sch_0: enums.ResultStatus2 = None
			self.Each: enums.ResultStatus2 = None
			self.Ccch: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.trace.cto.qsignal.maximum.calculate() \n
		Returns the values of the channel time offset Q-Signal traces. The results of the current, average and maximum traces can
		be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit check
		results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:QSIGnal:MAXimum?', self.__class__.CalculateStruct())
