from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("marker", core, parent)

	# noinspection PyTypeChecker
	class DelaysStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Marker_2: int: No parameter help available
			- Marker_3: int: No parameter help available
			- Marker_4: int: No parameter help available
			- Restart_Marker: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Marker_2'),
			ArgStruct.scalar_int('Marker_3'),
			ArgStruct.scalar_int('Marker_4'),
			ArgStruct.scalar_int('Restart_Marker')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Marker_2: int = None
			self.Marker_3: int = None
			self.Marker_4: int = None
			self.Restart_Marker: int = None

	def get_delays(self) -> DelaysStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: value: DelaysStruct = driver.source.gprf.generator.arb.marker.get_delays() \n
		No command help available \n
			:return: structure: for return value, see the help for DelaysStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays?', self.__class__.DelaysStruct())

	def set_delays(self, value: DelaysStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays \n
		Snippet: driver.source.gprf.generator.arb.marker.set_delays(value = DelaysStruct()) \n
		No command help available \n
			:param value: see the help for DelaysStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:ARB:MARKer:DELays', value)
