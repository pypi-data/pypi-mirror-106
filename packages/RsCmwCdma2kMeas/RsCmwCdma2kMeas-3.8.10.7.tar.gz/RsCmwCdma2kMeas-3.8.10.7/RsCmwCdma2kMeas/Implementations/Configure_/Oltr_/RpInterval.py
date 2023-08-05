from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpInterval:
	"""RpInterval commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rpInterval", core, parent)

	def get_time(self) -> float:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval:TIME \n
		Snippet: value: float = driver.configure.oltr.rpInterval.get_time() \n
		Gets the duration of the reference power interval, i.e. the interval that is used to calculate the MS reference power for
		the subsequent power step. \n
			:return: ref_pow_interval: float Range: 5 ms to 40 ms , Unit: ms
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval:TIME?')
		return Conversions.str_to_float(response)

	def get_value(self) -> int:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval \n
		Snippet: value: int = driver.configure.oltr.rpInterval.get_value() \n
		Gets the duration of the reference power interval, i.e. the interval that is used to calculate the MS reference power for
		the subsequent power step. \n
			:return: ref_pow_interval: integer The time as the number of power control groups: from 4 (= 5 ms) to 32 (=40 ms) Range: 4 to 32
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval?')
		return Conversions.str_to_int(response)

	def set_value(self, ref_pow_interval: int) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval \n
		Snippet: driver.configure.oltr.rpInterval.set_value(ref_pow_interval = 1) \n
		Gets the duration of the reference power interval, i.e. the interval that is used to calculate the MS reference power for
		the subsequent power step. \n
			:param ref_pow_interval: integer The time as the number of power control groups: from 4 (= 5 ms) to 32 (=40 ms) Range: 4 to 32
		"""
		param = Conversions.decimal_value_to_str(ref_pow_interval)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:OLTR:RPINterval {param}')
