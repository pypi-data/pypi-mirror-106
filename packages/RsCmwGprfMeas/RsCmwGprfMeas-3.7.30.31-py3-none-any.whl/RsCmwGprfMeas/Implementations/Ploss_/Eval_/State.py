from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Result_State_Open: enums.PathLossState: NCAP | PEND | RDY Result state for measurement mode 'Open' NCAP: no measurement results available PEND: measurement running RDY: measurement complete, results available
			- Result_State_Short: enums.PathLossState: NCAP | PEND | RDY Result state for measurement mode 'Short'
			- Result_State_Eval: enums.PathLossState: NCAP | PEND | RDY Result state for measurement mode 'Eval'"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Result_State_Open', enums.PathLossState),
			ArgStruct.scalar_enum('Result_State_Short', enums.PathLossState),
			ArgStruct.scalar_enum('Result_State_Eval', enums.PathLossState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Result_State_Open: enums.PathLossState = None
			self.Result_State_Short: enums.PathLossState = None
			self.Result_State_Eval: enums.PathLossState = None

	def fetch(self, connector: enums.CmwsConnector, path_index: enums.PathIndex = None) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:STATe \n
		Snippet: value: FetchStruct = driver.ploss.eval.state.fetch(connector = enums.CmwsConnector.R11, path_index = enums.PathIndex.P1) \n
		Queries the result state for all measurement modes and a selected path of a selected connector. For possible connector
		values, see 'Values for RF Path Selection'. \n
			:param connector: RF connector for which the result state is queried
			:param path_index: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the parameter if you have only one path at the connector.
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum), ArgSingle('path_index', path_index, DataType.Enum, True))
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:PLOSs:EVAL:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
