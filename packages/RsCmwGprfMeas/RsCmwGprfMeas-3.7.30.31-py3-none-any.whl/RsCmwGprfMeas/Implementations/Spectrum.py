from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 48 total commands, 8 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Spectrum_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def referenceMarker(self):
		"""referenceMarker commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_referenceMarker'):
			from .Spectrum_.ReferenceMarker import ReferenceMarker
			self._referenceMarker = ReferenceMarker(self._core, self._base)
		return self._referenceMarker

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Spectrum_.Marker import Marker
			self._marker = Marker(self._core, self._base)
		return self._marker

	@property
	def sample(self):
		"""sample commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sample'):
			from .Spectrum_.Sample import Sample
			self._sample = Sample(self._core, self._base)
		return self._sample

	@property
	def rms(self):
		"""rms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Spectrum_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def maximum(self):
		"""maximum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Spectrum_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Spectrum_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def average(self):
		"""average commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Spectrum_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	def initiate(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GPRF:MEASurement<Instance>:SPECtrum')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:SPECtrum')

	def stop(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GPRF:MEASurement<Instance>:SPECtrum')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:SPECtrum')

	def abort(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GPRF:MEASurement<Instance>:SPECtrum')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:SPECtrum \n
		Snippet: driver.spectrum.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:SPECtrum')

	def clone(self) -> 'Spectrum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
