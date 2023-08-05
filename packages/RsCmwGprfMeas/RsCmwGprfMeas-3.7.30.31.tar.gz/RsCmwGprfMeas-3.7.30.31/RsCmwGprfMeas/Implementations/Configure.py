from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 144 total commands, 9 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 7 commands."""
		if not hasattr(self, '_power'):
			from .Configure_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def iqVsSlot(self):
		"""iqVsSlot commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_iqVsSlot'):
			from .Configure_.IqVsSlot import IqVsSlot
			self._iqVsSlot = IqVsSlot(self._core, self._base)
		return self._iqVsSlot

	@property
	def extPwrSensor(self):
		"""extPwrSensor commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_extPwrSensor'):
			from .Configure_.ExtPwrSensor import ExtPwrSensor
			self._extPwrSensor = ExtPwrSensor(self._core, self._base)
		return self._extPwrSensor

	@property
	def nrpm(self):
		"""nrpm commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_nrpm'):
			from .Configure_.Nrpm import Nrpm
			self._nrpm = Nrpm(self._core, self._base)
		return self._nrpm

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 3 Sub-classes, 9 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .Configure_.IqRecorder import IqRecorder
			self._iqRecorder = IqRecorder(self._core, self._base)
		return self._iqRecorder

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_spectrum'):
			from .Configure_.Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._base)
		return self._spectrum

	@property
	def fftSpecAn(self):
		"""fftSpecAn commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_fftSpecAn'):
			from .Configure_.FftSpecAn import FftSpecAn
			self._fftSpecAn = FftSpecAn(self._core, self._base)
		return self._fftSpecAn

	@property
	def ploss(self):
		"""ploss commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ploss'):
			from .Configure_.Ploss import Ploss
			self._ploss = Ploss(self._core, self._base)
		return self._ploss

	# noinspection PyTypeChecker
	def get_display(self) -> enums.MeasTab:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: value: enums.MeasTab = driver.configure.get_display() \n
		Selects the displayed measurement tab. This command is useful, if you want to observe the GUI during remote control. The
		GUI controls are disabled in that case, so that you cannot select a tab via the GUI. To display the GUI,
		use SYSTem:DISPlay:UPDate ON. \n
			:return: meas_tab: POWer | SPECtrum | FFTSanalyzer | IQRecorder | IQVSlot | EPSensor
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.MeasTab)

	def set_display(self, meas_tab: enums.MeasTab) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.set_display(meas_tab = enums.MeasTab.EPSensor) \n
		Selects the displayed measurement tab. This command is useful, if you want to observe the GUI during remote control. The
		GUI controls are disabled in that case, so that you cannot select a tab via the GUI. To display the GUI,
		use SYSTem:DISPlay:UPDate ON. \n
			:param meas_tab: POWer | SPECtrum | FFTSanalyzer | IQRecorder | IQVSlot | EPSensor
		"""
		param = Conversions.enum_scalar_to_str(meas_tab, enums.MeasTab)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:DISPlay {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
