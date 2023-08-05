from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sample:
	"""Sample commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sample", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Count: int: Total sample count Range: 0 to 281.474976710655E+12
			- Time: float: Total sample time Range: 0 s to 30.7584E+6 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Count'),
			ArgStruct.scalar_float('Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Count: int = None
			self.Time: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:SAMPle \n
		Snippet: value: FetchStruct = driver.power.cumulativeDistribFnc.sample.fetch() \n
		Returns the sample counters in statistic evaluation mode (see method RsCmwGprfMeas.Configure.Power.mode) . The statistic
		evaluation mode is only available for single-step measurements (list mode OFF) . \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:POWer:CCDF:SAMPle?', self.__class__.FetchStruct())
