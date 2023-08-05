from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extended:
	"""Extended commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extended", core, parent)

	def get_foffsets(self) -> List[float or bool]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.acp.extended.get_foffsets() \n
		Defines the frequency offsets to be used for extended ACP measurements. The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. \n
			:return: frequency_offset: Range: 0 MHz to 4 MHz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_foffsets(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets \n
		Snippet: driver.configure.multiEval.acp.extended.set_foffsets(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the frequency offsets to be used for extended ACP measurements. The offsets are defined relative to the analyzer
		frequency. Up to 20 offsets can be defined and enabled. \n
			:param frequency_offset: Range: 0 MHz to 4 MHz Additional parameters: OFF | ON (disables | enables the offset)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:FOFFsets {param}')

	# noinspection PyTypeChecker
	def get_rbw(self) -> List[enums.Rbw]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:RBW \n
		Snippet: value: List[enums.Rbw] = driver.configure.multiEval.acp.extended.get_rbw() \n
		Defines the resolution bandwidth to be used for the upper and lower frequency offsets 0 to 19 of extended ACP
		measurements. \n
			:return: rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:RBW?')
		return Conversions.str_to_list_enum(response, enums.Rbw)

	def set_rbw(self, rbw: List[enums.Rbw]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:RBW \n
		Snippet: driver.configure.multiEval.acp.extended.set_rbw(rbw = [Rbw.F100k, Rbw.F6K25]) \n
		Defines the resolution bandwidth to be used for the upper and lower frequency offsets 0 to 19 of extended ACP
		measurements. \n
			:param rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz
		"""
		param = Conversions.enum_list_to_str(rbw, enums.Rbw)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:EXTended:RBW {param}')
