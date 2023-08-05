from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Call:
	"""Call commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("call", core, parent)

	def set(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:CALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.entry.call.set() \n
		Deletes all entries of the sequencer list and creates an entry with default settings. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:CALL')

	def set_with_opc(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:CALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.entry.call.set_with_opc() \n
		Deletes all entries of the sequencer list and creates an entry with default settings. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:CALL')
