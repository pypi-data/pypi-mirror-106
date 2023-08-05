from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[float] = driver.power.peak.minimum.calculate() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_minimum_min: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[float] = driver.power.peak.minimum.fetch() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_minimum_min: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum \n
		Snippet: value: List[float] = driver.power.peak.minimum.read() \n
		Returns RF power results, see 'Measurement Results'.
			INTRO_CMD_HELP: The following results can be retrieved: \n
			- 'Power Current RMS' (...:POWer:CURRent?)
			- 'Power Current Min.' (...:MINimum:CURRent?)
			- 'Power Current Max.' (...:MAXimum:CURRent?)
			- 'Power Average RMS' (...:AVERage?)
			- 'Power Minimum' (...:PEAK:MINimum?)
			- 'Power Maximum' (...:PEAK:MAXimum?)  \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power_minimum_min: If list mode is switched off, a single value is returned. In list mode, n is equal to the step count (method RsCmwGprfMeas.Configure.Power.ListPy.count) . CALCulate commands return error indicators for each measured power step. FETCh/READ commands return RF power values for each measured power step. Range: -100 dBm to 57 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:PEAK:MINimum?', suppressed)
		return response
