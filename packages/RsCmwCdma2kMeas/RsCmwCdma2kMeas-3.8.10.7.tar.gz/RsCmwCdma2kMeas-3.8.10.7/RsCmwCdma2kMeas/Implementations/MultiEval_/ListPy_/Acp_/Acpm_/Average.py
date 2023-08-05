from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self, acpMinus=repcap.AcpMinus.Default) -> List[float]:
		"""SCPI: FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:ACPM<freqpoint>:AVERage \n
		Snippet: value: List[float] = driver.multiEval.listPy.acp.acpm.average.fetch(acpMinus = repcap.AcpMinus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±10 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpMinus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpm')
			:return: acpm: No help available"""
		acpMinus_cmd_val = self._base.get_repcap_cmd_value(acpMinus, repcap.AcpMinus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:ACPM{acpMinus_cmd_val}:AVERage?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, acpMinus=repcap.AcpMinus.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:ACPM<freqpoint>:AVERage \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.listPy.acp.acpm.average.calculate(acpMinus = repcap.AcpMinus.Default) \n
		Returns adjacent channel power (statistical) values for the selected off-center channels and all active list mode
		segments. The mnemonic ACPM refers to the channels in the 'minus' direction, the mnemonic ACPP to the channels in the
		'plus' direction relative to the current channel. The offset is selected with the <freqpoint> suffix (±10 channels) . The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Use RsCmwCdma2kMeas.reliability.last_value to read the updated reliability indicator. \n
			:param acpMinus: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Acpm')
			:return: acpm: No help available"""
		acpMinus_cmd_val = self._base.get_repcap_cmd_value(acpMinus, repcap.AcpMinus)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:CDMA:MEASurement<Instance>:MEValuation:LIST:ACP:ACPM{acpMinus_cmd_val}:AVERage?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)
