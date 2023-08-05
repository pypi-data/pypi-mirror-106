from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 10 total commands, 2 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

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

	def get_slength(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth \n
		Snippet: value: float = driver.configure.iqRecorder.listPy.get_slength() \n
		Selects the time between the beginning of two consecutive measurement steps. \n
			:return: step_length: Range: 100E-6 s to 0.1 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth?')
		return Conversions.str_to_float(response)

	def set_slength(self, step_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth \n
		Snippet: driver.configure.iqRecorder.listPy.set_slength(step_length = 1.0) \n
		Selects the time between the beginning of two consecutive measurement steps. \n
			:param step_length: Range: 100E-6 s to 0.1 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SLENgth {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:COUNt \n
		Snippet: value: int = driver.configure.iqRecorder.listPy.get_count() \n
		Queries the total number of results, given by <StopIndex> – <StartIndex> + 1 (see method RsCmwGprfMeas.Configure.
		IqRecorder.ListPy.start and method RsCmwGprfMeas.Configure.IqRecorder.ListPy.stop) . \n
			:return: result_count: Range: 1 to 2000
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt \n
		Snippet: value: int = driver.configure.iqRecorder.listPy.get_start() \n
		Start index, defines the first frequency/level step in the frequency/level list that is measured. The value must not
		exceed the stop index defined by method RsCmwGprfMeas.Configure.IqRecorder.ListPy.stop. \n
			:return: start_index: Range: 0 to 1999
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt \n
		Snippet: driver.configure.iqRecorder.listPy.set_start(start_index = 1) \n
		Start index, defines the first frequency/level step in the frequency/level list that is measured. The value must not
		exceed the stop index defined by method RsCmwGprfMeas.Configure.IqRecorder.ListPy.stop. \n
			:param start_index: Range: 0 to 1999
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP \n
		Snippet: value: int = driver.configure.iqRecorder.listPy.get_stop() \n
		Stop index, defines the last frequency/level step in the frequency/level list that is measured. The value must not be
		smaller than the start index defined by method RsCmwGprfMeas.Configure.IqRecorder.ListPy.start. \n
			:return: stop_index: Range: 0 to 1999
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP \n
		Snippet: driver.configure.iqRecorder.listPy.set_stop(stop_index = 1) \n
		Stop index, defines the last frequency/level step in the frequency/level list that is measured. The value must not be
		smaller than the start index defined by method RsCmwGprfMeas.Configure.IqRecorder.ListPy.start. \n
			:param stop_index: Range: 0 to 1999
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:STOP {param}')

	# noinspection PyTypeChecker
	class SstopStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: Range: 0 to 1999
			- Stop_Index: int: Range: 0 to 1999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Stop_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Stop_Index: int = None

	def get_sstop(self) -> SstopStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SSTop \n
		Snippet: value: SstopStruct = driver.configure.iqRecorder.listPy.get_sstop() \n
		Start index and stop index, defines the first and last frequency/level step in the frequency/level list that is measured.
		The start index must not exceed the stop index. \n
			:return: structure: for return value, see the help for SstopStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SSTop?', self.__class__.SstopStruct())

	def set_sstop(self, value: SstopStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SSTop \n
		Snippet: driver.configure.iqRecorder.listPy.set_sstop(value = SstopStruct()) \n
		Start index and stop index, defines the first and last frequency/level step in the frequency/level list that is measured.
		The start index must not exceed the stop index. \n
			:param value: see the help for SstopStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST:SSTop', value)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST \n
		Snippet: value: bool = driver.configure.iqRecorder.listPy.get_value() \n
		Enables or disables the list mode for the I/Q recorder. \n
			:return: enable_list_mode: OFF | ON OFF: list mode off (single power step) ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST \n
		Snippet: driver.configure.iqRecorder.listPy.set_value(enable_list_mode = False) \n
		Enables or disables the list mode for the I/Q recorder. \n
			:param enable_list_mode: OFF | ON OFF: list mode off (single power step) ON: list mode on
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
