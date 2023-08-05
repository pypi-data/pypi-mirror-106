from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 17 total commands, 1 Sub-groups, 15 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def acp(self):
		"""acp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_acp'):
			from .Limit_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	# noinspection PyTypeChecker
	class PowerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Min_Power: float or bool: Range: -128 dBm to 50 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Max_Power: float or bool: Range: -128 dBm to 50 dBm, Unit: dBm Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Min_Power'),
			ArgStruct.scalar_float_ext('Max_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Power: float or bool = None
			self.Max_Power: float or bool = None

	def get_power(self) -> PowerStruct:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:POWer \n
		Snippet: value: PowerStruct = driver.configure.multiEval.limit.get_power() \n
		Defines limits for the mobile station (MS) power. \n
			:return: structure: for return value, see the help for PowerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:POWer?', self.__class__.PowerStruct())

	def set_power(self, value: PowerStruct) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:POWer \n
		Snippet: driver.configure.multiEval.limit.set_power(value = PowerStruct()) \n
		Defines limits for the mobile station (MS) power. \n
			:param value: see the help for PowerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:POWer', value)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Evm_Rms: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Evm_Peak: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Evm_Rms'),
			ArgStruct.scalar_float_ext('Evm_Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm_Rms: float or bool = None
			self.Evm_Peak: float or bool = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.multiEval.limit.get_ev_magnitude() \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude \n
		Snippet: driver.configure.multiEval.limit.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) . \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Merr_Rms: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Merr_Peak: float or bool: Range: 0 % to 100 %, Unit: % Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Merr_Rms'),
			ArgStruct.scalar_float_ext('Merr_Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Merr_Rms: float or bool = None
			self.Merr_Peak: float or bool = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.multiEval.limit.get_merror() \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:MERRor \n
		Snippet: driver.configure.multiEval.limit.set_merror(value = MerrorStruct()) \n
		Defines upper limits for the RMS and peak values of the magnitude error. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Perr_Rms: float or bool: Range: 0 deg to 180 deg, Unit: deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
			- Perr_Peak: float or bool: Range: 0 deg to 180 deg, Unit: deg Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Perr_Rms'),
			ArgStruct.scalar_float_ext('Perr_Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Perr_Rms: float or bool = None
			self.Perr_Peak: float or bool = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.multiEval.limit.get_perror() \n
		Defines a symmetric limit for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified value. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:PERRor \n
		Snippet: driver.configure.multiEval.limit.set_perror(value = PerrorStruct()) \n
		Defines a symmetric limit for the RMS and peak values of the phase error. The limit check fails if the absolute value of
		the measured phase error exceeds the specified value. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:PERRor', value)

	def get_iq_offset(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_offset() \n
		Defines an upper limit for the I/Q origin offset (carrier feedthrough) . \n
			:return: iq_offset: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQOFfset?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_offset(self, iq_offset: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.set_iq_offset(iq_offset = 1.0) \n
		Defines an upper limit for the I/Q origin offset (carrier feedthrough) . \n
			:param iq_offset: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_offset)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQOFfset {param}')

	def get_iq_imbalance(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_iq_imbalance() \n
		Defines an upper limit for the I/Q imbalance. \n
			:return: iq_imbalance: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance?')
		return Conversions.str_to_float_or_bool(response)

	def set_iq_imbalance(self, iq_imbalance: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance \n
		Snippet: driver.configure.multiEval.limit.set_iq_imbalance(iq_imbalance = 1.0) \n
		Defines an upper limit for the I/Q imbalance. \n
			:param iq_imbalance: Range: -120 dB to -20 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(iq_imbalance)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:IQIMbalance {param}')

	def get_cf_error(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CFERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cf_error() \n
		Defines an upper limit for the carrier frequency error. \n
			:return: cf_error: Range: 0 Hz to 1000 Hz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CFERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_cf_error(self, cf_error: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CFERror \n
		Snippet: driver.configure.multiEval.limit.set_cf_error(cf_error = 1.0) \n
		Defines an upper limit for the carrier frequency error. \n
			:param cf_error: Range: 0 Hz to 1000 Hz, Unit: Hz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(cf_error)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CFERror {param}')

	def get_tt_error(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:TTERror \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_tt_error() \n
		Defines an upper limit for the transport time error. \n
			:return: tt_error: Range: 0 µs to 10 µs, Unit: µs Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:TTERror?')
		return Conversions.str_to_float_or_bool(response)

	def set_tt_error(self, tt_error: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:TTERror \n
		Snippet: driver.configure.multiEval.limit.set_tt_error(tt_error = 1.0) \n
		Defines an upper limit for the transport time error. \n
			:param tt_error: Range: 0 µs to 10 µs, Unit: µs Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(tt_error)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:TTERror {param}')

	def get_wf_quality(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:WFQuality \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_wf_quality() \n
		Defines a lower limit for the waveform quality. For an ideal transmitter, the waveform quality equals 1. \n
			:return: wf_qual: Range: 0 to 1 Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:WFQuality?')
		return Conversions.str_to_float_or_bool(response)

	def set_wf_quality(self, wf_qual: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:WFQuality \n
		Snippet: driver.configure.multiEval.limit.set_wf_quality(wf_qual = 1.0) \n
		Defines a lower limit for the waveform quality. For an ideal transmitter, the waveform quality equals 1. \n
			:param wf_qual: Range: 0 to 1 Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(wf_qual)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:WFQuality {param}')

	def get_obw(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:OBW \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_obw() \n
		Defines an upper limit for the occupied bandwidth. \n
			:return: limit_obw: Range: 0 MHz to 8 MHz, Unit: MHz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:OBW?')
		return Conversions.str_to_float_or_bool(response)

	def set_obw(self, limit_obw: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:OBW \n
		Snippet: driver.configure.multiEval.limit.set_obw(limit_obw = 1.0) \n
		Defines an upper limit for the occupied bandwidth. \n
			:param limit_obw: Range: 0 MHz to 8 MHz, Unit: MHz Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit_obw)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:OBW {param}')

	def get_cdp(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDP \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cdp() \n
		Defines an upper limit for the code domain power of inactive channels. \n
			:return: limit_cdp: Range: -70 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDP?')
		return Conversions.str_to_float_or_bool(response)

	def set_cdp(self, limit_cdp: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDP \n
		Snippet: driver.configure.multiEval.limit.set_cdp(limit_cdp = 1.0) \n
		Defines an upper limit for the code domain power of inactive channels. \n
			:param limit_cdp: Range: -70 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(limit_cdp)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDP {param}')

	def get_cde(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDE \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cde() \n
		Defines an upper limit for the code domain error. \n
			:return: cdep: Range: -70 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDE?')
		return Conversions.str_to_float_or_bool(response)

	def set_cde(self, cdep: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDE \n
		Snippet: driver.configure.multiEval.limit.set_cde(cdep = 1.0) \n
		Defines an upper limit for the code domain error. \n
			:param cdep: Range: -70 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(cdep)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CDE {param}')

	def get_cp(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CP \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cp() \n
		Defines an upper limit for the channel power. \n
			:return: channel_power: Limit of the channel power. Range: -60 dB to 0 dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CP?')
		return Conversions.str_to_float_or_bool(response)

	def set_cp(self, channel_power: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CP \n
		Snippet: driver.configure.multiEval.limit.set_cp(channel_power = 1.0) \n
		Defines an upper limit for the channel power. \n
			:param channel_power: Limit of the channel power. Range: -60 dB to 0 dB Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(channel_power)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CP {param}')

	def get_cpo(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CPO \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cpo() \n
		Defines an upper limit for the absolute channel phase offset. \n
			:return: ch_phase_offset: Limit for absolute phase offset. Range: 0 mRad to 200 mRad, Unit: mRad Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CPO?')
		return Conversions.str_to_float_or_bool(response)

	def set_cpo(self, ch_phase_offset: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CPO \n
		Snippet: driver.configure.multiEval.limit.set_cpo(ch_phase_offset = 1.0) \n
		Defines an upper limit for the absolute channel phase offset. \n
			:param ch_phase_offset: Limit for absolute phase offset. Range: 0 mRad to 200 mRad, Unit: mRad Additional parameters: OFF | ON (disables the limit check | enables the limit check using the previous/default limit values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(ch_phase_offset)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CPO {param}')

	def get_cto(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CTO \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.get_cto() \n
		Defines the upper limit for the absolute time offset. \n
			:return: ch_time_offset: Limit for absolute time offset in nanoseconds. Range: 0 ns to 40 ns, Unit: ns
		"""
		response = self._core.io.query_str('CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CTO?')
		return Conversions.str_to_float_or_bool(response)

	def set_cto(self, ch_time_offset: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CTO \n
		Snippet: driver.configure.multiEval.limit.set_cto(ch_time_offset = 1.0) \n
		Defines the upper limit for the absolute time offset. \n
			:param ch_time_offset: Limit for absolute time offset in nanoseconds. Range: 0 ns to 40 ns, Unit: ns
		"""
		param = Conversions.decimal_or_bool_value_to_str(ch_time_offset)
		self._core.io.write(f'CONFigure:CDMA:MEASurement<Instance>:MEValuation:LIMit:CTO {param}')

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
