from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Up:
	"""Up commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("up", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_state'):
			from .Up_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def read(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: READ:CDMA:MEASurement<Instance>:OLTR:SEQuence<Sequence>:TRACe:UP \n
		Snippet: value: List[float] = driver.oltr.sequence.trace.up.read(sequence = repcap.Sequence.Default) \n
		Returns the values of the OLTR traces. For each sequence, UP/DOWN commands return the results of the 100 ms interval
		following the power up/down step. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: up_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:CDMA:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:UP?', suppressed)
		return response

	def fetch(self, sequence=repcap.Sequence.Default) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:OLTR:SEQuence<Sequence>:TRACe:UP \n
		Snippet: value: List[float] = driver.oltr.sequence.trace.up.fetch(sequence = repcap.Sequence.Default) \n
		Returns the values of the OLTR traces. For each sequence, UP/DOWN commands return the results of the 100 ms interval
		following the power up/down step. The values described below are returned by FETCh and READ commands. CALCulate commands
		return limit check results instead, one value for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param sequence: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequence')
			:return: up_power: No help available"""
		sequence_cmd_val = self._base.get_repcap_cmd_value(sequence, repcap.Sequence)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:OLTR:SEQuence{sequence_cmd_val}:TRACe:UP?', suppressed)
		return response

	def clone(self) -> 'Up':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Up(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
