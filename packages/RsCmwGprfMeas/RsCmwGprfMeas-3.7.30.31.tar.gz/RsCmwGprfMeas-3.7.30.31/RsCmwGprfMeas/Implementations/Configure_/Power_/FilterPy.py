from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	@property
	def bandpass(self):
		"""bandpass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandpass'):
			from .FilterPy_.Bandpass import Bandpass
			self._bandpass = Bandpass(self._core, self._base)
		return self._bandpass

	@property
	def gauss(self):
		"""gauss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gauss'):
			from .FilterPy_.Gauss import Gauss
			self._gauss = Gauss(self._core, self._base)
		return self._gauss

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DigitalFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE \n
		Snippet: value: enums.DigitalFilterType = driver.configure.power.filterPy.get_type_py() \n
		Selects the IF filter type. \n
			:return: filter_type: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: Bandpass filter with selectable bandwidth GAUSs: Filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DigitalFilterType)

	def set_type_py(self, filter_type: enums.DigitalFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE \n
		Snippet: driver.configure.power.filterPy.set_type_py(filter_type = enums.DigitalFilterType.BANDpass) \n
		Selects the IF filter type. \n
			:param filter_type: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: Bandpass filter with selectable bandwidth GAUSs: Filter of Gaussian shape with selectable bandwidth WCDMA: 3.84 MHz RRC filter with a roll-off = 0.22 for WCDMA TX tests CDMA: 1.2288 MHz-wide channel filter for CDMA 2000 TX tests TDSCdma: 1.28 MHz RRC filter with a roll-off = 0.22 for TD-SCDMA TX tests
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.DigitalFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
