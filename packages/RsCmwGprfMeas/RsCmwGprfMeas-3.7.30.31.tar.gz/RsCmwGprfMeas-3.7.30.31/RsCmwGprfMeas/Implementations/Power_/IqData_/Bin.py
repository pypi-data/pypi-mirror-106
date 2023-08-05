from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bin:
	"""Bin commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bin", core, parent)

	def fetch(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:IQData:BIN \n
		Snippet: value: List[float] = driver.power.iqData.bin.fetch(list_index = 1, result_index = 1) \n
		Returns the results of the I/Q data measurement in a particular frequency/level step <index> in binary data format. With
		the optional <ResultIndex> parameter, it is also possible to get results for a particular list index repetition. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:param list_index: Range: 0 to 3999
			:param result_index: Range: 0 to #repetitions of ListIndex
			:return: iq_data: I and Q amplitudes (binary) in alternating order. See Table 'Returned IQData' below. The values depend on the selected magnitude unit (method RsCmwGprfMeas.Configure.Power.ListPy.munit. Range: -160.0 to 160.0 if magnitude unit is VOLT, -32768.0 to 32767.0 if magnitude unit is RAW"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:IQData:BIN? {param}'.rstrip(), suppressed)
		return response
