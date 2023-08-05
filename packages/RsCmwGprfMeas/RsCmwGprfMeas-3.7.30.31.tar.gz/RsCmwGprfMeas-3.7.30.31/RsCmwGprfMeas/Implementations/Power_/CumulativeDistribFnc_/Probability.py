from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Probability:
	"""Probability commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("probability", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:PROBability \n
		Snippet: value: List[float] = driver.power.cumulativeDistribFnc.probability.fetch() \n
		Returns percentiles of the complementary cumulative distribution function (CCDF) . This result is only available in
		statistic evaluation mode (see method RsCmwGprfMeas.Configure.Power.mode) . \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: probability: Comma-separated list of percentiles: 10%, 1%, 0.1%, 0.01%, 0.001% and 0.0001% percentiles of the CCDF (6 values) That means, the power limits Lp (in dB) such that 10%, 1%, ... of the samples have a power value average power + Lp. The average power can be retrieved via method RsCmwGprfMeas.Power.CumulativeDistribFnc.Power.fetch. Range: -80 dB to 50 dB, Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:PROBability?', suppressed)
		return response
