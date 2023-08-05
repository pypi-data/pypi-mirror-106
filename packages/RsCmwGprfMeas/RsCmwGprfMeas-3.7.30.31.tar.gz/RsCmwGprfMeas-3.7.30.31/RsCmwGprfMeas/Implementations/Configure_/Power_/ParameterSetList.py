from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ParameterSetList:
	"""ParameterSetList commands group definition. 13 total commands, 5 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("parameterSetList", core, parent)

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_slength'):
			from .ParameterSetList_.Slength import Slength
			self._slength = Slength(self._core, self._base)
		return self._slength

	@property
	def mlength(self):
		"""mlength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mlength'):
			from .ParameterSetList_.Mlength import Mlength
			self._mlength = Mlength(self._core, self._base)
		return self._mlength

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .ParameterSetList_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .ParameterSetList_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def pdefSet(self):
		"""pdefSet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdefSet'):
			from .ParameterSetList_.PdefSet import PdefSet
			self._pdefSet = PdefSet(self._core, self._base)
		return self._pdefSet

	# noinspection PyTypeChecker
	def get_value(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET \n
		Snippet: value: enums.ParameterSetMode = driver.configure.power.parameterSetList.get_value() \n
		Selects the measurement control settings for the power measurement. The list settings require a 'Retrigger Preselect'
		trigger mode (method RsCmwGprfMeas.Trigger.Power.mode PRESelect) . In this mode, the R&S CMW uses the parameter settings
		defined via method RsCmwGprfMeas.Configure.Power.ListPy.ParameterSetList.set. \n
			:return: parameter_set_mode: GLOBal | LIST GLOBal: Use global settings for all steps. LIST: Use step-specific settings.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:PSET?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_value(self, parameter_set_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:PSET \n
		Snippet: driver.configure.power.parameterSetList.set_value(parameter_set_mode = enums.ParameterSetMode.GLOBal) \n
		Selects the measurement control settings for the power measurement. The list settings require a 'Retrigger Preselect'
		trigger mode (method RsCmwGprfMeas.Trigger.Power.mode PRESelect) . In this mode, the R&S CMW uses the parameter settings
		defined via method RsCmwGprfMeas.Configure.Power.ListPy.ParameterSetList.set. \n
			:param parameter_set_mode: GLOBal | LIST GLOBal: Use global settings for all steps. LIST: Use step-specific settings.
		"""
		param = Conversions.enum_scalar_to_str(parameter_set_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:PSET {param}')

	def clone(self) -> 'ParameterSetList':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ParameterSetList(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
