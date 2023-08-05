from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmplitudeProbDensity:
	"""AmplitudeProbDensity commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("amplitudeProbDensity", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:APD \n
		Snippet: value: List[float] = driver.power.amplitudeProbDensity.fetch() \n
		Returns the trace points of the amplitude probability density (APD) . This result is only available in statistic
		evaluation mode (see method RsCmwGprfMeas.Configure.Power.mode) . \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: 4096 results, each representing a 0.047dB interval ('bin') . The position of the average power 'bin' can be retrieved via method RsCmwGprfMeas.Power.CumulativeDistribFnc.Power.fetch. Range: 10E-9 % to 100 %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:POWer:APD?', suppressed)
		return response
