from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def set(self, index: int, frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency \n
		Snippet: driver.configure.power.listPy.frequency.set(index = 1, frequency = 1.0) \n
		Defines or queries the frequency of a selected frequency/level step. The supported frequency range depends on the
		instrument model and the available options. The supported range can be smaller than stated here. Refer to the preface of
		your model-specific base unit manual. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 3999
			:param frequency: Frequency of the frequency/level step Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency \n
		Snippet: value: float = driver.configure.power.listPy.frequency.get(index = 1) \n
		Defines or queries the frequency of a selected frequency/level step. The supported frequency range depends on the
		instrument model and the available options. The supported range can be smaller than stated here. Refer to the preface of
		your model-specific base unit manual. \n
			:param index: Number of the frequency/level step in the table Range: 0 to 3999
			:return: frequency: Frequency of the frequency/level step Range: 70 MHz to 6 GHz, Unit: Hz"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency:ALL \n
		Snippet: value: List[float] = driver.configure.power.listPy.frequency.get_all() \n
		Defines the frequencies of all frequency/level steps. The supported frequency range depends on the instrument model and
		the available options. The supported range can be smaller than stated here. Refer to the preface of your model-specific
		base unit manual. \n
			:return: frequency: Comma-separated list of up to 2000 frequencies, with one value per frequency/level step A query returns 2000 results (maximum number of steps) . Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency:ALL?')
		return response

	def set_all(self, frequency: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency:ALL \n
		Snippet: driver.configure.power.listPy.frequency.set_all(frequency = [1.1, 2.2, 3.3]) \n
		Defines the frequencies of all frequency/level steps. The supported frequency range depends on the instrument model and
		the available options. The supported range can be smaller than stated here. Refer to the preface of your model-specific
		base unit manual. \n
			:param frequency: Comma-separated list of up to 2000 frequencies, with one value per frequency/level step A query returns 2000 results (maximum number of steps) . Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.list_to_csv_str(frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FREQuency:ALL {param}')
