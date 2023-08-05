from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("symbolRate", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQRecorder:SRATe \n
		Snippet: value: float = driver.iqRecorder.symbolRate.fetch() \n
		Returns the sampling rate of the I/Q recorder measurement, depending on the filter settings, see 'Filter Settings and
		Samples'. \n
			:return: sample_rate: Range: 0 Hz to 100 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'FETCh:GPRF:MEASurement<Instance>:IQRecorder:SRATe?')
		return Conversions.str_to_float(response)
