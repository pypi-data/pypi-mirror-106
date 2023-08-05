from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 23 total commands, 7 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	@property
	def iqData(self):
		"""iqData commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_iqData'):
			from .ListPy_.IqData import IqData
			self._iqData = IqData(self._core, self._base)
		return self._iqData

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .ListPy_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_envelopePower'):
			from .ListPy_.EnvelopePower import EnvelopePower
			self._envelopePower = EnvelopePower(self._core, self._base)
		return self._envelopePower

	@property
	def retrigger(self):
		"""retrigger commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_retrigger'):
			from .ListPy_.Retrigger import Retrigger
			self._retrigger = Retrigger(self._core, self._base)
		return self._retrigger

	@property
	def irepetition(self):
		"""irepetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_irepetition'):
			from .ListPy_.Irepetition import Irepetition
			self._irepetition = Irepetition(self._core, self._base)
		return self._irepetition

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .ListPy_.ParameterSetList import ParameterSetList
			self._parameterSetList = ParameterSetList(self._core, self._base)
		return self._parameterSetList

	# noinspection PyTypeChecker
	def get_txi_timing(self) -> enums.Timing:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: value: enums.Timing = driver.configure.power.listPy.get_txi_timing() \n
		Specifies the timing of the generated 'GPRF Meas<i>:Power' trigger. \n
			:return: timing: STEP | CENTered STEP: Trigger signals are generated at the step boundaries. CENTered: Trigger signals are generated in the middle of the gaps between subsequent measurement intervals.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming?')
		return Conversions.str_to_scalar_enum(response, enums.Timing)

	def set_txi_timing(self, timing: enums.Timing) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: driver.configure.power.listPy.set_txi_timing(timing = enums.Timing.CENTered) \n
		Specifies the timing of the generated 'GPRF Meas<i>:Power' trigger. \n
			:param timing: STEP | CENTered STEP: Trigger signals are generated at the step boundaries. CENTered: Trigger signals are generated in the middle of the gaps between subsequent measurement intervals.
		"""
		param = Conversions.enum_scalar_to_str(timing, enums.Timing)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming {param}')

	# noinspection PyTypeChecker
	def get_munit(self) -> enums.MagnitudeUnit:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: value: enums.MagnitudeUnit = driver.configure.power.listPy.get_munit() \n
		Selects the magnitude unit for I/Q measurement results. \n
			:return: magnitude_unit: VOLT | RAW Voltage units or raw I/Q data relative to full scale
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit?')
		return Conversions.str_to_scalar_enum(response, enums.MagnitudeUnit)

	def set_munit(self, magnitude_unit: enums.MagnitudeUnit) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: driver.configure.power.listPy.set_munit(magnitude_unit = enums.MagnitudeUnit.RAW) \n
		Selects the magnitude unit for I/Q measurement results. \n
			:param magnitude_unit: VOLT | RAW Voltage units or raw I/Q data relative to full scale
		"""
		param = Conversions.enum_scalar_to_str(magnitude_unit, enums.MagnitudeUnit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt \n
		Snippet: value: int = driver.configure.power.listPy.get_count() \n
		Queries the total number of steps (results) in the selected list section. The total number of results (segments with
		repetitions) is limited by 10000. \n
			:return: result_count: Range: 1 to 10E+3
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: value: int = driver.configure.power.listPy.get_start() \n
		Start index, defines the first list segment to be measured. The total number of results (segments with repetitions) in
		the selected list section must not be higher than 10000. \n
			:return: start_index: Range: 0 to 1999
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: driver.configure.power.listPy.set_start(start_index = 1) \n
		Start index, defines the first list segment to be measured. The total number of results (segments with repetitions) in
		the selected list section must not be higher than 10000. \n
			:param start_index: Range: 0 to 1999
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: value: int = driver.configure.power.listPy.get_stop() \n
		Stop index, defines the last list segment to be measured. The total number of results (segments with repetitions) in the
		selected list section must not be higher than 10000. \n
			:return: stop_index: Range: 0 to 3999
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: driver.configure.power.listPy.set_stop(stop_index = 1) \n
		Stop index, defines the last list segment to be measured. The total number of results (segments with repetitions) in the
		selected list section must not be higher than 10000. \n
			:param stop_index: Range: 0 to 3999
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP {param}')

	# noinspection PyTypeChecker
	class SstopStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: Range: 0 to 3999
			- Stop_Index: int: Range: 0 to 3999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Stop_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Stop_Index: int = None

	def get_sstop(self) -> SstopStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop \n
		Snippet: value: SstopStruct = driver.configure.power.listPy.get_sstop() \n
		Start and stop index of the list section to be measured. The total number of results (segments with repetitions) in the
		list section must not be higher than 10000. \n
			:return: structure: for return value, see the help for SstopStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop?', self.__class__.SstopStruct())

	def set_sstop(self, value: SstopStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop \n
		Snippet: driver.configure.power.listPy.set_sstop(value = SstopStruct()) \n
		Start and stop index of the list section to be measured. The total number of results (segments with repetitions) in the
		list section must not be higher than 10000. \n
			:param value: see the help for SstopStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop', value)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: value: bool = driver.configure.power.listPy.get_value() \n
		Enables or disables the list mode for the power measurement. \n
			:return: enable_list_mode: OFF | ON OFF: list mode off (single power step) ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: driver.configure.power.listPy.set_value(enable_list_mode = False) \n
		Enables or disables the list mode for the power measurement. \n
			:param enable_list_mode: OFF | ON OFF: list mode off (single power step) ON: list mode on
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
