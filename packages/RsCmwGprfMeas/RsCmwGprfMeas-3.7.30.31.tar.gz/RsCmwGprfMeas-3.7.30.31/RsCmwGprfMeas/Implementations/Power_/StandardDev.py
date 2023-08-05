from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .StandardDev_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:SDEViation \n
		Snippet: value: List[float] = driver.power.standardDev.calculate() \n
		Returns the standard deviation values, see 'Measurement Results'. The values described below are returned by FETCh and
		READ commands. CALCulate commands return a single-value error code for each result listed below. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_std_dev_cur: Standard deviation of RMS power results for each measured power step. If the list mode is switched off, a single value is returned (n = 1) . In list mode, the total number n of results is equal to the list count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . Range: 0 dB to 78 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:SDEViation?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:SDEViation \n
		Snippet: value: List[float] = driver.power.standardDev.fetch() \n
		Returns the standard deviation values, see 'Measurement Results'. The values described below are returned by FETCh and
		READ commands. CALCulate commands return a single-value error code for each result listed below. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_std_dev_cur: Standard deviation of RMS power results for each measured power step. If the list mode is switched off, a single value is returned (n = 1) . In list mode, the total number n of results is equal to the list count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . Range: 0 dB to 78 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:SDEViation?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:SDEViation \n
		Snippet: value: List[float] = driver.power.standardDev.read() \n
		Returns the standard deviation values, see 'Measurement Results'. The values described below are returned by FETCh and
		READ commands. CALCulate commands return a single-value error code for each result listed below. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_std_dev_cur: Standard deviation of RMS power results for each measured power step. If the list mode is switched off, a single value is returned (n = 1) . In list mode, the total number n of results is equal to the list count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . Range: 0 dB to 78 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:SDEViation?', suppressed)
		return response

	def clone(self) -> 'StandardDev':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StandardDev(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
