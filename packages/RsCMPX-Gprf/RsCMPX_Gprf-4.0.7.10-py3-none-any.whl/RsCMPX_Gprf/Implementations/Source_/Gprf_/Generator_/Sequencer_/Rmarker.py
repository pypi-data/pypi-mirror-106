from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmarker:
	"""Rmarker commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmarker", core, parent)

	def get_delay(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RMARker:DELay \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.rmarker.get_delay() \n
		Defines a delay time for the ARB output trigger events relative to the restart marker events. \n
			:return: restart_marker: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:RMARker:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, restart_marker: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RMARker:DELay \n
		Snippet: driver.source.gprf.generator.sequencer.rmarker.set_delay(restart_marker = 1.0) \n
		Defines a delay time for the ARB output trigger events relative to the restart marker events. \n
			:param restart_marker: No help available
		"""
		param = Conversions.decimal_value_to_str(restart_marker)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:RMARker:DELay {param}')
