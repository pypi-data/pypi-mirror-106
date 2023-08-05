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
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger \n
		Snippet: driver.configure.iqVsSlot.listPy.retrigger.set(index = 1, retrigger = False) \n
		Enables the retrigger mechanism after a selected frequency/level step. The setting is relevant for trigger mode
		'Retrigger Preselect' (method RsCmwGprfMeas.Trigger.IqVsSlot.mode PRESelect) . \n
			:param index: Number of the frequency/level step in the table Range: 0 to 199
			:param retrigger: OFF | ON Disables or enables retriggering after the frequency/level step.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('retrigger', retrigger, DataType.Boolean))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger \n
		Snippet: value: bool = driver.configure.iqVsSlot.listPy.retrigger.get(index = 1) \n
		Enables the retrigger mechanism after a selected frequency/level step. The setting is relevant for trigger mode
		'Retrigger Preselect' (method RsCmwGprfMeas.Trigger.IqVsSlot.mode PRESelect) . \n
			:param index: Number of the frequency/level step in the table Range: 0 to 199
			:return: retrigger: OFF | ON Disables or enables retriggering after the frequency/level step."""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger? {param}')
		return Conversions.str_to_bool(response)

	def get_all(self) -> List[bool]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger:ALL \n
		Snippet: value: List[bool] = driver.configure.iqVsSlot.listPy.retrigger.get_all() \n
		Enables the retrigger mechanism after all frequency/level steps. The setting is relevant for trigger mode 'Retrigger
		Preselect' (method RsCmwGprfMeas.Trigger.IqVsSlot.modePRESelect) . \n
			:return: retrigger: OFF | ON Comma-separated list of n values, one value per frequency/level step, where n ≤ 200. The query returns 200 results.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger:ALL?')
		return Conversions.str_to_bool_list(response)

	def set_all(self, retrigger: List[bool]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger:ALL \n
		Snippet: driver.configure.iqVsSlot.listPy.retrigger.set_all(retrigger = [True, False, True]) \n
		Enables the retrigger mechanism after all frequency/level steps. The setting is relevant for trigger mode 'Retrigger
		Preselect' (method RsCmwGprfMeas.Trigger.IqVsSlot.modePRESelect) . \n
			:param retrigger: OFF | ON Comma-separated list of n values, one value per frequency/level step, where n ≤ 200. The query returns 200 results.
		"""
		param = Conversions.list_to_csv_str(retrigger)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:RETRigger:ALL {param}')
