from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connector", core, parent)

	def set(self, index: int, cmws_connector: enums.CmwsConnector) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector \n
		Snippet: driver.configure.power.listPy.singleCmw.connector.set(index = 1, cmws_connector = enums.CmwsConnector.R11) \n
		Selects the RF input connector for a selected list entry for GPRF power list mode measurements with the R&S CMWS or with
		an instrument with integrated connector bench. This setting is only relevant for connector mode LIST, see method
		RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.cmode. All list entries must use connectors of the same bench.
		For possible connector values, see 'Values for RF Path Selection'. \n
			:param index: Selects the list entry Range: 0 to 3999
			:param cmws_connector: Selects the input connector of the connector bench
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('cmws_connector', cmws_connector, DataType.Enum))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, index: int) -> enums.CmwsConnector:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector \n
		Snippet: value: enums.CmwsConnector = driver.configure.power.listPy.singleCmw.connector.get(index = 1) \n
		Selects the RF input connector for a selected list entry for GPRF power list mode measurements with the R&S CMWS or with
		an instrument with integrated connector bench. This setting is only relevant for connector mode LIST, see method
		RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.cmode. All list entries must use connectors of the same bench.
		For possible connector values, see 'Values for RF Path Selection'. \n
			:param index: Selects the list entry Range: 0 to 3999
			:return: cmws_connector: Selects the input connector of the connector bench"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CmwsConnector)

	def get_all(self) -> List[float]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector:ALL \n
		Snippet: value: List[float] = driver.configure.power.listPy.singleCmw.connector.get_all() \n
		Selects the RF input connectors for the first n list entries (n=1 to 4000) . Only for GPRF power list mode measurements
		with the R&S CMWS or with an instrument with integrated connector bench. This setting is only relevant for connector mode
		LIST, see method RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.cmode. All list entries must use connectors of the same
		bench. For possible connector values, see 'Values for RF Path Selection'. \n
			:return: cmws_connector: Selects the input connector of the connector bench Comma-separated list of n settings, for segment 0 to n-1
		"""
		response = self._core.io.query_bin_or_ascii_float_list('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector:ALL?')
		return response

	def set_all(self, cmws_connector: List[float]) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector:ALL \n
		Snippet: driver.configure.power.listPy.singleCmw.connector.set_all(cmws_connector = [1.1, 2.2, 3.3]) \n
		Selects the RF input connectors for the first n list entries (n=1 to 4000) . Only for GPRF power list mode measurements
		with the R&S CMWS or with an instrument with integrated connector bench. This setting is only relevant for connector mode
		LIST, see method RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.cmode. All list entries must use connectors of the same
		bench. For possible connector values, see 'Values for RF Path Selection'. \n
			:param cmws_connector: Selects the input connector of the connector bench Comma-separated list of n settings, for segment 0 to n-1
		"""
		param = Conversions.list_to_csv_str(cmws_connector)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CONNector:ALL {param}')
