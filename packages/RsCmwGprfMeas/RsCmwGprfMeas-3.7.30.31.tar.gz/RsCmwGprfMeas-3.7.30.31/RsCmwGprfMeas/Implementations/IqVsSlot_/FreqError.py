from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqError:
	"""FreqError commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("freqError", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:IQVSlot:FERRor \n
		Snippet: value: List[float] = driver.iqVsSlot.freqError.read() \n
		Returns the frequency errors, see 'Measurement Results'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: frequency_error: Frequency error for each measurement step. The total number n of results is equal to the total number of steps (see method RsCmwGprfMeas.Configure.IqVsSlot.scount) . Range: -500 kHz to 500 kHz, Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:IQVSlot:FERRor?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQVSlot:FERRor \n
		Snippet: value: List[float] = driver.iqVsSlot.freqError.fetch() \n
		Returns the frequency errors, see 'Measurement Results'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: frequency_error: Frequency error for each measurement step. The total number n of results is equal to the total number of steps (see method RsCmwGprfMeas.Configure.IqVsSlot.scount) . Range: -500 kHz to 500 kHz, Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:IQVSlot:FERRor?', suppressed)
		return response
