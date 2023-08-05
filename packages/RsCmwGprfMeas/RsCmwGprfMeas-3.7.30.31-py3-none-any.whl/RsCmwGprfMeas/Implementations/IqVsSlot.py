from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqVsSlot:
	"""IqVsSlot commands group definition. 18 total commands, 7 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqVsSlot", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .IqVsSlot_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def ofError(self):
		"""ofError commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ofError'):
			from .IqVsSlot_.OfError import OfError
			self._ofError = OfError(self._core, self._base)
		return self._ofError

	@property
	def icomponent(self):
		"""icomponent commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_icomponent'):
			from .IqVsSlot_.Icomponent import Icomponent
			self._icomponent = Icomponent(self._core, self._base)
		return self._icomponent

	@property
	def qcomponent(self):
		"""qcomponent commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qcomponent'):
			from .IqVsSlot_.Qcomponent import Qcomponent
			self._qcomponent = Qcomponent(self._core, self._base)
		return self._qcomponent

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_level'):
			from .IqVsSlot_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_phase'):
			from .IqVsSlot_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_freqError'):
			from .IqVsSlot_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	def initiate(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:GPRF:MEASurement<Instance>:IQVSlot')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:GPRF:MEASurement<Instance>:IQVSlot')

	def stop(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:GPRF:MEASurement<Instance>:IQVSlot')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:IQVSlot')

	def abort(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:GPRF:MEASurement<Instance>:IQVSlot')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:IQVSlot \n
		Snippet: driver.iqVsSlot.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwGprfMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:IQVSlot')

	def clone(self) -> 'IqVsSlot':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqVsSlot(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
