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
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:STATe \n
		Snippet: value: List[enums.SigChStateA] = driver.multiEval.trace.cto.isignal.state.fetch() \n
		Return the states of the channel time offset (CTO) I-Signal and Q-Signal bar graphs. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: cto_isig_ch_state: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:TRACe:CTO:ISIGnal:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.SigChStateA)
