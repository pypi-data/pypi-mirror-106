from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSpecAn:
	"""FftSpecAn commands group definition. 9 total commands, 1 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fftSpecAn", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .FftSpecAn_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	# noinspection PyTypeChecker
	def get_omode(self) -> enums.OffsetMode:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe \n
		Snippet: value: enums.OffsetMode = driver.trigger.fftSpecAn.get_omode() \n
		Selects a fixed or a variable trigger offset. In the FFT spectrum analyzer measurement, the trigger offset defines the
		center of the FFT window. \n
			:return: offset_mode: VARiable | FIXed VARiable Trigger offset defined via method RsCmwGprfMeas.Trigger.FftSpecAn.osStop. FIXed Trigger offset defined via method RsCmwGprfMeas.Trigger.FftSpecAn.offset.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.OffsetMode)

	def set_omode(self, offset_mode: enums.OffsetMode) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe \n
		Snippet: driver.trigger.fftSpecAn.set_omode(offset_mode = enums.OffsetMode.FIXed) \n
		Selects a fixed or a variable trigger offset. In the FFT spectrum analyzer measurement, the trigger offset defines the
		center of the FFT window. \n
			:param offset_mode: VARiable | FIXed VARiable Trigger offset defined via method RsCmwGprfMeas.Trigger.FftSpecAn.osStop. FIXed Trigger offset defined via method RsCmwGprfMeas.Trigger.FftSpecAn.offset.
		"""
		param = Conversions.enum_scalar_to_str(offset_mode, enums.OffsetMode)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OMODe {param}')

	# noinspection PyTypeChecker
	class OsStopStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Offset_Start: float: Must be smaller than the stop value. Range: -0.15 s to 0.15 s, Unit: s
			- Offset_Stop: float: Must be larger than the start value. Range: -0.15 s to 0.15 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_Start'),
			ArgStruct.scalar_float('Offset_Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_Start: float = None
			self.Offset_Stop: float = None

	def get_os_stop(self) -> OsStopStruct:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OSSTop \n
		Snippet: value: OsStopStruct = driver.trigger.fftSpecAn.get_os_stop() \n
		Defines the start and stop time for the variable trigger offset, see method RsCmwGprfMeas.Trigger.FftSpecAn.omode. \n
			:return: structure: for return value, see the help for OsStopStruct structure arguments.
		"""
		return self._core.io.query_struct('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OSSTop?', self.__class__.OsStopStruct())

	def set_os_stop(self, value: OsStopStruct) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OSSTop \n
		Snippet: driver.trigger.fftSpecAn.set_os_stop(value = OsStopStruct()) \n
		Defines the start and stop time for the variable trigger offset, see method RsCmwGprfMeas.Trigger.FftSpecAn.omode. \n
			:param value: see the help for OsStopStruct structure arguments.
		"""
		self._core.io.write_struct('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OSSTop', value)

	def get_source(self) -> str:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce \n
		Snippet: value: str = driver.trigger.fftSpecAn.get_source() \n
		Selects the source of the trigger events. Some values are always available in this firmware application. They are listed
		below. Depending on the installed options, additional values are available. A complete list of all supported values can
		be displayed using TRIGger:...:CATalog:SOURce?. \n
			:return: source: 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce \n
		Snippet: driver.trigger.fftSpecAn.set_source(source = '1') \n
		Selects the source of the trigger events. Some values are always available in this firmware application. They are listed
		below. Depending on the installed options, additional values are available. A complete list of all supported values can
		be displayed using TRIGger:...:CATalog:SOURce?. \n
			:param source: 'IF Power': IF power trigger 'Free Run': free run (untriggered)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SOURce {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: minimum_gap: Range: 0 s to 0.01 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, minimum_gap: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP \n
		Snippet: driver.trigger.fftSpecAn.set_mgap(minimum_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param minimum_gap: Range: 0 s to 0.01 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(minimum_gap)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:MGAP {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: value: float or bool = driver.trigger.fftSpecAn.get_timeout() \n
		Selects the maximum time that the R&S CMW waits for a trigger event before it stops the measurement in remote control
		mode or indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: timeout: Range: 0.01 s to 300 s, Unit: s Additional values: OFF | ON (disables | enables the timeout check) .
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: driver.trigger.fftSpecAn.set_timeout(timeout = 1.0) \n
		Selects the maximum time that the R&S CMW waits for a trigger event before it stops the measurement in remote control
		mode or indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param timeout: Range: 0.01 s to 300 s, Unit: s Additional values: OFF | ON (disables | enables the timeout check) .
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT {param}')

	def get_offset(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_offset() \n
		Defines the fixed trigger offset, see method RsCmwGprfMeas.Trigger.FftSpecAn.omode. \n
			:return: offset: Range: -0.15 s to 0.15 s, Unit: s
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet \n
		Snippet: driver.trigger.fftSpecAn.set_offset(offset = 1.0) \n
		Defines the fixed trigger offset, see method RsCmwGprfMeas.Trigger.FftSpecAn.omode. \n
			:param offset: Range: -0.15 s to 0.15 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:OFFSet {param}')

	def get_threshold(self) -> float:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold \n
		Snippet: value: float = driver.trigger.fftSpecAn.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold \n
		Snippet: driver.trigger.fftSpecAn.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation)
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlopeExt:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe \n
		Snippet: value: enums.SignalSlopeExt = driver.trigger.fftSpecAn.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		response = self._core.io.query_str('TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlopeExt)

	def set_slope(self, event: enums.SignalSlopeExt) -> None:
		"""SCPI: TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe \n
		Snippet: driver.trigger.fftSpecAn.set_slope(event = enums.SignalSlopeExt.FALLing) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param event: REDGe | FEDGe REDGe: rising edge FEDGe: falling edge
		"""
		param = Conversions.enum_scalar_to_str(event, enums.SignalSlopeExt)
		self._core.io.write(f'TRIGger:GPRF:MEASurement<Instance>:FFTSanalyzer:SLOPe {param}')

	def clone(self) -> 'FftSpecAn':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftSpecAn(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
