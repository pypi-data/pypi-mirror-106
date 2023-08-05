from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CumulativeDistribFnc:
	"""CumulativeDistribFnc commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cumulativeDistribFnc", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .CumulativeDistribFnc_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def sample(self):
		"""sample commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sample'):
			from .CumulativeDistribFnc_.Sample import Sample
			self._sample = Sample(self._core, self._base)
		return self._sample

	@property
	def probability(self):
		"""probability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_probability'):
			from .CumulativeDistribFnc_.Probability import Probability
			self._probability = Probability(self._core, self._base)
		return self._probability

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF \n
		Snippet: value: List[float] = driver.power.cumulativeDistribFnc.fetch() \n
		Returns the trace points of the complementary cumulative distribution function (CCDF) . This result is only available in
		statistic evaluation mode (see method RsCmwGprfMeas.Configure.Power.mode) . \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: 4096 results, each representing a 0.047dB interval ('bin') . The position of the average power 'bin' can be retrieved via method RsCmwGprfMeas.Power.CumulativeDistribFnc.Power.fetch. Range: 10E-9 % to 100 %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF?', suppressed)
		return response

	def clone(self) -> 'CumulativeDistribFnc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CumulativeDistribFnc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
