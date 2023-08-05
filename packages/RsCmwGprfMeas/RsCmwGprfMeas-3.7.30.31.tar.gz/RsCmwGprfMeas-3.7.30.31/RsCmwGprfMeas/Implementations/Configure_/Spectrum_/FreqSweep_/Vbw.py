from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vbw:
	"""Vbw commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("vbw", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: value: bool = driver.configure.spectrum.freqSweep.vbw.get_auto() \n
		Sets or gets the state of the Auto-VBW selection for the frequency sweep mode. \n
			:return: vbw_auto: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, vbw_auto: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: driver.configure.spectrum.freqSweep.vbw.set_auto(vbw_auto = False) \n
		Sets or gets the state of the Auto-VBW selection for the frequency sweep mode. \n
			:param vbw_auto: OFF | ON
		"""
		param = Conversions.bool_to_str(vbw_auto)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO {param}')

	def get_value(self) -> float or bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: value: float or bool = driver.configure.spectrum.freqSweep.vbw.get_value() \n
		Sets or gets the video bandwidth (VBW) for the frequency sweep mode. Setting this value is only possible if the Auto-VBW
		selection for the sweep mode is switched OFF (see method RsCmwGprfMeas.Configure.Spectrum.FreqSweep.Vbw.auto) . \n
			:return: vbw: Range: 10 Hz to 10 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW?')
		return Conversions.str_to_float_or_bool(response)

	def set_value(self, vbw: float or bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: driver.configure.spectrum.freqSweep.vbw.set_value(vbw = 1.0) \n
		Sets or gets the video bandwidth (VBW) for the frequency sweep mode. Setting this value is only possible if the Auto-VBW
		selection for the sweep mode is switched OFF (see method RsCmwGprfMeas.Configure.Spectrum.FreqSweep.Vbw.auto) . \n
			:param vbw: Range: 10 Hz to 10 MHz, Unit: Hz
		"""
		param = Conversions.decimal_or_bool_value_to_str(vbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW {param}')
