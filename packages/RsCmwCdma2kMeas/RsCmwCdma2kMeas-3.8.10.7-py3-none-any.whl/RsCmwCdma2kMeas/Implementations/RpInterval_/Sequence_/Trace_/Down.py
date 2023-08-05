from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Down:
	"""Down commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("down", core, parent)

	def read(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:RPINterval:SEQuence<Sequence>:TRACe:DOWN \n
		Snippet: value: List[float] = driver.rpInterval.sequence.trace.down.read(sequence = repcap.Sequence.Default) \n
		Returns the values of the reference power traces. For each sequence, UP/DOWN commands return the results of the reference
		power interval for the power up/down step. See method RsCmwCdma2kMeas.Configure.Oltr.RpInterval.time) . \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:RPINterval:SEQuence{sequence_cmd_val}:TRACe:DOWN?', suppressed)
		return response

	def fetch(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:RPINterval:SEQuence<Sequence>:TRACe:DOWN \n
		Snippet: value: List[float] = driver.rpInterval.sequence.trace.down.fetch(sequence = repcap.Sequence.Default) \n
		Returns the values of the reference power traces. For each sequence, UP/DOWN commands return the results of the reference
		power interval for the power up/down step. See method RsCmwCdma2kMeas.Configure.Oltr.RpInterval.time) . \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: down_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:RPINterval:SEQuence{sequence_cmd_val}:TRACe:DOWN?', suppressed)
		return response
