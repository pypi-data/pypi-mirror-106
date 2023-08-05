from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qcomponent:
	"""Qcomponent commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qcomponent", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQVSlot:Q \n
		Snippet: value: List[float] = driver.iqVsSlot.qcomponent.read() \n
		Returns the averaged I and Q amplitudes, see 'Measurement Results'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qdata: Average I or Q amplitude for each measurement step. The total number n of results is equal to the total number of steps (see method RsCmwGprfMeas.Configure.IqVsSlot.scount) . Range: -150 V to 150 V, Unit: V"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:IQVSlot:Q?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQVSlot:Q \n
		Snippet: value: List[float] = driver.iqVsSlot.qcomponent.fetch() \n
		Returns the averaged I and Q amplitudes, see 'Measurement Results'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qdata: Average I or Q amplitude for each measurement step. The total number n of results is equal to the total number of steps (see method RsCmwGprfMeas.Configure.IqVsSlot.scount) . Range: -150 V to 150 V, Unit: V"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:IQVSlot:Q?', suppressed)
		return response
