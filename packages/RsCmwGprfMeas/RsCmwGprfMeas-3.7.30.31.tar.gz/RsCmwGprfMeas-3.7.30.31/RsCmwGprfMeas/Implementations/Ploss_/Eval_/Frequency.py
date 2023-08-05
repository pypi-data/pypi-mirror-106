from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def fetch(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> List[float]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:FREQuency \n
		Snippet: value: List[float] = driver.ploss.eval.frequency.fetch(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		Returns the frequency values of the result table for a selected path of a selected connector. The order of the list
		entries is the same as in the command method RsCmwGprfMeas.Ploss.Eval.Gain.fetch. Use this command to check at which
		frequencies the gain values have been measured. For possible connector values, see 'Values for RF Path Selection'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:param connector: RF connector for which results are queried
			:param path_index: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the parameter if you have only one path at the connector.
			:return: frequency: Comma-separated list of frequency values Unit: Hz"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum), ArgSingle('path_index', path_index, DataType.Enum, True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:FREQuency? {param}'.rstrip(), suppressed)
		return response
