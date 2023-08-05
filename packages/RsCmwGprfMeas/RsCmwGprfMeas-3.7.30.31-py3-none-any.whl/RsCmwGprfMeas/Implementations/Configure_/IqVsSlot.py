from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqVsSlot:
	"""IqVsSlot commands group definition. 19 total commands, 2 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqVsSlot", core, parent)

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .IqVsSlot_.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	@property
	def listPy(self):
		"""listPy commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_listPy'):
			from .IqVsSlot_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: value: float = driver.configure.iqVsSlot.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT \n
		Snippet: driver.configure.iqVsSlot.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.iqVsSlot.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition \n
		Snippet: driver.configure.iqVsSlot.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt \n
		Snippet: value: int = driver.configure.iqVsSlot.get_scount() \n
		Defines the number of measurement steps per subsweep. The total number of steps, i.e. the step count times the number of
		subsweeps, must not exceed 3000 (see method RsCmwGprfMeas.Configure.IqVsSlot.ListPy.count) . \n
			:return: step_count: Range: 1 to 3000
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, step_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt \n
		Snippet: driver.configure.iqVsSlot.set_scount(step_count = 1) \n
		Defines the number of measurement steps per subsweep. The total number of steps, i.e. the step count times the number of
		subsweeps, must not exceed 3000 (see method RsCmwGprfMeas.Configure.IqVsSlot.ListPy.count) . \n
			:param step_count: Range: 1 to 3000
		"""
		param = Conversions.decimal_value_to_str(step_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SCOunt {param}')

	def get_mlength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth \n
		Snippet: value: float = driver.configure.iqVsSlot.get_mlength() \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the I/Q vs. slot results for each
		measurement step. \n
			:return: meas_length: Range: 10E-6 s to 1 ms, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth?')
		return Conversions.str_to_float(response)

	def set_mlength(self, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth \n
		Snippet: driver.configure.iqVsSlot.set_mlength(meas_length = 1.0) \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the I/Q vs. slot results for each
		measurement step. \n
			:param meas_length: Range: 10E-6 s to 1 ms, Unit: s
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:MLENgth {param}')

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth \n
		Snippet: value: float = driver.configure.iqVsSlot.get_slength() \n
		Selects the time between the beginning of two consecutive measurement steps. \n
			:return: step_length: Range: 50E-6 s to 5E-3 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth \n
		Snippet: driver.configure.iqVsSlot.set_slength(step_length = 1.0) \n
		Selects the time between the beginning of two consecutive measurement steps. \n
			:param step_length: Range: 50E-6 s to 5E-3 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_ftype(self) -> enums.FilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe \n
		Snippet: value: enums.FilterType = driver.configure.iqVsSlot.get_ftype() \n
		Selects the IF filter type. \n
			:return: filter_type: GAUSs | NYQuist | NY1Mhz GAUSs: filter of Gaussian shape, 100 kHz bandwidth NYQuist: Nyquist filter, 100 kHz bandwidth NY1Mhz: Nyquist filter, 1 MHz bandwidth
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.FilterType)

	def set_ftype(self, filter_type: enums.FilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe \n
		Snippet: driver.configure.iqVsSlot.set_ftype(filter_type = enums.FilterType.GAUSs) \n
		Selects the IF filter type. \n
			:param filter_type: GAUSs | NYQuist | NY1Mhz GAUSs: filter of Gaussian shape, 100 kHz bandwidth NYQuist: Nyquist filter, 100 kHz bandwidth NY1Mhz: Nyquist filter, 1 MHz bandwidth
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FTYPe {param}')

	def get_fe_limit(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit \n
		Snippet: value: float = driver.configure.iqVsSlot.get_fe_limit() \n
		Defines a minimum average signal level relative to the expected nominal power. The setting applies to all measurement
		steps considered for the calculation of the average frequency per subsweep and the overall frequency error. \n
			:return: limit: Range: -100 dB to -30 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit?')
		return Conversions.str_to_float(response)

	def set_fe_limit(self, limit: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit \n
		Snippet: driver.configure.iqVsSlot.set_fe_limit(limit = 1.0) \n
		Defines a minimum average signal level relative to the expected nominal power. The setting applies to all measurement
		steps considered for the calculation of the average frequency per subsweep and the overall frequency error. \n
			:param limit: Range: -100 dB to -30 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(limit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:FELimit {param}')

	def clone(self) -> 'IqVsSlot':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqVsSlot(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
