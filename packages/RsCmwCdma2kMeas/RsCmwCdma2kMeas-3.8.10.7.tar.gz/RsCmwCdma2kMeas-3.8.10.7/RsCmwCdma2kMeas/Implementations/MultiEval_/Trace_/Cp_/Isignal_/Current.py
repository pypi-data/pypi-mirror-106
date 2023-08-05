from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


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
			- Pich: float: float RMS channel power values for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -60 dB to 0 dB , Unit: dB
			- Dcch: float: float RMS channel power values for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -60 dB to 0 dB , Unit: dB
			- Sch_1: float: float RMS channel power values for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -60 dB to 0 dB , Unit: dB"""
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
		"""SCPI: READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.cp.isignal.current.read() \n
		Returns the values of the channel power I-Signal traces. The results of the current, average, maximum and minimum traces
		can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.cp.isignal.current.fetch() \n
		Returns the values of the channel power I-Signal traces. The results of the current, average, maximum and minimum traces
		can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliabiltiy: float: No parameter help available
			- Pich: float: float RMS channel power values for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -60 dB to 0 dB , Unit: dB
			- Dcch: float: float RMS channel power values for reverse pilot channel, reverse dedicated control channel and reverse supplemental channel 0. Range: -60 dB to 0 dB , Unit: dB
			- Sch_1: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Reliabiltiy'),
			ArgStruct.scalar_float('Pich'),
			ArgStruct.scalar_float('Dcch'),
			ArgStruct.scalar_float('Sch_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliabiltiy: float = None
			self.Pich: float = None
			self.Dcch: float = None
			self.Sch_1: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.trace.cp.isignal.current.calculate() \n
		Returns the values of the channel power I-Signal traces. The results of the current, average, maximum and minimum traces
		can be retrieved. The values described below are returned by FETCh and READ commands. CALCulate commands return limit
		check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:TRACe:CP:ISIGnal:CURRent?', self.__class__.CalculateStruct())
