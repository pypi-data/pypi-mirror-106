from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Seg_Reliability: int: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated. Range: 0 | 3 | 4 | 8
			- Rpi_Ch: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased INVisible: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rdc_Ch: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rcc_Ch: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rea_Ch: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rfch: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rsch_0_W_02_E_04: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rsch_0_W_01_E_02: enums.SigChStateA: INVisible | ACTive | IACTive | ALIased
			- Rsch_1_W_06_E_08: enums.SigChStateA: For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: enums.SigChStateA: For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Rpi_Ch', enums.SigChStateA),
			ArgStruct.scalar_enum('Rdc_Ch', enums.SigChStateA),
			ArgStruct.scalar_enum('Rcc_Ch', enums.SigChStateA),
			ArgStruct.scalar_enum('Rea_Ch', enums.SigChStateA),
			ArgStruct.scalar_enum('Rfch', enums.SigChStateA),
			ArgStruct.scalar_enum('Rsch_0_W_02_E_04', enums.SigChStateA),
			ArgStruct.scalar_enum('Rsch_0_W_01_E_02', enums.SigChStateA),
			ArgStruct.scalar_enum('Rsch_1_W_06_E_08', enums.SigChStateA),
			ArgStruct.scalar_enum('Rsch_1_W_02_E_04', enums.SigChStateA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Rpi_Ch: enums.SigChStateA = None
			self.Rdc_Ch: enums.SigChStateA = None
			self.Rcc_Ch: enums.SigChStateA = None
			self.Rea_Ch: enums.SigChStateA = None
			self.Rfch: enums.SigChStateA = None
			self.Rsch_0_W_02_E_04: enums.SigChStateA = None
			self.Rsch_0_W_01_E_02: enums.SigChStateA = None
			self.Rsch_1_W_06_E_08: enums.SigChStateA = None
			self.Rsch_1_W_02_E_04: enums.SigChStateA = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:CP:STATe \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.cp.state.fetch(segment = repcap.Segment.Default) \n
		Return the states of the channels for power measurement (CP) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:CP:STATe?', self.__class__.FetchStruct())
