from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delays:
	"""Delays commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("delays", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Restart_Marker: float: No parameter help available
			- Marker_1: float: No parameter help available
			- Marker_2: float: No parameter help available
			- Marker_3: float: No parameter help available
			- Marker_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Restart_Marker'),
			ArgStruct.scalar_float('Marker_1'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Restart_Marker: float = None
			self.Marker_1: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL \n
		Snippet: value: AllStruct = driver.source.gprf.generator.sequencer.marker.delays.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.marker.delays.set_all(value = AllStruct()) \n
		No command help available \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays:ALL', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Restart_Marker: float: No parameter help available
			- Marker_2: float: No parameter help available
			- Marker_3: float: No parameter help available
			- Marker_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Restart_Marker'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Restart_Marker: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: value: ValueStruct = driver.source.gprf.generator.sequencer.marker.delays.get_value() \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays \n
		Snippet: driver.source.gprf.generator.sequencer.marker.delays.set_value(value = ValueStruct()) \n
		Defines delay times for the ARB output trigger events relative to the marker events. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:MARKer:DELays', value)
