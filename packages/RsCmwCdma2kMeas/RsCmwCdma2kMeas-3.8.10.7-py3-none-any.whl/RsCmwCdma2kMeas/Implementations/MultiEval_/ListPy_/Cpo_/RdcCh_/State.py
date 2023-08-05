from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.SigChStateA]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RDCCh:STATe \n
		Snippet: value: List[enums.SigChStateA] = driver.multiEval.listPy.cpo.rdcCh.state.fetch() \n
		Returns the state of a particular reverse link channel (R-CCCH, R-DCCH, R-EACH, R-FCH, R-PICH, R-SCH0 - W0102, R-SCH0 -
		W0204) in a channel-related measurement (CP, CPO, CTO) for all active segments. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: rdc_ch: INVisible | ACTive | IACTive | ALIased Comma-separated list of states, one per active segment."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:CPO:RDCCh:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.SigChStateA)
