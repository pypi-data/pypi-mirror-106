from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 48 total commands, 5 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .Power_.ParameterSetList import ParameterSetList
			self._parameterSetList = ParameterSetList(self._core, self._base)
		return self._parameterSetList

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Power_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Power_.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .Power_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def listPy(self):
		"""listPy commands group. 7 Sub-classes, 7 commands."""
		if not hasattr(self, '_listPy'):
			from .Power_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CcdfMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: value: enums.CcdfMode = driver.configure.power.get_mode() \n
		Sets/gets the result mode for the single-step power measurement. Note that the result mode has to be set before the power
		measurement is started. \n
			:return: ccdf_mode: POWer | STATistic POWer: power mode, only summary statistics calculated (minimum, maximum, average, standard deviation) STATistic: statistic mode, power distributions/densities calculated
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CcdfMode)

	def set_mode(self, ccdf_mode: enums.CcdfMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MODE \n
		Snippet: driver.configure.power.set_mode(ccdf_mode = enums.CcdfMode.POWer) \n
		Sets/gets the result mode for the single-step power measurement. Note that the result mode has to be set before the power
		measurement is started. \n
			:param ccdf_mode: POWer | STATistic POWer: power mode, only summary statistics calculated (minimum, maximum, average, standard deviation) STATistic: statistic mode, power distributions/densities calculated
		"""
		param = Conversions.enum_scalar_to_str(ccdf_mode, enums.CcdfMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:MODE {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: value: float = driver.configure.power.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT \n
		Snippet: driver.configure.power.set_timeout(tcd_timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:TOUT {param}')

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth \n
		Snippet: value: float = driver.configure.power.get_slength() \n
		Selects the time between the beginning of two consecutive measured power steps. \n
			:return: step_length: Range: 50E-6 s to 1 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth \n
		Snippet: driver.configure.power.set_slength(step_length = 1.0) \n
		Selects the time between the beginning of two consecutive measured power steps. \n
			:param step_length: Range: 50E-6 s to 1 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:SLENgth {param}')

	def get_mlength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth \n
		Snippet: value: float = driver.configure.power.get_mlength() \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the power results for each measurement
		step. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.slength) . \n
			:return: meas_length: Range: 10E-6 s to 1 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth?')
		return Conversions.str_to_float(response)

	def set_mlength(self, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth \n
		Snippet: driver.configure.power.set_mlength(meas_length = 1.0) \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the power results for each measurement
		step. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.slength) . \n
			:param meas_length: Range: 10E-6 s to 1 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:MLENgth {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.power.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition \n
		Snippet: driver.configure.power.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:REPetition {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt \n
		Snippet: value: int = driver.configure.power.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: Number of measurement intervals. A measurement interval comprises a single power/frequency step (list mode switched off) or a sweep (list mode switched on) . Range: 1 to 100E+3
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt \n
		Snippet: driver.configure.power.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: Number of measurement intervals. A measurement interval comprises a single power/frequency step (list mode switched off) or a sweep (list mode switched on) . Range: 1 to 100E+3
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:SCOunt {param}')

	def get_pdef_set(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset \n
		Snippet: value: str = driver.configure.power.get_pdef_set() \n
		This command is related to the global parameter set. A setting command loads a predefined set of parameters into the
		global parameter set. A query returns the name of the predefined set assigned to the global parameter set. To get a list
		of predefined-set strings, use method RsCmwGprfMeas.Configure.Power.ParameterSetList.Catalog.pdefSet. \n
			:return: predefined_set: Predefined set as string
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset?')
		return trim_str_response(response)

	def set_pdef_set(self, predefined_set: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset \n
		Snippet: driver.configure.power.set_pdef_set(predefined_set = '1') \n
		This command is related to the global parameter set. A setting command loads a predefined set of parameters into the
		global parameter set. A query returns the name of the predefined set assigned to the global parameter set. To get a list
		of predefined-set strings, use method RsCmwGprfMeas.Configure.Power.ParameterSetList.Catalog.pdefSet. \n
			:param predefined_set: Predefined set as string
		"""
		param = Conversions.value_to_quoted_str(predefined_set)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PDEFset {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
