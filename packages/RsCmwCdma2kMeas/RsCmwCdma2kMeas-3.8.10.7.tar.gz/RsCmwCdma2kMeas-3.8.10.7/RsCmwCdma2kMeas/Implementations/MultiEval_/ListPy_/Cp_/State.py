from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'. In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal The segment reliability indicates whether one of the following exceptions occurred in this segment: 0: No error 3: Signal overflow 4: Signal low 8: Synchronization error If a combination of exceptions occurs, the most severe error is indicated. Range: 0 | 3 | 4 | 8
			- Rpi_Ch: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rdc_Ch: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rcc_Ch: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rea_Ch: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rfch: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rsch_0_W_02_E_04: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rsch_0_W_01_E_02: List[enums.SigChStateA]: INVisible | ACTive | IACTive INV: No channel available ACTive: Active channel IACtive: Inactive channel ALIased: Aliased channel
			- Rsch_1_W_06_E_08: List[enums.SigChStateA]: float For future use - returned value not relevant.
			- Rsch_1_W_02_E_04: List[enums.SigChStateA]: float For future use - returned value not relevant."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Rpi_Ch', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rdc_Ch', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rcc_Ch', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rea_Ch', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rfch', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rsch_0_W_02_E_04', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rsch_0_W_01_E_02', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rsch_1_W_06_E_08', DataType.EnumList, enums.SigChStateA, False, True, 1),
			ArgStruct('Rsch_1_W_02_E_04', DataType.EnumList, enums.SigChStateA, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Rpi_Ch: List[enums.SigChStateA] = None
			self.Rdc_Ch: List[enums.SigChStateA] = None
			self.Rcc_Ch: List[enums.SigChStateA] = None
			self.Rea_Ch: List[enums.SigChStateA] = None
			self.Rfch: List[enums.SigChStateA] = None
			self.Rsch_0_W_02_E_04: List[enums.SigChStateA] = None
			self.Rsch_0_W_01_E_02: List[enums.SigChStateA] = None
			self.Rsch_1_W_06_E_08: List[enums.SigChStateA] = None
			self.Rsch_1_W_02_E_04: List[enums.SigChStateA] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:STATe \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.cp.state.fetch() \n
		Return the states of the channels for power measurement (CP) . The values listed below in curly brackets {} are returned
		for each active segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The number of active segments n is determined by method
		RsCmwCdma2kMeas.Configure.MultiEval.ListPy.count. The number to the left of each result parameter is provided for easy
		identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CP:STATe?', self.__class__.FetchStruct())
