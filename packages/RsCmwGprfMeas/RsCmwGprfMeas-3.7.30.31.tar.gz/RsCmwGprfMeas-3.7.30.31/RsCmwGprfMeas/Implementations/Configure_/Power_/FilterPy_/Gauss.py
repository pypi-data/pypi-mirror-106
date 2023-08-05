from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gauss:
	"""Gauss commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gauss", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth \n
		Snippet: value: float = driver.configure.power.filterPy.gauss.get_bandwidth() \n
		Selects the bandwidth for a filter of Gaussian shape. \n
			:return: gauss_bw: Range: 10 Hz | 30 Hz | 50 Hz | 100 Hz | 300 Hz | 500 Hz | 1 kHz | 3 kHz | 5 kHz | 6.25 kHz | 10 kHz | 30 kHz | 50 kHz | 100 kHz | 300 kHz | 500 kHz | 1 MHz | 3 MHz | 5 MHz | 10 MHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, gauss_bw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth \n
		Snippet: driver.configure.power.filterPy.gauss.set_bandwidth(gauss_bw = 1.0) \n
		Selects the bandwidth for a filter of Gaussian shape. \n
			:param gauss_bw: Range: 10 Hz | 30 Hz | 50 Hz | 100 Hz | 300 Hz | 500 Hz | 1 kHz | 3 kHz | 5 kHz | 6.25 kHz | 10 kHz | 30 kHz | 50 kHz | 100 kHz | 300 kHz | 500 kHz | 1 MHz | 3 MHz | 5 MHz | 10 MHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(gauss_bw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:GAUSs:BWIDth {param}')
