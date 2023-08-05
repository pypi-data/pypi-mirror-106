from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmw:
	"""SingleCmw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("singleCmw", core, parent)

	# noinspection PyTypeChecker
	def get_cmode(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:CMWS:CMODe \n
		Snippet: value: enums.ParameterSetMode = driver.configure.multiEval.listPy.singleCmw.get_cmode() \n
		Specifies how the input connector is selected for CDMA2000 list mode measurements with the R&S CMWS. \n
			:return: cmws_connector_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:CMWS:CMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_cmode(self, cmws_connector_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:CMWS:CMODe \n
		Snippet: driver.configure.multiEval.listPy.singleCmw.set_cmode(cmws_connector_mode = enums.ParameterSetMode.GLOBal) \n
		Specifies how the input connector is selected for CDMA2000 list mode measurements with the R&S CMWS. \n
			:param cmws_connector_mode: GLOBal | LIST GLOBal: The same input connector is used for all segments. It is selected in the same way as without list mode, for example via ROUTe:CDMA:MEASi:SCENario:SALone. LIST: The input connector is configured individually for each segment. See method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.SingleCmw.Connector.set or method RsCmwCdma2kMeas.Configure.MultiEval.ListPy.Segment.Setup.set.
		"""
		param = Conversions.enum_scalar_to_str(cmws_connector_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:CMWS:CMODe {param}')
