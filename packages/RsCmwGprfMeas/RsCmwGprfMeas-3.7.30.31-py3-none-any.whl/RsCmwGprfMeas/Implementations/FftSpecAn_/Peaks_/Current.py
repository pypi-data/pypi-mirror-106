from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Frequency: List[float]: The range depends on the search range settings, see [CMDLINK: CONFigure:GPRF:MEASi:FFTSanalyzer:PSEarch CMDLINK]. Unit: Hz
			- Level: List[float]: Range: -100 dBm to 57 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Frequency: List[float] = None
			self.Level: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:GPRF:MEASurement<Instance>:FFTSanalyzer:PEAKs:CURRent \n
		Snippet: value: ResultData = driver.fftSpecAn.peaks.current.read() \n
		Returns the results of the peak search. Separate commands retrieve current and average values. There are results for
		search range no. 0 to 4: <Reliability>, <Frequency0>, <Power0>, ..., <Frequency4>, <Power4> \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GPRF:MEASurement<Instance>:FFTSanalyzer:PEAKs:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:PEAKs:CURRent \n
		Snippet: value: ResultData = driver.fftSpecAn.peaks.current.fetch() \n
		Returns the results of the peak search. Separate commands retrieve current and average values. There are results for
		search range no. 0 to 4: <Reliability>, <Frequency0>, <Power0>, ..., <Frequency4>, <Power4> \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:FFTSanalyzer:PEAKs:CURRent?', self.__class__.ResultData())
