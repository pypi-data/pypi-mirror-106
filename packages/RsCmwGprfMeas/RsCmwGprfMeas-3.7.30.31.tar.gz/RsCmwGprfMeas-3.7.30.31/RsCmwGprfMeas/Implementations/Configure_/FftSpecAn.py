from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSpecAn:
	"""FftSpecAn commands group definition. 10 total commands, 1 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fftSpecAn", core, parent)

	@property
	def peakSearch(self):
		"""peakSearch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_peakSearch'):
			from .FftSpecAn_.PeakSearch import PeakSearch
			self._peakSearch = PeakSearch(self._core, self._base)
		return self._peakSearch

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: value: float = driver.configure.fftSpecAn.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT \n
		Snippet: driver.configure.fftSpecAn.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param tcd_timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:TOUT {param}')

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AveragingMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe \n
		Snippet: value: enums.AveragingMode = driver.configure.fftSpecAn.get_amode() \n
		Selects the averaging mode for the average FFT trace (see method RsCmwGprfMeas.FftSpecAn.Power.Average.read) . \n
			:return: averaging_mode: LINear | LOGarithmic LINear: averaging of linear power values LOGarithmic: averaging of logarithmic (displayed) power values
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AveragingMode)

	def set_amode(self, averaging_mode: enums.AveragingMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe \n
		Snippet: driver.configure.fftSpecAn.set_amode(averaging_mode = enums.AveragingMode.LINear) \n
		Selects the averaging mode for the average FFT trace (see method RsCmwGprfMeas.FftSpecAn.Power.Average.read) . \n
			:param averaging_mode: LINear | LOGarithmic LINear: averaging of linear power values LOGarithmic: averaging of logarithmic (displayed) power values
		"""
		param = Conversions.enum_scalar_to_str(averaging_mode, enums.AveragingMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:AMODe {param}')

	# noinspection PyTypeChecker
	def get_detector(self) -> enums.DetectorBasic:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector \n
		Snippet: value: enums.DetectorBasic = driver.configure.fftSpecAn.get_detector() \n
		Selects the detector for the display of the FFT trace. \n
			:return: detector: PEAK | RMS PEAK: Trace points are calculated from peak values of a set of adjacent raw calculated data. RMS: Trace points are calculated from RMS values.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector?')
		return Conversions.str_to_scalar_enum(response, enums.DetectorBasic)

	def set_detector(self, detector: enums.DetectorBasic) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector \n
		Snippet: driver.configure.fftSpecAn.set_detector(detector = enums.DetectorBasic.PEAK) \n
		Selects the detector for the display of the FFT trace. \n
			:param detector: PEAK | RMS PEAK: Trace points are calculated from peak values of a set of adjacent raw calculated data. RMS: Trace points are calculated from RMS values.
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.DetectorBasic)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:DETector {param}')

	def get_fft_length(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength \n
		Snippet: value: int = driver.configure.fftSpecAn.get_fft_length() \n
		Selects the number of samples (FFT length) that the R&S CMW uses for the FFT analysis. \n
			:return: length: Range: 1024 | 2048 | 4096 | 8192 | 16384 (other values are rounded to the closest possible FFT length)
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength?')
		return Conversions.str_to_int(response)

	def set_fft_length(self, length: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength \n
		Snippet: driver.configure.fftSpecAn.set_fft_length(length = 1) \n
		Selects the number of samples (FFT length) that the R&S CMW uses for the FFT analysis. \n
			:param length: Range: 1024 | 2048 | 4096 | 8192 | 16384 (other values are rounded to the closest possible FFT length)
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FFTLength {param}')

	def get_fspan(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan \n
		Snippet: value: float = driver.configure.fftSpecAn.get_fspan() \n
		Selects the calculated and displayed frequency range (span) of the FFT spectrum analyzer. \n
			:return: frequency_span: Range: 1.25 MHz | 2.5 MHz | 5 MHz | 10 MHz | 20 MHz | 40 MHz | 80 MHz | 160 MHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan?')
		return Conversions.str_to_float(response)

	def set_fspan(self, frequency_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan \n
		Snippet: driver.configure.fftSpecAn.set_fspan(frequency_span = 1.0) \n
		Selects the calculated and displayed frequency range (span) of the FFT spectrum analyzer. \n
			:param frequency_span: Range: 1.25 MHz | 2.5 MHz | 5 MHz | 10 MHz | 20 MHz | 40 MHz | 80 MHz | 160 MHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:FSPan {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception \n
		Snippet: value: bool = driver.configure.fftSpecAn.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception \n
		Snippet: driver.configure.fftSpecAn.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF | ON OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.fftSpecAn.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition \n
		Snippet: driver.configure.fftSpecAn.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt \n
		Snippet: value: int = driver.configure.fftSpecAn.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals. A measurement interval comprises a single power/frequency step (list mode switched off) or a sweep (list mode switched on) . Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt \n
		Snippet: driver.configure.fftSpecAn.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals. A measurement interval comprises a single power/frequency step (list mode switched off) or a sweep (list mode switched on) . Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:SCOunt {param}')

	def clone(self) -> 'FftSpecAn':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FftSpecAn(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
