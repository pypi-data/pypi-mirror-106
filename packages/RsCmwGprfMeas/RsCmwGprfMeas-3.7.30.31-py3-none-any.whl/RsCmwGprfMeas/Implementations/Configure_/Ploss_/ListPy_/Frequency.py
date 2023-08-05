from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	def set(self, connector: enums.CmwsConnector, num_entries: int, frequency: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency \n
		Snippet: driver.configure.ploss.listPy.frequency.set(connector = enums.CmwsConnector.R11, num_entries = 1, frequency = [1.1, 2.2, 3.3]) \n
		Configures the frequency list for a selected RF connector, path index 1. Use this command if you have only a single
		signal path at the RF connector. For possible connector values, see 'Values for RF Path Selection'.
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param connector: RF connector for which the frequency list is configured
			:param num_entries: Configures the number of frequencies to be defined Range: 1 to 200
			:param frequency: Comma-separated list of NumEntries frequencies Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.Enum), ArgSingle('num_entries', num_entries, DataType.Integer), ArgSingle.as_open_list('frequency', frequency, DataType.FloatList))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Num_Entries: int: Configures the number of frequencies to be defined Range: 1 to 200
			- Frequency: List[float]: Comma-separated list of NumEntries frequencies Range: 70 MHz to 6 GHz, Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Num_Entries'),
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Num_Entries: int = None
			self.Frequency: List[float] = None

	def get(self, connector: enums.CmwsConnector) -> GetStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency \n
		Snippet: value: GetStruct = driver.configure.ploss.listPy.frequency.get(connector = enums.CmwsConnector.R11) \n
		Configures the frequency list for a selected RF connector, path index 1. Use this command if you have only a single
		signal path at the RF connector. For possible connector values, see 'Values for RF Path Selection'.
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. Refer to the preface of your model-specific base unit manual. \n
			:param connector: RF connector for which the frequency list is configured
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(connector, enums.CmwsConnector)
		return self._core.io.query_struct(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:LIST:FREQuency? {param}', self.__class__.GetStruct())
