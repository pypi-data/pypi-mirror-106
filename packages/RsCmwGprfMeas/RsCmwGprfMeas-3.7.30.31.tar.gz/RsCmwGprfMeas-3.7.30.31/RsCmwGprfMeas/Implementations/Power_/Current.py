from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 9 total commands, 3 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rms'):
			from .Current_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Current_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Current_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[float] = driver.power.current.calculate() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_current_rms: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[float] = driver.power.current.fetch() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_current_rms: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:CURRent \n
		Snippet: value: List[float] = driver.power.current.read() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_current_rms: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:CURRent?', suppressed)
		return response

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
