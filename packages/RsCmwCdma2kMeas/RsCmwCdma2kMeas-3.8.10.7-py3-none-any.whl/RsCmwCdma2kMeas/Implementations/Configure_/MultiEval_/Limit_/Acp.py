from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acp:
	"""Acp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acp", core, parent)

	def get_relative(self) -> List[float or bool]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP[:RELative] \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.limit.acp.get_relative() \n
		Defines limits for the ACP in dBc at the individual offset frequencies (set via method RsCmwCdma2kMeas.Configure.
		MultiEval.Acp.foffsets) . \n
			:return: limit_acp: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:RELative?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_relative(self, limit_acp: List[float or bool]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP[:RELative] \n
		Snippet: driver.configure.multiEval.limit.acp.set_relative(limit_acp = [1.1, True, 2.2, False, 3.3]) \n
		Defines limits for the ACP in dBc at the individual offset frequencies (set via method RsCmwCdma2kMeas.Configure.
		MultiEval.Acp.foffsets) . \n
			:param limit_acp: numeric Range: -80 dBc to 10 dBc , Unit: dBc Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.list_to_csv_str(limit_acp)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:RELative {param}')

	def get_absolute(self) -> List[float or bool]:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:ABSolute \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.limit.acp.get_absolute() \n
		Defines limits for the ACP in dBm at the individual offset frequencies (set via method RsCmwCdma2kMeas.Configure.
		MultiEval.Acp.foffsets) . \n
			:return: limit_acp: numeric Range: -80 dBm to 10 dBm , Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:ABSolute?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_absolute(self, limit_acp: List[float or bool]) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:ABSolute \n
		Snippet: driver.configure.multiEval.limit.acp.set_absolute(limit_acp = [1.1, True, 2.2, False, 3.3]) \n
		Defines limits for the ACP in dBm at the individual offset frequencies (set via method RsCmwCdma2kMeas.Configure.
		MultiEval.Acp.foffsets) . \n
			:param limit_acp: numeric Range: -80 dBm to 10 dBm , Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.list_to_csv_str(limit_acp)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:ACP:ABSolute {param}')
