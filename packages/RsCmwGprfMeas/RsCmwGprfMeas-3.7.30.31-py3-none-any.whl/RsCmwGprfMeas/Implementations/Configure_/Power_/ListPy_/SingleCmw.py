from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCmw:
	"""SingleCmw commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("singleCmw", core, parent)

	@property
	def connector(self):
		"""connector commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_connector'):
			from .SingleCmw_.Connector import Connector
			self._connector = Connector(self._core, self._base)
		return self._connector

	# noinspection PyTypeChecker
	def get_cmode(self) -> enums.ParameterSetMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CMODe \n
		Snippet: value: enums.ParameterSetMode = driver.configure.power.listPy.singleCmw.get_cmode() \n
		Specifies how the input connector is selected for GPRF power list mode measurements with the R&S CMWS or an instrument
		with integrated connector bench. \n
			:return: cmws_connector_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ParameterSetMode)

	def set_cmode(self, cmws_connector_mode: enums.ParameterSetMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CMODe \n
		Snippet: driver.configure.power.listPy.singleCmw.set_cmode(cmws_connector_mode = enums.ParameterSetMode.GLOBal) \n
		Specifies how the input connector is selected for GPRF power list mode measurements with the R&S CMWS or an instrument
		with integrated connector bench. \n
			:param cmws_connector_mode: GLOBal | LIST GLOBal: The same input connector is used for all list entries. It is selected in the same way as without list mode, for example via ROUTe:GPRF:MEASi:SCENario:SALone. LIST: The input connector is configured individually for each list entry. See method RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.Connector.set and method RsCmwGprfMeas.Configure.Power.ListPy.SingleCmw.Connector.all.
		"""
		param = Conversions.enum_scalar_to_str(cmws_connector_mode, enums.ParameterSetMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:CMWS:CMODe {param}')

	def clone(self) -> 'SingleCmw':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SingleCmw(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
