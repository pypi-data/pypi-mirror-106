from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdefSet:
	"""PdefSet commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdefSet", core, parent)

	def set(self, index: int, predefined_set: str) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:PDEFset \n
		Snippet: driver.configure.power.parameterSetList.pdefSet.set(index = 1, predefined_set = '1') \n
		This command is related to parameter sets in retriggered list mode. A setting command loads a predefined set of
		parameters into the parameter set <Index>. A query returns the name of the predefined set assigned to the parameter set
		<Index>. To get a list of predefined-set strings, use method RsCmwGprfMeas.Configure.Power.ParameterSetList.Catalog.
		pdefSet. \n
			:param index: Parameter set number Range: 0 to 31
			:param predefined_set: Predefined set as string
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('predefined_set', predefined_set, DataType.String))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:PDEFset {param}'.rstrip())

	def get(self, index: int) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:PDEFset \n
		Snippet: value: str = driver.configure.power.parameterSetList.pdefSet.get(index = 1) \n
		This command is related to parameter sets in retriggered list mode. A setting command loads a predefined set of
		parameters into the parameter set <Index>. A query returns the name of the predefined set assigned to the parameter set
		<Index>. To get a list of predefined-set strings, use method RsCmwGprfMeas.Configure.Power.ParameterSetList.Catalog.
		pdefSet. \n
			:param index: Parameter set number Range: 0 to 31
			:return: predefined_set: Predefined set as string"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:PDEFset? {param}')
		return trim_str_response(response)
