from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 6 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	@property
	def span(self):
		"""span commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_span'):
			from .Frequency_.Span import Span
			self._span = Span(self._core, self._base)
		return self._span

	def get_center(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer \n
		Snippet: value: float = driver.configure.spectrum.frequency.get_center() \n
		Sets or gets the center frequency of the spectrum measurement.
			INTRO_CMD_HELP: In frequency sweep mode (see method RsCmwGprfMeas.Configure.Spectrum.Frequency.Span.mode) , setting the center frequency adjusts the start and stop frequencies as follows: \n
			- If the start frequency and stop frequency do not reach the minimum / maximum values, the frequency span is kept constant.
			- If the start frequency or stop frequency reaches the minimum / maximum value, the frequency span is reduced automatically as far as required.
		In zero span mode, setting the center frequency leaves the start frequency, stop frequency and span unchanged.
		These values are adjusted according to the new center frequency and (appropriately reduced) span when the frequency sweep
		mode is selected. This command is only relevant for the standalone scenario. For the combined signal path scenario, use
		the corresponding ...:SIGN<i>:.. command. The supported frequency range depends on the instrument model and the available
		options. The supported range can be smaller than stated here. Refer to the preface of your model-specific base unit
		manual. \n
			:return: center_frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def set_center(self, center_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer \n
		Snippet: driver.configure.spectrum.frequency.set_center(center_frequency = 1.0) \n
		Sets or gets the center frequency of the spectrum measurement.
			INTRO_CMD_HELP: In frequency sweep mode (see method RsCmwGprfMeas.Configure.Spectrum.Frequency.Span.mode) , setting the center frequency adjusts the start and stop frequencies as follows: \n
			- If the start frequency and stop frequency do not reach the minimum / maximum values, the frequency span is kept constant.
			- If the start frequency or stop frequency reaches the minimum / maximum value, the frequency span is reduced automatically as far as required.
		In zero span mode, setting the center frequency leaves the start frequency, stop frequency and span unchanged.
		These values are adjusted according to the new center frequency and (appropriately reduced) span when the frequency sweep
		mode is selected. This command is only relevant for the standalone scenario. For the combined signal path scenario, use
		the corresponding ...:SIGN<i>:.. command. The supported frequency range depends on the instrument model and the available
		options. The supported range can be smaller than stated here. Refer to the preface of your model-specific base unit
		manual. \n
			:param center_frequency: Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(center_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:CENTer {param}')

	def get_start(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt \n
		Snippet: value: float = driver.configure.spectrum.frequency.get_start() \n
		Sets or gets the start frequency of the frequency sweep. \n
			:return: start_frequency: Range: 7E+7 Hz to 6 GHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt \n
		Snippet: driver.configure.spectrum.frequency.set_start(start_frequency = 1.0) \n
		Sets or gets the start frequency of the frequency sweep. \n
			:param start_frequency: Range: 7E+7 Hz to 6 GHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(start_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STARt {param}')

	def get_stop(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP \n
		Snippet: value: float = driver.configure.spectrum.frequency.get_stop() \n
		Sets or gets the stop frequency of the frequency sweep. \n
			:return: stop_frequency: Range: 7E+7 Hz to 6 GHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop_frequency: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP \n
		Snippet: driver.configure.spectrum.frequency.set_stop(stop_frequency = 1.0) \n
		Sets or gets the stop frequency of the frequency sweep. \n
			:param stop_frequency: Range: 7E+7 Hz to 6 GHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(stop_frequency)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:STOP {param}')

	def get_laspan(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan \n
		Snippet: value: float = driver.configure.spectrum.frequency.get_laspan() \n
		Sets the span for frequency sweep measurements to its previous value or queries the span's previous value (see method
		RsCmwGprfMeas.Configure.Spectrum.Frequency.Span.value) . \n
			:return: last_span: Range: 0 Hz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan?')
		return Conversions.str_to_float(response)

	def set_laspan(self, last_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan \n
		Snippet: driver.configure.spectrum.frequency.set_laspan(last_span = 1.0) \n
		Sets the span for frequency sweep measurements to its previous value or queries the span's previous value (see method
		RsCmwGprfMeas.Configure.Spectrum.Frequency.Span.value) . \n
			:param last_span: Range: 0 Hz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(last_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:LASPan {param}')

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
