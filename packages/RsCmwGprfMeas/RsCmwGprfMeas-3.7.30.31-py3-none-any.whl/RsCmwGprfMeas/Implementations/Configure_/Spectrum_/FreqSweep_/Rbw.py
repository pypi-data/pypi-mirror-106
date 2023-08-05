from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbw:
	"""Rbw commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rbw", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO \n
		Snippet: value: bool = driver.configure.spectrum.freqSweep.rbw.get_auto() \n
		Sets or gets the state of the Auto-RBW selection for the frequency sweep mode. \n
			:return: rbw_auto: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, rbw_auto: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO \n
		Snippet: driver.configure.spectrum.freqSweep.rbw.set_auto(rbw_auto = False) \n
		Sets or gets the state of the Auto-RBW selection for the frequency sweep mode. \n
			:param rbw_auto: OFF | ON
		"""
		param = Conversions.bool_to_str(rbw_auto)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW:AUTO {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW \n
		Snippet: value: float = driver.configure.spectrum.freqSweep.rbw.get_value() \n
		Sets or gets the resolution bandwidth (RBW) for the frequency sweep mode. Setting this value is only possible if the
		Auto-RBW selection for the sweep mode is switched OFF (see method RsCmwGprfMeas.Configure.Spectrum.FreqSweep.Rbw.auto) . \n
			:return: rbw: Range: 100 Hz to 10 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW?')
		return Conversions.str_to_float(response)

	def set_value(self, rbw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW \n
		Snippet: driver.configure.spectrum.freqSweep.rbw.set_value(rbw = 1.0) \n
		Sets or gets the resolution bandwidth (RBW) for the frequency sweep mode. Setting this value is only possible if the
		Auto-RBW selection for the sweep mode is switched OFF (see method RsCmwGprfMeas.Configure.Spectrum.FreqSweep.Rbw.auto) . \n
			:param rbw: Range: 100 Hz to 10 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(rbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:RBW {param}')
