from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Short:
	"""Short commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("short", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> enums.PathLossState:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: value: enums.PathLossState = driver.ploss.short.fetch(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		Queries the result state for the measurement mode 'Short' and a selected path of a selected connector. For possible
		connector values, see 'Values for RF Path Selection'. \n
		Use RsCmwGprfMeas.reliability.last_value to read the updated reliability indicator. \n
			:param connector: RF connector for which the result state is queried
			:param path_index: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the parameter if you have only one path at the connector.
			:return: result_state_short: NCAP | PEND | RDY NCAP: no measurement results available PEND: measurement running RDY: measurement complete, results available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum), ArgSingle('path_index', path_index, DataType.Enum, True))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GPRF:MEASurement<Instance>:PLOSs:SHORt? {param}'.rstrip(), suppressed)
		return Conversions.str_to_scalar_enum(response, enums.PathLossState)
