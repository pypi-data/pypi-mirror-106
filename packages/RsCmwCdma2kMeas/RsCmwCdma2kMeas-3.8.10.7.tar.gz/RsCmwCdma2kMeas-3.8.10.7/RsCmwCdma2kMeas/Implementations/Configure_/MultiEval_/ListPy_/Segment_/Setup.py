from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: integer Number of measured power control groups (slots) in the segment. The sum of the segment lengths must not exceed 10000 slots; limit violation is indicated by a reliability indicator of 2 (capture buffer overflow) . Range: 1 to 1000
			- Level: float: numeric Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - user margin The input power range is stated in the data sheet.
			- Frequency: float: numeric Center frequency of the RF analyzer. Range: 100 MHz to 6 GHz , Unit: Hz
			- Retrigger_Option: enums.RetriggerOption: OFF | ON | IFPower | IFPSync Enables or disables the trigger system to start segment measurement. Note: For the first segment (no = 1) the setting of this parameter is ignored, since the general MELM measurement starts with the measurement of the first segment. That means, with the first trigger event the first segment is always measured. OFF: Disables the retrigger. The segment measurement is started by the first trigger event. ON: Enables the retrigger. The list mode measurement continues only if a new event for this segment is triggered (retrigger) . IFPower: Waits for the power ramp of the received bursts before measuring the segment. IFPSync: Before measuring the next segment, the R&S CMW waits for the power ramp of the received bursts and tries to synchronize to a slot boundary after the trigger event.
			- Rconfig: enums.Rconfig: R12Q | R36H | R3Q Selects the radio configuration which determines, for example, the modulation type. Note that if RetriggerOption=OFF for all segments (i.e. in 'trigger once' mode) , the radio configuration is inherited from the multi-evaluation measurement (see [CMDLINK: CONFigure:CDMA:MEASi:RCONfig CMDLINK]) , ignoring the RConfig values specified for the individual segments. R12Q: RC1 or 2 (O-QPSK) R36H: RC3 to 6 (H-PSK) R3Q: RC3 (QPSK)
			- Cmws_Connector: enums.CmwsConnector: Optional setting parameter. Optional parameter, as alternative to the command [CMDLINK: CONFigure:CDMA:MEASi:MEValuation:LIST:SEGMentno:CMWS:CONNector CMDLINK]"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_enum('Retrigger_Option', enums.RetriggerOption),
			ArgStruct.scalar_enum('Rconfig', enums.Rconfig),
			ArgStruct.scalar_enum('Cmws_Connector', enums.CmwsConnector)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Frequency: float = None
			self.Retrigger_Option: enums.RetriggerOption = None
			self.Rconfig: enums.Rconfig = None
			self.Cmws_Connector: enums.CmwsConnector = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.multiEval.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the length of segment <no> and the analyzer settings. In general, this command must be sent for all segments
		measured. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length of segment <no> and the analyzer settings. In general, this command must be sent for all segments
		measured. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
