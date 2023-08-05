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
		"""SCPI: READ:GPRF:MEASurement<Instance>:FFTSanalyzer:Q \n
		Snippet: value: List[float] = driver.fftSpecAn.qcomponent.read() \n
		Returns the measured normalized I and Q amplitudes in the time domain. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qdata: Comma-separated list of n normalized I or Q amplitudes, where n is given by the FFT length, see method RsCmwGprfMeas.Configure.FftSpecAn.fftLength. Range: -2 to 2"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GPRF:MEASurement<Instance>:FFTSanalyzer:Q?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:Q \n
		Snippet: value: List[float] = driver.fftSpecAn.qcomponent.fetch() \n
		Returns the measured normalized I and Q amplitudes in the time domain. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: qdata: Comma-separated list of n normalized I or Q amplitudes, where n is given by the FFT length, see method RsCmwGprfMeas.Configure.FftSpecAn.fftLength. Range: -2 to 2"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:Q?', suppressed)
		return response
