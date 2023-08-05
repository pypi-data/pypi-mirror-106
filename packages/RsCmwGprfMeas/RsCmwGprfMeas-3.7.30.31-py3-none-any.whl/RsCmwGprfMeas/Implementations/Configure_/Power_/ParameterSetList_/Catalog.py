from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get_pdef_set(self) -> List[str]:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:CATalog:PDEFset \n
		Snippet: value: List[str] = driver.configure.power.parameterSetList.catalog.get_pdef_set() \n
		Gets a comma-separated list of predefined parameter sets that can be loaded as parameter set in retriggered list mode
		(see method RsCmwGprfMeas.Configure.Power.ParameterSetList.PdefSet.set) . See also 'Measurement Settings and Predefined
		Parameter Sets' \n
			:return: predefined_set: Examples for strings: 'GSM Power','WCDMA UE Power','WCDMA Off Power','LTE TX Power 20','LTE OFF Power 20','Customized'
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET:CATalog:PDEFset?')
		return Conversions.str_to_str_list(response)
