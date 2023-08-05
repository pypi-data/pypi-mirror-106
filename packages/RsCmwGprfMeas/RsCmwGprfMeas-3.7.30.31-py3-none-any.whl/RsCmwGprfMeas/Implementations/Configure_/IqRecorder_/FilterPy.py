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
	def get_type_py(self) -> enums.RbwFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:TYPE \n
		Snippet: value: enums.RbwFilterType = driver.configure.iqRecorder.filterPy.get_type_py() \n
		Selects the IF filter type. Gauss filters have shorter settling times and therefore larger sampling rates.
		Bandpass filters have a flat passband and steeper edges. See also 'Filter Settings and Samples'. \n
			:return: filter_type: BANDpass | GAUSs BANDpass: bandpass filter with variable bandwidth GAUSs: filter of Gaussian shape with variable bandwidth
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.RbwFilterType)

	def set_type_py(self, filter_type: enums.RbwFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:TYPE \n
		Snippet: driver.configure.iqRecorder.filterPy.set_type_py(filter_type = enums.RbwFilterType.BANDpass) \n
		Selects the IF filter type. Gauss filters have shorter settling times and therefore larger sampling rates.
		Bandpass filters have a flat passband and steeper edges. See also 'Filter Settings and Samples'. \n
			:param filter_type: BANDpass | GAUSs BANDpass: bandpass filter with variable bandwidth GAUSs: filter of Gaussian shape with variable bandwidth
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.RbwFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
