from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mlength:
	"""Mlength commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mlength", core, parent)

	def set(self, index: int, meas_length: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth \n
		Snippet: driver.configure.power.parameterSetList.mlength.set(index = 1, meas_length = 1.0) \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the 'Power' results for a particular
		parameter set <Index>. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.
		ParameterSetList.Slength.set) . \n
			:param index: Number of the parameter set Range: 0 to 31
			:param meas_length: Range: 10E-6 s to 1 s, Unit: s
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('meas_length', meas_length, DataType.Float))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth {param}'.rstrip())

	def get(self, index: int) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth \n
		Snippet: value: float = driver.configure.power.parameterSetList.mlength.get(index = 1) \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the 'Power' results for a particular
		parameter set <Index>. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.
		ParameterSetList.Slength.set) . \n
			:param index: Number of the parameter set Range: 0 to 31
			:return: meas_length: Range: 10E-6 s to 1 s, Unit: s"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth? {param}')
		return Conversions.str_to_float(response)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL \n
		Snippet: value: List[float] = driver.configure.power.parameterSetList.mlength.get_all() \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the 'Power' results for all parameter
		sets. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.ParameterSetList.
		Slength.all) . \n
			:return: meas_length: Comma-separated list of 32 values, for parameter set no. 0 to 31 Range: 10E-6 s to 1 s, Unit: s
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL?')
		return response

	def set_all(self, meas_length: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL \n
		Snippet: driver.configure.power.parameterSetList.mlength.set_all(meas_length = [1.1, 2.2, 3.3]) \n
		Selects the length of the averaging intervals that the R&S CMW uses to calculate the 'Power' results for all parameter
		sets. The measurement length must not exceed the step length (method RsCmwGprfMeas.Configure.Power.ParameterSetList.
		Slength.all) . \n
			:param meas_length: Comma-separated list of 32 values, for parameter set no. 0 to 31 Range: 10E-6 s to 1 s, Unit: s
		"""
		param = Conversions.list_to_csv_str(meas_length)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:MLENgth:ALL {param}')
