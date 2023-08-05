from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get_pdef_set(self) -> List[str]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:CATalog:PDEFset \n
		Snippet: value: List[str] = driver.configure.power.catalog.get_pdef_set() \n
		Gets a comma/separated list of predefined parameter sets that can be loaded or queried using method RsCmwGprfMeas.
		Configure.Power.pdefSet. Currently there are the following predefined parameter sets: 'GSM Power','WCDMA UE Power','WCDMA
		Off Power','TDSCDMA UE Power','TDSCDMA Off Power','CDMA MS Power Wide','CDMA MS Power 1.23','1xEVDO MS Power Wide',
		'1xEVDO MS Power 1.23','LTE TX Power 20','LTE OFF Power 20','LTE TX Power 15','LTE OFF Power 15','LTE TX Power 10','LTE
		OFF Power 10','LTE TX Power 5','LTE OFF Power 5','LTE TX Power 3','LTE OFF Power 3','LTE TX Power 1.4','LTE OFF Power 1.
		4','Bluetooth DH1','Bluetooth DH3','Bluetooth DH5','WLAN a','WLAN b','WLAN n 20','WLAN n 40','WiMAX 10','WiMAX 8.
		75','WiMAX 7','WiMAX 5','WiMAX 3.5','Customized' (see 'Measurement Settings and Predefined Parameter Sets') . \n
			:return: predefined_set: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:CATalog:PDEFset?')
		return Conversions.str_to_str_list(response)
