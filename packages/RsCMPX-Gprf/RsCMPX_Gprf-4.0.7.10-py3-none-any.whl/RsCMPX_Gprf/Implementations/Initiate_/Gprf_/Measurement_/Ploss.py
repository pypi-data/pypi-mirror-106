from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ploss", core, parent)

	# noinspection PyTypeChecker
	class OpenStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: No parameter help available
			- Path_Index: enums.PathIndex: No parameter help available"""
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
		Snippet: value: OpenStruct = driver.initiate.gprf.measurement.ploss.get_open() \n
		No command help available \n
			:return: structure: for return value, see the help for OpenStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN?', self.__class__.OpenStruct())

	def set_open(self, value: OpenStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN \n
		Snippet: driver.initiate.gprf.measurement.ploss.set_open(value = OpenStruct()) \n
		No command help available \n
			:param value: see the help for OpenStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:OPEN', value)

	# noinspection PyTypeChecker
	class ShortStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: No parameter help available
			- Path_Index: enums.PathIndex: No parameter help available"""
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
		Snippet: value: ShortStruct = driver.initiate.gprf.measurement.ploss.get_short() \n
		No command help available \n
			:return: structure: for return value, see the help for ShortStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt?', self.__class__.ShortStruct())

	def set_short(self, value: ShortStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt \n
		Snippet: driver.initiate.gprf.measurement.ploss.set_short(value = ShortStruct()) \n
		No command help available \n
			:param value: see the help for ShortStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:SHORt', value)

	# noinspection PyTypeChecker
	class EvaluateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Connector: enums.CmwsConnector: No parameter help available
			- Path_Index: enums.PathIndex: No parameter help available"""
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
		Snippet: value: EvaluateStruct = driver.initiate.gprf.measurement.ploss.get_evaluate() \n
		No command help available \n
			:return: structure: for return value, see the help for EvaluateStruct structure arguments.
		"""
		return self._core.io.query_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate?', self.__class__.EvaluateStruct())

	def set_evaluate(self, value: EvaluateStruct) -> None:
		"""SCPI: INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate \n
		Snippet: driver.initiate.gprf.measurement.ploss.set_evaluate(value = EvaluateStruct()) \n
		No command help available \n
			:param value: see the help for EvaluateStruct structure arguments.
		"""
		self._core.io.write_struct('INITiate:GPRF:MEASurement<Instance>:PLOSs:EVALuate', value)
