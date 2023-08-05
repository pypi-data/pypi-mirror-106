from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def read(self, sequence=repcap.Sequence.Default) -> List[enums.StatePower]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:OLTR:SEQuence<Sequence>:TRACe:DOWN:STATe \n
		Snippet: value: List[enums.StatePower] = driver.oltr.sequence.trace.down.state.read(sequence = repcap.Sequence.Default) \n
		For each sequence, state commands return limit violation results 'State Down/Up Power' in 20 equidistant parts of the 100
		ms interval following the power down/up step. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: state_down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:CDMA:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:DOWN:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.StatePower)

	# noinspection PyTypeChecker
	def fetch(self, sequence=repcap.Sequence.Default) -> List[enums.StatePower]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:OLTR:SEQuence<Sequence>:TRACe:DOWN:STATe \n
		Snippet: value: List[enums.StatePower] = driver.oltr.sequence.trace.down.state.fetch(sequence = repcap.Sequence.Default) \n
		For each sequence, state commands return limit violation results 'State Down/Up Power' in 20 equidistant parts of the 100
		ms interval following the power down/up step. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: state_down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:DOWN:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.StatePower)

	# noinspection PyTypeChecker
	def calculate(self, sequence=repcap.Sequence.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:OLTR:SEQuence<Sequence>:TRACe:DOWN:STATe \n
		Snippet: value: List[enums.ResultStatus2] = driver.oltr.sequence.trace.down.state.calculate(sequence = repcap.Sequence.Default) \n
		For each sequence, state commands return limit violation results 'State Down/Up Power' in 20 equidistant parts of the 100
		ms interval following the power down/up step. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: state_down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:DOWN:STATe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
