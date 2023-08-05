from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParameterSetList:
	"""ParameterSetList commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("parameterSetList", core, parent)

	def set(self, index: int, parameter_set: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET \n
		Snippet: driver.configure.power.listPy.parameterSetList.set(index = 1, parameter_set = 1) \n
		Selects the parameter set for a particular frequency/level step <index>. The parameter sets are defined using ...
		GPRF:MEAS<i>:POWER:PSET... commands; see 'Command Reference'. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 3999
			:param parameter_set: Parameter set number Range: 0 to 31
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('parameter_set', parameter_set, DataType.Integer))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET {param}'.rstrip())

	def get(self, index: int) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET \n
		Snippet: value: int = driver.configure.power.listPy.parameterSetList.get(index = 1) \n
		Selects the parameter set for a particular frequency/level step <index>. The parameter sets are defined using ...
		GPRF:MEAS<i>:POWER:PSET... commands; see 'Command Reference'. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 3999
			:return: parameter_set: Parameter set number Range: 0 to 31"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET? {param}')
		return Conversions.str_to_int(response)

	def get_all(self) -> List[int]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL \n
		Snippet: value: List[int] = driver.configure.power.listPy.parameterSetList.get_all() \n
		Selects the parameter set for all frequency/level steps. To configure parameter sets, see 'Parameter Set List Settings'. \n
			:return: parameter_set: Comma-separated list of up to 2000 parameter set indices, with one value per frequency/level step A query returns 2000 values (maximum number of steps) . Range: 0 to 31
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL?')
		return response

	def set_all(self, parameter_set: List[int]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL \n
		Snippet: driver.configure.power.listPy.parameterSetList.set_all(parameter_set = [1, 2, 3]) \n
		Selects the parameter set for all frequency/level steps. To configure parameter sets, see 'Parameter Set List Settings'. \n
			:param parameter_set: Comma-separated list of up to 2000 parameter set indices, with one value per frequency/level step A query returns 2000 values (maximum number of steps) . Range: 0 to 31
		"""
		param = Conversions.list_to_csv_str(parameter_set)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:PSET:ALL {param}')
