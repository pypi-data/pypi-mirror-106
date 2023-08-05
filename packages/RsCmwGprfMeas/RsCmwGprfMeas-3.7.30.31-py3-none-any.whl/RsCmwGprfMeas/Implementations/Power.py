from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 71 total commands, 13 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Power_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def current(self):
		"""current commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Power_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Power_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def minimum(self):
		"""minimum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Power_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def maximum(self):
		"""maximum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Power_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def standardDev(self):
		"""standardDev commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_standardDev'):
			from .Power_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def cumulativeDistribFnc(self):
		"""cumulativeDistribFnc commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_cumulativeDistribFnc'):
			from .Power_.CumulativeDistribFnc import CumulativeDistribFnc
			self._cumulativeDistribFnc = CumulativeDistribFnc(self._core, self._base)
		return self._cumulativeDistribFnc

	@property
	def amplitudeProbDensity(self):
		"""amplitudeProbDensity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amplitudeProbDensity'):
			from .Power_.AmplitudeProbDensity import AmplitudeProbDensity
			self._amplitudeProbDensity = AmplitudeProbDensity(self._core, self._base)
		return self._amplitudeProbDensity

	@property
	def elapsedStats(self):
		"""elapsedStats commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elapsedStats'):
			from .Power_.ElapsedStats import ElapsedStats
			self._elapsedStats = ElapsedStats(self._core, self._base)
		return self._elapsedStats

	@property
	def listPy(self):
		"""listPy commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .Power_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def peak(self):
		"""peak commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Power_.Peak import Peak
			self._peak = Peak(self._core, self._base)
		return self._peak

	@property
	def iqData(self):
		"""iqData commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_iqData'):
			from .Power_.IqData import IqData
			self._iqData = IqData(self._core, self._base)
		return self._iqData

	@property
	def iqInfo(self):
		"""iqInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqInfo'):
			from .Power_.IqInfo import IqInfo
			self._iqInfo = IqInfo(self._core, self._base)
		return self._iqInfo

	def initiate(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GPRF:MEASurement<Instance>:POWer')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:POWer')

	def stop(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GPRF:MEASurement<Instance>:POWer')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:POWer')

	def abort(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GPRF:MEASurement<Instance>:POWer')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:POWer \n
		Snippet: driver.power.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:POWer')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
