from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqData:
	"""IqData commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqData", core, parent)

	@property
	def bin(self):
		"""bin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bin'):
			from .IqData_.Bin import Bin
			self._bin = Bin(self._core, self._base)
		return self._bin

	def fetch(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:IQData \n
		Snippet: value: List[float] = driver.power.iqData.fetch(list_index = 1, result_index = 1) \n
		Returns the results of the I/Q data measurement in a particular frequency/level step <index> in ASCII format. With the
		optional <ResultIndex> parameter, it is also possible to get results for a particular list index repetition. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:param list_index: Range: 0 to 3999
			:param result_index: Range: 0 to #repetitions of ListIndex
			:return: iq_data: I and Q amplitudes in alternating order. The values depend on the selected magnitude unit (method RsCmwGprfMeas.Configure.Power.ListPy.munit. Range: -160 V to 160 V , Unit: V"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:IQData? {param}'.rstrip(), suppressed)
		return response

	def read(self, list_index: int, result_index: int = None) -> List[float]:
		"""SCPI: READ:GPRF:MEASurement<Instance>:POWer:IQData \n
		Snippet: value: List[float] = driver.power.iqData.read(list_index = 1, result_index = 1) \n
		Returns the results of the I/Q data measurement in a particular frequency/level step <index> in ASCII format. With the
		optional <ResultIndex> parameter, it is also possible to get results for a particular list index repetition. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:param list_index: Range: 0 to 3999
			:param result_index: Range: 0 to #repetitions of ListIndex
			:return: iq_data: I and Q amplitudes in alternating order. The values depend on the selected magnitude unit (method RsCmwGprfMeas.Configure.Power.ListPy.munit. Range: -160 V to 160 V , Unit: V"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('list_index', list_index, DataType.Integer), ArgSingle('result_index', result_index, DataType.Integer, True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:POWer:IQData? {param}'.rstrip(), suppressed)
		return response

	def clone(self) -> 'IqData':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqData(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
