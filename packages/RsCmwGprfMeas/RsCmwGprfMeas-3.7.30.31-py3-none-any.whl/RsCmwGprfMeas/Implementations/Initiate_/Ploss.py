from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ploss", core, parent)

	# noinspection PyTypeChecker
	class OpenStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: RF connector of the path to be measured
			- Path_Index: enums.PathIndex: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the setting if you have only one path at the connector."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connector', enums.CmwsConnector),
			ArgStruct.scalar_enum('Path_Index', enums.PathIndex)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector: enums.CmwsConnector = None
			self.Path_Index: enums.PathIndex = None

	# noinspection PyTypeChecker
	def get_open(self) -> OpenStruct:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN \n
		Snippet: value: OpenStruct = driver.initiate.ploss.get_open() \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:return: structure: for return value, see the help for OpenStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN?', self.__class__.OpenStruct())

	def set_open(self, value: OpenStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN \n
		Snippet: driver.initiate.ploss.set_open(value = OpenStruct()) \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:param value: see the help for OpenStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN', value)

	# noinspection PyTypeChecker
	class ShortStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: RF connector of the path to be measured
			- Path_Index: enums.PathIndex: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the setting if you have only one path at the connector."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connector', enums.CmwsConnector),
			ArgStruct.scalar_enum('Path_Index', enums.PathIndex)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector: enums.CmwsConnector = None
			self.Path_Index: enums.PathIndex = None

	# noinspection PyTypeChecker
	def get_short(self) -> ShortStruct:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: value: ShortStruct = driver.initiate.ploss.get_short() \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:return: structure: for return value, see the help for ShortStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt?', self.__class__.ShortStruct())

	def set_short(self, value: ShortStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: driver.initiate.ploss.set_short(value = ShortStruct()) \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:param value: see the help for ShortStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt', value)

	# noinspection PyTypeChecker
	class EvaluateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: RF connector of the path to be measured
			- Path_Index: enums.PathIndex: P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 Path index, default value P1 Skip the setting if you have only one path at the connector."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Connector', enums.CmwsConnector),
			ArgStruct.scalar_enum('Path_Index', enums.PathIndex)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector: enums.CmwsConnector = None
			self.Path_Index: enums.PathIndex = None

	# noinspection PyTypeChecker
	def get_evaluate(self) -> EvaluateStruct:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate \n
		Snippet: value: EvaluateStruct = driver.initiate.ploss.get_evaluate() \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:return: structure: for return value, see the help for EvaluateStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate?', self.__class__.EvaluateStruct())

	def set_evaluate(self, value: EvaluateStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate \n
		Snippet: driver.initiate.ploss.set_evaluate(value = EvaluateStruct()) \n
		Sets the measurement mode according to the last mnemonic ('Open', 'Short' or 'Eval') . Selects an RF connector and
		optionally a path of that connector. Starts the measurement. For possible connector values, see 'Values for RF Path
		Selection'. \n
			:param value: see the help for EvaluateStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate', value)
