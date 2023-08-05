from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("typePy", core, parent)

	def set(self, index: int, filter_py: enums.DigitalFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE \n
		Snippet: driver.configure.power.parameterSetList.filterPy.typePy.set(index = 1, filter_py = enums.DigitalFilterType.BANDpass) \n
		Selects the IF filter type for a particular parameter set <index>. \n
			:param index: Number of the parameter set in the list Range: 0 to 31
			:param filter_py: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter with selectable bandwidth GAUSs: filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('filter_py', filter_py, DataType.Enum))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, index: int) -> enums.DigitalFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE \n
		Snippet: value: enums.DigitalFilterType = driver.configure.power.parameterSetList.filterPy.typePy.get(index = 1) \n
		Selects the IF filter type for a particular parameter set <index>. \n
			:param index: Number of the parameter set in the list Range: 0 to 31
			:return: filter_py: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter with selectable bandwidth GAUSs: filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.DigitalFilterType)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.DigitalFilterType]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL \n
		Snippet: value: List[enums.DigitalFilterType] = driver.configure.power.parameterSetList.filterPy.typePy.get_all() \n
		Selects the IF filter type for all parameter sets. \n
			:return: filter_py: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma Comma-separated list of 32 values, for parameter set no. 0 to 31 BANDpass: Bandpass filter with selectable bandwidth GAUSs: Filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL?')
		return Conversions.str_to_list_enum(response, enums.DigitalFilterType)

	def set_all(self, filter_py: List[enums.DigitalFilterType]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL \n
		Snippet: driver.configure.power.parameterSetList.filterPy.typePy.set_all(filter_py = [DigitalFilterType.BANDpass, DigitalFilterType.WCDMa]) \n
		Selects the IF filter type for all parameter sets. \n
			:param filter_py: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma Comma-separated list of 32 values, for parameter set no. 0 to 31 BANDpass: Bandpass filter with selectable bandwidth GAUSs: Filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests
		"""
		param = Conversions.enum_list_to_str(filter_py, enums.DigitalFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:FILTer:TYPE:ALL {param}')
