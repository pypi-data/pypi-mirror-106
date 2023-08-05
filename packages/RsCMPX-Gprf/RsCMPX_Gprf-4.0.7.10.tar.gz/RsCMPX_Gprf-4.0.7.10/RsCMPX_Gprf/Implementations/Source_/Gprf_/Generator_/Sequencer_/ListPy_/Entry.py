from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Entry:
	"""Entry commands group definition. 5 total commands, 4 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("entry", core, parent)

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Entry_.Insert import Insert
			self._insert = Insert(self._core, self._base)
		return self._insert

	@property
	def call(self):
		"""call commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_call'):
			from .Entry_.Call import Call
			self._call = Call(self._core, self._base)
		return self._call

	@property
	def mup(self):
		"""mup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mup'):
			from .Entry_.Mup import Mup
			self._mup = Mup(self._core, self._base)
		return self._mup

	@property
	def mdown(self):
		"""mdown commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mdown'):
			from .Entry_.Mdown import Mdown
			self._mdown = Mdown(self._core, self._base)
		return self._mdown

	def delete(self, index: int = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:DELete \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.entry.delete(index = 1) \n
		Deletes the selected entry from the sequencer list. You can specify <Index> to select that entry. Or you can select an
		entry via method RsCMPX_Gprf.Source.Gprf.Generator.Sequencer.ListPy.index. After the deletion, the selection moves to the
		next entry, if possible. Otherwise, it moves to the previous entry. \n
			:param index: Index of the entry to be deleted
		"""
		param = ''
		if index:
			param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ENTRy:DELete {param}'.strip())

	def clone(self) -> 'Entry':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Entry(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
