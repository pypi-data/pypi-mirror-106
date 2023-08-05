from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnvelopePower:
	"""EnvelopePower commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("envelopePower", core, parent)

	def set(self, index: int, exp_nom_power: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower \n
		Snippet: driver.configure.iqRecorder.listPy.envelopePower.set(index = 1, exp_nom_power = 1.0) \n
		Defines or queries the expected nominal power of a selected frequency/level step. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 1999
			:param exp_nom_power: Expected nominal power of the frequency/level step Range: -55 dBm to 55 dBm, Unit: dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('exp_nom_power', exp_nom_power, DataType.Float))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower \n
		Snippet: value: float = driver.configure.iqRecorder.listPy.envelopePower.get(index = 1) \n
		Defines or queries the expected nominal power of a selected frequency/level step. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 1999
			:return: exp_nom_power: Expected nominal power of the frequency/level step Range: -55 dBm to 55 dBm, Unit: dBm"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower:ALL \n
		Snippet: value: List[float] = driver.configure.iqRecorder.listPy.envelopePower.get_all() \n
		Defines the expected nominal power of all frequency/level steps. \n
			:return: exp_nom_power: Comma-separated list of up to 2000 expected powers, one value per frequency/level step A query returns 2000 results (maximum number of steps) . Range: -55 dBm to 55 dBm, Unit: dBm
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower:ALL?')
		return response

	def set_all(self, exp_nom_power: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower:ALL \n
		Snippet: driver.configure.iqRecorder.listPy.envelopePower.set_all(exp_nom_power = [1.1, 2.2, 3.3]) \n
		Defines the expected nominal power of all frequency/level steps. \n
			:param exp_nom_power: Comma-separated list of up to 2000 expected powers, one value per frequency/level step A query returns 2000 results (maximum number of steps) . Range: -55 dBm to 55 dBm, Unit: dBm
		"""
		param = Conversions.list_to_csv_str(exp_nom_power)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:ENPower:ALL {param}')
