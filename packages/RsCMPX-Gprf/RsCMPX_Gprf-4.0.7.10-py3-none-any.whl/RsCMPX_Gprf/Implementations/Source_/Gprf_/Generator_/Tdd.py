from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdd:
	"""Tdd commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tdd", core, parent)

	def get_mode(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:TDD:MODE \n
		Snippet: value: bool = driver.source.gprf.generator.tdd.get_mode() \n
		No command help available \n
			:return: tdd_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:TDD:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, tdd_mode: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:TDD:MODE \n
		Snippet: driver.source.gprf.generator.tdd.set_mode(tdd_mode = False) \n
		No command help available \n
			:param tdd_mode: No help available
		"""
		param = Conversions.bool_to_str(tdd_mode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:TDD:MODE {param}')

	# noinspection PyTypeChecker
	def get_marker(self) -> enums.TddMarker:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:TDD:MARKer \n
		Snippet: value: enums.TddMarker = driver.source.gprf.generator.tdd.get_marker() \n
		No command help available \n
			:return: tdd_marker: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:TDD:MARKer?')
		return Conversions.str_to_scalar_enum(response, enums.TddMarker)

	def set_marker(self, tdd_marker: enums.TddMarker) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:TDD:MARKer \n
		Snippet: driver.source.gprf.generator.tdd.set_marker(tdd_marker = enums.TddMarker.NONE) \n
		No command help available \n
			:param tdd_marker: No help available
		"""
		param = Conversions.enum_scalar_to_str(tdd_marker, enums.TddMarker)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:TDD:MARKer {param}')
