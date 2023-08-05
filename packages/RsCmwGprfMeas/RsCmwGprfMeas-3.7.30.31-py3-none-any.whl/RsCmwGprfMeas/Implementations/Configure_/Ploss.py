from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ploss", core, parent)

	@property
	def view(self):
		"""view commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_view'):
			from .Ploss_.View import View
			self._view = View(self._core, self._base)
		return self._view

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .Ploss_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def mpath(self):
		"""mpath commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mpath'):
			from .Ploss_.Mpath import Mpath
			self._mpath = Mpath(self._core, self._base)
		return self._mpath

	def get_trace(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: value: bool = driver.configure.ploss.get_trace() \n
		Selects whether a result diagram is provided. \n
			:return: trace_mode: OFF | ON OFF: no result diagram, faster measurement ON: result diagram, slower measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe?')
		return Conversions.str_to_bool(response)

	def set_trace(self, trace_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: driver.configure.ploss.set_trace(trace_mode = False) \n
		Selects whether a result diagram is provided. \n
			:param trace_mode: OFF | ON OFF: no result diagram, faster measurement ON: result diagram, slower measurement
		"""
		param = Conversions.bool_to_str(trace_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe {param}')

	def clone(self) -> 'Ploss':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ploss(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
