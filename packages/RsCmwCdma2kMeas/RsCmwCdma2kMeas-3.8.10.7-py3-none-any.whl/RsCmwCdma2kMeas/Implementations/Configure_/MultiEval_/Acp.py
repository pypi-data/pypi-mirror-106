from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extended'):
			from .Acp_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	def get_foffsets(self) -> List[float or bool]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:FOFFsets \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.acp.get_foffsets() \n
		Defines the frequency offsets to be used for ACP measurements. The offsets are defined relative to the analyzer frequency.
		Up to 10 offsets can be defined and enabled. \n
			:return: frequency_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:FOFFsets?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_foffsets(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:FOFFsets \n
		Snippet: driver.configure.multiEval.acp.set_foffsets(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the frequency offsets to be used for ACP measurements. The offsets are defined relative to the analyzer frequency.
		Up to 10 offsets can be defined and enabled. \n
			:param frequency_offset: numeric | OFF | ON Range: 0 MHz to 4 MHz, Unit: MHz Additional parameters: OFF | ON (disables the offset | enables the offset using the previous defined value)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:FOFFsets {param}')

	# noinspection PyTypeChecker
	def get_rbw(self) -> List[enums.Rbw]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:RBW \n
		Snippet: value: List[enums.Rbw] = driver.configure.multiEval.acp.get_rbw() \n
		Defines the resolution bandwidth to be used for the upper and lower frequency offsets 0 to 9 of ACP measurements. \n
			:return: rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:RBW?')
		return Conversions.str_to_list_enum(response, enums.Rbw)

	def set_rbw(self, rbw: List[enums.Rbw]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:RBW \n
		Snippet: driver.configure.multiEval.acp.set_rbw(rbw = [Rbw.F100k, Rbw.F6K25]) \n
		Defines the resolution bandwidth to be used for the upper and lower frequency offsets 0 to 9 of ACP measurements. \n
			:param rbw: F1K0 | F6K25 | F10K | F12K5 | F25K | F30K | F50K | F100k | F1M0 | F1M23 F1K0: 1 kHz F6K25: 6.25 kHz F10K: 10 kHz F12K5: 12.5 kHz F25K: 25 kHz F30K: 30 kHz F50K: 50 kHz F100k: 100 kHz F1M0: 1 MHz F1M23: 1.23 MHz
		"""
		param = Conversions.enum_list_to_str(rbw, enums.Rbw)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:ACP:RBW {param}')

	def clone(self) -> 'Acp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Acp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
