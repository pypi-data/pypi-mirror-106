from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scount", core, parent)

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.multiEval.scount.get_modulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: scount_mod: numeric Number of measurement intervals. Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, scount_mod: int) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: driver.configure.multiEval.scount.set_modulation(scount_mod = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param scount_mod: numeric Number of measurement intervals. Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(scount_mod)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:MODulation {param}')

	def get_spectrum(self) -> int:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum \n
		Snippet: value: int = driver.configure.multiEval.scount.get_spectrum() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: scount_spectrum: numeric Number of measurement intervals. Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum?')
		return Conversions.str_to_int(response)

	def set_spectrum(self, scount_spectrum: int) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum \n
		Snippet: driver.configure.multiEval.scount.set_spectrum(scount_spectrum = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param scount_spectrum: numeric Number of measurement intervals. Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(scount_spectrum)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:SCOunt:SPECtrum {param}')
