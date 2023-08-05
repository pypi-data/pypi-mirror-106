from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Retrigger:
	"""Retrigger commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("retrigger", core, parent)

	def set(self, index: int, retrigger: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger \n
		Snippet: driver.configure.power.listPy.retrigger.set(index = 1, retrigger = False) \n
		Enables the retrigger mechanism for a selected list segment. The setting is relevant for trigger mode 'Retrigger
		Preselect' (method RsCmwGprfMeas.Trigger.Power.mode PRESelect) . \n
			:param index: List segment index Range: 0 to 3999
			:param retrigger: OFF | ON Disables or enables retriggering for segment Index.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('retrigger', retrigger, DataType.Boolean))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger \n
		Snippet: value: bool = driver.configure.power.listPy.retrigger.get(index = 1) \n
		Enables the retrigger mechanism for a selected list segment. The setting is relevant for trigger mode 'Retrigger
		Preselect' (method RsCmwGprfMeas.Trigger.Power.mode PRESelect) . \n
			:param index: List segment index Range: 0 to 3999
			:return: retrigger: OFF | ON Disables or enables retriggering for segment Index."""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger? {param}')
		return Conversions.str_to_bool(response)

	def get_all(self) -> List[bool]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger:ALL \n
		Snippet: value: List[bool] = driver.configure.power.listPy.retrigger.get_all() \n
		Enables or disables the retrigger mechanism after the individual frequency/level steps. The setting is relevant for the
		trigger mode 'Retrigger Preselect' (method RsCmwGprfMeas.Trigger.Power.modePRESelect) . \n
			:return: retrigger: OFF | ON Comma-separated list of up to 2000 values, with one value per frequency/level step A query returns 2000 values (maximum number of steps) .
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger:ALL?')
		return Conversions.str_to_bool_list(response)

	def set_all(self, retrigger: List[bool]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger:ALL \n
		Snippet: driver.configure.power.listPy.retrigger.set_all(retrigger = [True, False, True]) \n
		Enables or disables the retrigger mechanism after the individual frequency/level steps. The setting is relevant for the
		trigger mode 'Retrigger Preselect' (method RsCmwGprfMeas.Trigger.Power.modePRESelect) . \n
			:param retrigger: OFF | ON Comma-separated list of up to 2000 values, with one value per frequency/level step A query returns 2000 values (maximum number of steps) .
		"""
		param = Conversions.list_to_csv_str(retrigger)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:RETRigger:ALL {param}')
